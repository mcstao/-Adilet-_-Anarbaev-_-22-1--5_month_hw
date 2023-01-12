from django.urls import path
from movie_app.views import (
    MovieListCreateApiView, MovieItemUpdateDeleteApiView,DirectorListCreateApiView,DirectorItemUpdateDeleteApiView,
    ReviewModelViewSet
)

urlpatterns = [
    path('', MovieListCreateApiView.as_view()),
    path('<int:pk>/', MovieItemUpdateDeleteApiView.as_view()),
    path('directors/', DirectorListCreateApiView.as_view() ),
    path('directors/<int:pk>/', DirectorItemUpdateDeleteApiView.as_view()),
    path('reviews/', ReviewModelViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('reviews/<int:pk>/', ReviewModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
]