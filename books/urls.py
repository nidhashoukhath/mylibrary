from django.urls import path
from .views import index, details, create, update, delete

urlpatterns = [
    path('', index),
    path('create/', create),
    path('<int:id>/', details),
    path('<int:id>/update/', update),
    path('<int:id>/delete/', delete)


]