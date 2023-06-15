from django.urls import path
from todoapp.models import Todo
from todoapp.views import taskdetails,todopage

urlpatterns = [
   
   path('todopage/<str:pk>/', taskdetails.as_view()),
   path('todopage/',todopage.as_view())
   ]