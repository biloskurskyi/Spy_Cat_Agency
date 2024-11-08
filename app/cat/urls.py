from django.urls import path

from .views import CatDetailView, CatView

app_name = 'cat'

urlpatterns = [
    path('cat/', CatView.as_view(), name='create_cat'),
    path('cat/<int:pk>/', CatDetailView.as_view(), name='detail_cat')
]
