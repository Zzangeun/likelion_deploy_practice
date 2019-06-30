from django.db import models
from django.utils import timezone

class Review(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        a =[]
        a.append(self.title)

        if len(a[-1])>6:
            return self.title[:6]+'...'
        else:
            return self.title

class Comment(models.Model):
    review = models.ForeignKey('review.Review', related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text