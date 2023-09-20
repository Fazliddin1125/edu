from django.urls import path
from .views import HomePageView, TeachersView
urlpatterns = [
    path("", HomePageView.as_view(), name='index'),
    path("teachers/<int:id>/", TeachersView.as_view(), name='teachers')
]

