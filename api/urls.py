from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import TasksByUserIdView

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/by_user/<int:user_id>/', TasksByUserIdView.as_view(), name='tasks-by-user')
]