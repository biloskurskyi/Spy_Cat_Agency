from django.urls import path

from .views import MissionCreateView, MissionDeleteView

app_name = 'mission'

urlpatterns = [
    path('missions/', MissionCreateView.as_view(), name='create_mission'),
    path('missions/<int:pk>/delete/', MissionDeleteView.as_view(), name='delete_mission'),
]
