from rest_framework.response import Response
from movie_app.models import Movie, Director, Review
from rest_framework.decorators import api_view
from movie_app.serializer import MovieSerializer,DirectorSerializer, ReviewSerializer,MovieValidateSerializer
from movie_app.serializer import DirectorValidateSerializer, ReviewValidateSerializer
from rest_framework import status
from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class DirectorListCreateApiView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination

class DirectorItemUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


class MovieListCreateApiView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination


class MovieItemUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# class MovieModelViewSet(ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     pagination_class = PageNumberPagination

# @api_view(['GET','POST'])
# def movies_view(request):
#     print(request.user)
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors':serializer.errors},
#                             status=status.HTTP_400_BAD_REQUEST)
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         director_id = serializer.validated_data.get('director_id')
#         duration = serializer.validated_data.get('duration')
#         movie = Movie.objects.create(title=title, description=description, director_id=director_id,duration=duration)
#         movie.save()
#         return Response(data={'message': 'data recievid!',
#                               'movie':MovieSerializer(movie).data})


# @api_view(['GET','PUT','DELETE'])
# def movie_detail_view(request,**kwargs):
#     try:
#         movie = Movie.objects.get(id=kwargs['id'])
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'message':'Post not found!'})
#     if request.method == 'GET':
#
#         serializer = MovieSerializer(movie, many=False)
#         return Response (data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = serializer.validated_data.get('title')
#         movie.description = serializer.validated_data.get('description')
#         movie.director_id = serializer.validated_data.get('director_id')
#         movie.duration = serializer.validated_data.get('duration')
#         movie.save()
#         return Response(data={'message': 'data recievid!',
#                               'movie':MovieSerializer(movie).data})


# @api_view(['GET','POST'])
# def directors_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         name = request.data.get('name')
#         director = Director.objects.create(name= name)
#         director.save()
#         return Response(data={'message': 'data recievid!',
#                               'director':DirectorSerializer(director).data})

# @api_view(['GET','PUT','DELETE'])
# def director_detail_view(request,**kwargs):
#     try:
#         director = Director.objects.get(id=kwargs['id'])
#
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'message':'Post not found!'})
#     if request.method == 'GET':
#
#         serializer = DirectorSerializer(director, many=False)
#         return Response (data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director.name = request.data.get('name')
#         director.save()
#         return Response(data={'message': 'data recievid!',
#                               'director': DirectorSerializer(director).data})

# @api_view(['GET','POST'])
# def reviews_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = request.data.get('text')
#         movie_id = request.data.get('movie_id')
#         stars = request.data.get('stars')
#         review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
#         review.save()
#         return Response(data={'message': 'data recievid!',
#                               'review': ReviewSerializer(review).data})

# @api_view(['GET','PUT','DELETE'])
# def review_detail_view(request,**kwargs):
#     try:
#         review = Review.objects.get(id=kwargs['id'])
#
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'message':'Post not found!'})
#     if request.method == 'GET':
#
#         serializer = ReviewSerializer(review, many=False)
#         return Response (data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = request.data.get('text')
#         review.movie_id = request.data.get('movie_id')
#         review.stars = request.data.get('stars')
#         review.save()
#         return Response(data={'message': 'data recievid!',
#                               'review': ReviewSerializer(review).data})