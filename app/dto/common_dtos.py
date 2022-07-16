from typing import Generic, TypeVar, List, Union

from fastapi import Query
from pydantic import BaseModel
from pydantic.generics import GenericModel

from app.helpers.string import to_camelcase

DataT = TypeVar('DataT')


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camelcase
        allow_population_by_field_name = True


class CamelGenericModal(GenericModel):
    class Config:
        alias_generator = to_camelcase
        allow_population_by_field_name = True


class Pagination(CamelGenericModal, Generic[DataT]):
    page: int
    item_count: int
    page_count: int
    take: int
    has_next: bool
    has_previous: bool
    items: List[DataT]


class PaginateQueryParams:
    def __init__(self,
                 page: int = Query(default=1, ge=1),
                 take: int = Query(default=20, ge=1)):
        self.page = page
        self.take = take


class PaginateWithSearchQueryParams(PaginateQueryParams):
    def __init__(self, query: Union[str, None] = None,
                 page: int = Query(default=1, ge=1),
                 take: int = Query(default=20, ge=1)):
        super().__init__(page, take)
        self.query = query

    def get_search_query(self):
        if self.query is not None and self.query != "":
            return "%{}%".format(self.query)
        return None

    def get_offset(self):
        return (self.page - 1) * self.take
