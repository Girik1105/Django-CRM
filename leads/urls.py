from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('all/', views.LeadsListView.as_view(), name='lead-list'),

    path('Create/', views.CreateLeadView.as_view(), name='lead-create'),
    path('<pk>/update/', views.UpdateLeadView.as_view(), name='lead-update'),
    path('<pk>/delete/', views.DeleteLeadView.as_view(), name='lead-delete'),

    path('<pk>/details/', views.DetailLeadView.as_view(), name='lead-detail'),


    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<pk>/details', views.CategoryDetailView.as_view(), name="category-detail"),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]
