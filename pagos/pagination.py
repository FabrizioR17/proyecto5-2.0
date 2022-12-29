from rest_framework.pagination import PageNumberPagination

class Pagination_payments(PageNumberPagination):
  page_size= 100
  page_query_param = 'page_size'
  #max_page_size = 5