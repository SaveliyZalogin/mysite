from django.db import models


class KeyWords(models.Model):
    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.keyword}'


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    annotation = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to="static/images", blank=True)
    key_word = models.ManyToManyField(KeyWords, blank=True)

    def __str__(self):
        return f'{self.id} {self.title}'
