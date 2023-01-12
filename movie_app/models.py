from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=50,verbose_name='Имя режиссера')


    def __str__(self):
        return self.name


    @property
    def movie_count(self):
        return self.movies.all().count()



class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE,
                                 null=True,related_name='movies')
    title = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    duration = models.CharField(max_length=20,verbose_name='Продолжительность')
    created_date = models.DateTimeField(auto_now=True,verbose_name='Дата создания')
    modified_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата изменения')

    def __str__(self):
        return self.title


    @property
    def rating(self):
        total_amount = self.reviews.all().count()
        if total_amount == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amount




class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,
                              related_name='reviews',verbose_name='Фильм')
    stars = models.IntegerField(default=0,verbose_name='Рейтинг')

    def __str__(self):
        return self.text





