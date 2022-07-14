from typing import Generic, TypeVar, List
import math

from pydantic import Field
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class Pagination(GenericModel, Generic[DataT]):
    page: int
    item_count: int = Field(..., alias="itemCount")
    page_count: int = Field(..., alias="pageCount")
    take: int
    has_next: bool = Field(..., alias="hasNext")
    has_previous: bool = Field(..., alias="hasPrevious")
    items: List[DataT]

    class Config:
        allow_population_by_field_name = True


def create_pagination(items,
                      page: int,
                      take: int,
                      all_items_count: int):
    page_count = math.ceil(all_items_count / take)
    return Pagination(
        page=page,
        items=items,
        page_count=page_count,
        item_count=all_items_count,
        take=take,
        has_next=page < page_count,
        has_previous=page > 1
    )
