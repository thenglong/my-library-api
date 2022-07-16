import math

from app.dto.common_dtos import Pagination, PaginateQueryParams


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


def create_pagination_from_paginate_params(items, paginate: PaginateQueryParams, all_items_count: int):
    return create_pagination(items, page=paginate.page, take=paginate.take, all_items_count=all_items_count)
