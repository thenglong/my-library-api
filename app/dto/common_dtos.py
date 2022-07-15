import math
from typing import Generic, TypeVar, List

from humps.main import camelize
from pydantic import BaseModel
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class CamelModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class CamelGenericModal(GenericModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class Pagination(CamelGenericModal, Generic[DataT]):
    page: int
    item_count: int
    page_count: int
    take: int
    has_next: bool
    has_previous: bool
    items: List[DataT]


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
