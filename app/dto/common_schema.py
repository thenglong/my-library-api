from typing import Generic, TypeVar, List

from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class Pagination(GenericModel, Generic[DataT]):
    page: int
    itemCount: int
    pageCount: int
    taken: int
    hasNext: bool
    hasPrevious: bool
    items: List[DataT]
