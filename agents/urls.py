from django.urls import path

from . import views

app_name = 'agents'

urlpatterns = [
    path('', views.AgentListView.as_view(), name='agent-list'),
    path('create/', views.AgentCreateView.as_view(), name='agent-create'),
    path('<pk>/update/', views.AgentUpdateView.as_view(), name='agent-update'),
    path('<pk>/detail/', views.AgentDetailView.as_view(), name='agent-detail'),
    path('<pk>/delete/', views.AgentDeleteView.as_view(), name='agent-delete'),
]
