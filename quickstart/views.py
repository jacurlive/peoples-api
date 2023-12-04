from rest_framework import generics
from .models import Peoples, Category
from .serializers import PeopleSerializer, CategorySerializer


class PeopleAPIList(generics.ListCreateAPIView):
    queryset = Peoples.objects.filter(is_published=True)
    serializer_class = PeopleSerializer


class PeopleAPIUpdate(generics.UpdateAPIView):
    queryset = Peoples.objects.filter(is_published=True)
    serializer_class = PeopleSerializer


class PeopleAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Peoples.objects.filter(is_published=True)
    serializer_class = PeopleSerializer


class CategoryPeoplesAPIView(generics.ListAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                return Peoples.objects.filter(is_published=True, cat=category)
            except Category.DoesNotExist:
                return Peoples.objects.none() 
    

class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
