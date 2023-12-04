from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
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


# class PeopleAPIView(APIView):
#     def get(self, request):
#         objects = Peoples.objects.filter(is_published=True)
#         return Response({'peoples': PeopleSerializer(objects, many=True).data})
    
#     def post(self, request):

#         data = request.data.copy()

#         if 'nickname' not in data:
#             data['nickname'] = None

#         serializer = PeopleSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()


#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):

#         data = request.data.copy()

#         if 'nickname' not in data:
#             data['nickname'] = None

#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Peoples.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         serializer = PeopleSerializer(data=data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"post": serializer.data})
    

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
    

class CategoryAPIView(APIView):
    def get(self, request):
        objects = Category.objects.all()
        return Response({'categories': CategorySerializer(objects, many=True).data})
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'category': serializer.data})
