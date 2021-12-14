from django.db import models
import datetime


class Category(models.Model):
    cat_name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'


class Content(models.Model):
    content_index = models.IntegerField()
    content_img = models.ImageField(upload_to="blog/posts", blank=True)
    content_text = models.TextField(blank=True)

    def __str__(self):
        return 'Контент'

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.ManyToManyField(Content)
    photo = models.ImageField(upload_to="blog/posts")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return 'Пост'

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'




    def get_time(self):
        now = datetime.datetime.now()
        then = self.time_create

        duration = now.year - then.year
        if duration > 0:
            return str(duration) + " years ago"

        duration = now.month - then.month
        if duration > 0:
            if duration < 2:
                return "месяц назад"
            return str(duration) + " месяца назад"

        duration = now.day - then.day
        if duration > 0:
            if duration < 2:
                return str(duration) + " день назад"
            if 2 <= duration < 5:
                return str(duration) + " дня назад"
            return str(duration) + " дней назад"

        duration = now.hour - then.hour
        if duration < 2:
            return str(duration) + "час назад"
        if 2 <= duration < 5:
            return str(duration) + " часа назад"
        return str(duration) + " часов назад"