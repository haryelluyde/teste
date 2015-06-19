import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField('Questão',max_length=200)
    pub_date = models.DateTimeField('data de publicação')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publicado recentemente?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField('Alternativa',max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text