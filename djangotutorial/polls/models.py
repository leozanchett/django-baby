import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data publicacao") # data publicacao é o verbose_name, usado para exibir uma descrição mais amigável no admin do Django.

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now # Verifica se a data de publicação é recente, ou seja, se está dentro do intervalo de 1 dia até o momento atual.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text