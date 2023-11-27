from django.urls import path
from .views import PeopleAPIView, CategoryAPIView


urlpatterns = [
    path('api/v1/peoples', PeopleAPIView.as_view()),
    path('api/v1/category', CategoryAPIView.as_view()),
    path('api/v1/peoples/<int:pk>', PeopleAPIView.as_view())
]
