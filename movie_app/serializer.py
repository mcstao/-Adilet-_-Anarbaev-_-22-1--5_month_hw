from rest_framework import serializers
from movie_app.models import Movie, Director, Review
from rest_framework.exceptions import ValidationError

class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    movie_id = serializers.CharField()

    stars = serializers.IntegerField(min_value=1,
                                     max_value=5,
                                     )
    class Meta:
        model = Review
        fields = ["id",

                  "movie_id",
                  "text",
                  "stars",
                  ]



class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Director
        fields = ['name',
                  'movie_count',
                  ]




class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    reviews = ReviewSerializer(default='',many=True)
    director_id = serializers.CharField()
    class Meta:

        model = Movie
        fields = ['duration',
                  'id',
                  'director_id',
                  'director',
                  'title',
                  'description',
                  'reviews',
                  'rating',
                  'created_date',
                  'modified_date'
                  ]

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3,max_length=100)
    description = serializers.CharField()
    director_id = serializers.IntegerField(min_value=1)
    duration = serializers.CharField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found!')
        return director_id

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3,max_length=100)

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3,max_length=500)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
