from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import Cat
from .serializers import CatSerializer


class CatList(ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
