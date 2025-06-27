from django.urls import path
from . import views
urlpatterns=[
    path("getUsers/", views.getUsers),
    path("updateAndDelete/<int:id>/", views.updateAndDelete),
    path('UserGetAndPOST/', views.UserGetAndPOST.as_view()),
    path('UserGETAndPUTAndDelete/<int:pk>/', views.UserGETAndPUTAndDelete.as_view()),
    path('TodoGetAndPutAndDelete/<int:pk>/', views.TodoGetAndPutAndDelete.as_view()),
    path('TodoCreateAndRetrieve/', views.TodoCreateAndRetrieve.as_view()),
]