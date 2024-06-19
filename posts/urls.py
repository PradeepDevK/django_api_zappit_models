from django.urls import path
from  posts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/vote/', views.VoteCreateView.as_view(), name='vote_list'),
]
