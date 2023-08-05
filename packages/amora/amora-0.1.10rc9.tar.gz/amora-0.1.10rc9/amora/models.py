import inspect
import re
from dataclasses import dataclass, field
from enum import Enum, auto
from importlib.util import module_from_spec, spec_from_file_location
from inspect import getfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, Type, Union

from sqlalchemy import Column, MetaData, Table, select
from sqlalchemy.orm import declared_attr
from sqlalchemy.sql import ColumnElement
from sqlmodel import Field, Session, SQLModel, create_engine

from amora.config import settings
from amora.logger import logger
from amora.protocols import CompilableProtocol
from amora.types import Compilable
from amora.utils import list_files, model_path_for_target_path

select = select
Column = Column
ColumnElement = ColumnElement
Columns = Iterable[ColumnElement]
Field = Field
Model = Type["AmoraModel"]
MetaData = MetaData
Models = Iterable[Model]
Session = Session
create_engine = create_engine


@dataclass
class PartitionConfig:
    field: str
    data_type: str = "date"
    granularity: str = "day"
    range: Optional[Dict[str, Any]] = None


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class MaterializationTypes(AutoName):
    ephemeral = auto()
    view = auto()
    table = auto()


@dataclass
class ModelConfig:
    """
    Model configuration metadata

    Attributes:
        cluster_by (List[str]): BigQuery tables can be [clustered](https://cloud.google.com/bigquery/docs/clustered-tables) to colocate related data. Expects a list of columns, as strings.
        description (Optional[str]): A string description of the model, used for documentation
        labels (Dict[str,str]): A dict of labels that can be used for resource selection
        materialized (amora.models.MaterializationTypes): The materialization configuration: `view`, `table`, `ephemeral`. Default: `view`
        partition_by (Optional[PartitionConfig]): BigQuery supports the use of a [partition by](https://cloud.google.com/bigquery/docs/partitioned-tables) clause to easily partition a table by a column or expression. This option can help decrease latency and cost when querying large tables.
    """

    description: str = "Undocumented! Generated by Amora Data Build Tool 💚"
    materialized: MaterializationTypes = MaterializationTypes.view
    partition_by: Optional[PartitionConfig] = None
    cluster_by: List[str] = field(default_factory=list)
    labels: Dict[str, str] = field(default_factory=dict)


metadata = MetaData(schema=f"{settings.TARGET_PROJECT}.{settings.TARGET_SCHEMA}")


class AmoraModel(SQLModel):
    """
    Attributes:
        __depends_on__ (Models): A list of Amora Models that the current model depends on
        __model_config__ (ModelConfig): Model configuration metadata
        __table__ (Table): SQLAlchemy table object
        __table_args__ (Dict[str, Any]): SQLAlchemy table arguments
    """

    __depends_on__: Models = []
    __model_config__ = ModelConfig(materialized=MaterializationTypes.view)
    __table__: Table
    __table_args__: Dict[str, Any] = {"extend_existing": True}
    metadata = metadata

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:  # type: ignore
        """
        By default, `__tablename__` is the `snake_case` class name.

        ```python
        class MyModel(AmoraModel):
            ...


        assert MyModel.__tablename__ == "my_model"
        ```
        """
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

    @classmethod
    def dependencies(cls) -> Models:
        source = cls.source()
        if source is None:
            return []

        # todo: Remover necessidade de __depends_on__ inspecionando a query e chegando ao modelo de origem
        # tables: List[Table] = source.froms

        return cls.__depends_on__

    @classmethod
    def source(cls) -> Optional[Compilable]:
        """
        Called when `amora compile` is executed, Amora will build this model
        in your data warehouse by wrapping it in a `create view as` or `create table as` statement.

        Return `None` for defining models for tables/views that already exist on the data warehouse
        and shouldn't be managed by Amora.

        Return a `Compilable`, which is a sqlalchemy select statement, in order to compile the model with the given statement
        :return:
        """
        return None

    @classmethod
    def target_path(cls, model_file_path: Union[str, Path]) -> Path:
        # {settings.dbt_models_path}/a_model/a_model.py -> a_model/a_model.py
        strip_path = settings.MODELS_PATH.as_posix()
        relative_model_path = str(model_file_path).split(strip_path)[1][1:]
        # a_model/a_model.py -> ~/project/amora/target/a_model/a_model.sql
        target_file_path = settings.TARGET_PATH.joinpath(
            relative_model_path.replace(".py", ".sql")
        )

        return target_file_path

    @classmethod
    def model_file_path(cls) -> Path:
        return Path(getfile(cls))

    @classmethod
    @property
    def unique_name(cls) -> str:
        return str(cls.__table__)


def amora_model_for_path(path: Path) -> Model:
    spec = spec_from_file_location(".".join(["amoramodel", path.stem]), path)
    if spec is None:
        raise ValueError(f"Invalid path `{path}`. Not a valid Python file.")

    module = module_from_spec(spec)

    if spec.loader is None:
        raise ValueError(f"Invalid path `{path}`. Unable to load module.")

    try:
        spec.loader.exec_module(module)  # type: ignore
    except ImportError as e:
        raise ValueError(f"Invalid path `{path}`. Unable to load module.") from e
    is_amora_model = (
        lambda x: isinstance(x, CompilableProtocol)
        and inspect.isclass(x)
        and issubclass(x, AmoraModel)  # type: ignore
    )
    compilables = inspect.getmembers(
        module,
        is_amora_model,  # type: ignore
    )

    for _name, class_ in compilables:
        try:
            # fixme: Quando carregamos o código em inspect, não existe um arquivo associado,
            #  ou seja, ao iterar sobre as classes de um arquivo, a classe que retornar um TypeError,
            #  é uma classe definida no arquivo
            class_.model_file_path()
        except TypeError:
            return class_

    raise ValueError(f"Invalid path `{path}`")


def amora_model_for_target_path(path: Path) -> Model:
    model_path = model_path_for_target_path(path)
    return amora_model_for_path(model_path)


def list_models(
    path: Path = settings.MODELS_PATH,
) -> Iterable[Tuple[Model, Path]]:
    for model_file_path in list_files(path, suffix=".py"):
        try:
            yield amora_model_for_path(model_file_path), model_file_path
        except ValueError:
            logger.warning(
                "Unable to load amora model for path",
                extra={"model_file_path": model_file_path},
            )
            continue
