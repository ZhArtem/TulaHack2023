from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок публикации", )
    content = models.TextField(blank=True, verbose_name="Текст публикации")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_moderated = models.BooleanField(default=False, verbose_name="Прошло модерацию")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории публикации") # например публикация с фото или новость 
    theme = models.ForeignKey('Theme', on_delete=models.PROTECT, verbose_name="Тема")

    def __str__(self):
        return self.title
    
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug}) 

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=32, verbose_name="Город")

    class Meta:
        verbose_name = 'Автор публикации'
        verbose_name_plural = 'Авторы публикации'
        ordering = ['id']


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст комментария")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания комментария")

    def __str__(self):
        return self.commentUser.username

    class Meta:
        verbose_name = 'Комметарий'
        verbose_name_plural = 'Комметарии'
        ordering = ['id']


class Theme(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название темы")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_slug': self.slug}) 

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['id']