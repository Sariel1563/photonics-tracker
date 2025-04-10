from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExperimentListView.as_view(), name='experiment-list'),
    path('experiment/<int:pk>/', views.ExperimentDetailView.as_view(), name='experiment-detail'),
    path('experiment/new/', views.ExperimentCreateView.as_view(), name='experiment-create'),
]