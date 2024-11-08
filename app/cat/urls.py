from django.urls import path
from .views import CatView, CatDetailView

app_name = 'cat'

urlpatterns = [
    path('cats/', CatView.as_view(), name='create_cat'),
    path('cat/<int:pk>/', CatDetailView.as_view(), name='detail_cat')
]