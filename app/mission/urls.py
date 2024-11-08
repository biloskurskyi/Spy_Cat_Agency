from django.urls import path

from .views import (GoalUpdateView, MissionCreateView, MissionDeleteView,
                    MissionGetById, MissionsGet, MissionUpdateView)

app_name = 'mission'

urlpatterns = [
    path('missions/', MissionCreateView.as_view(), name='create_mission'),
    path('mission/<int:pk>/delete/', MissionDeleteView.as_view(), name='delete_mission'),
    path('mission/<int:pk>/update/', MissionUpdateView.as_view(), name='update_mission'),
    path('goal/<int:pk>/update/', GoalUpdateView.as_view(), name='update_goal'),
    path('missions/get-all/', MissionsGet.as_view(), name='get_missions'),
    path('mission/<int:pk>/get/', MissionGetById.as_view(), name='get_mission'),
]
