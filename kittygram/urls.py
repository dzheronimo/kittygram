from django.urls import include, path

from cats.views import APICat, APICatDetail

urlpatterns = [
   path('cats/', APICat.as_view(), name='api_cat'),
   path('cat_detail/<int:pk>/', APICatDetail.as_view())
]


