from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = "limit"
    offset_query_param = "offset"


class CategoryPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 1
    limit_query_param = "limit"
    offset_query_param = "offset"
