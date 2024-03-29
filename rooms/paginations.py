from rest_framework import pagination


class SimpleResultSetPagination(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = "page_size"
    max_page_size = 60
