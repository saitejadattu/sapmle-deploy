from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns=[
    path('TodoGetAndPutAndDelete/<int:pk>/', views.TodoGetAndPutAndDelete.as_view()),
    path('TodoCreateAndRetrieve/', views.TodoCreateAndRetrieve.as_view()),
    path("logout/", views.logout_view, name="logout_view"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('register/', views.register),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_user_todos/<int:user_id>/', views.getUserTodos),
]