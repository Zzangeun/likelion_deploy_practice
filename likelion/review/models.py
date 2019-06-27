from django.db import models
from django.utils import timezone

class Review(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)

    # short_title=list(title)

    # if len(title)>6 :
    #     short_title = title[0:6] + "..."
    # else :
    #     short_title = title

    def __str__(self):
        return self.short_title

class Comment(models.Model):
    review = models.ForeignKey('review.Review', related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text