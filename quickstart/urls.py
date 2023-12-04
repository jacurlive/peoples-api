from django.urls import path
from .views import CategoryAPIView, PeopleAPIList, PeopleAPIUpdate, PeopleAPIDetail, CategoryPeoplesAPIView


urlpatterns = [
    path('api/v1/peoples/', PeopleAPIList.as_view()),
    path('api/v1/category/', CategoryAPIView.as_view()),
    path('api/v1/peoples/<int:pk>/', PeopleAPIUpdate.as_view()),
    path('api/v1/peoplesdetail/<int:pk>/', PeopleAPIDetail.as_view()),
    path('api/v1/category/<int:pk>/', CategoryPeoplesAPIView.as_view())
]
