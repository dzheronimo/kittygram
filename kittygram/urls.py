from django.urls import include, path

from cats.views import CatList, CatDetail

urlpatterns = [
   path('cats/', CatList.as_view(), name='api_cat'),
   path('cat_detail/<int:pk>/', CatDetail.as_view())
]


