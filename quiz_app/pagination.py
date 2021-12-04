from rest_framework.pagination import PageNumberPagination

class NewPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'sayfa'
