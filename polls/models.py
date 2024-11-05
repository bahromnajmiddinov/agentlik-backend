from django.db import models

from core.models import TimeStamps


class Poll(TimeStamps):
    question = models.CharField(max_length=250)

    def __str__(self):
        choices_count = len([i for i in self.choices.all()])

        return f'{self.question} | {choices_count}'


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    answer = models.TextField()
    clicks = models.PositiveIntegerField(default=0)
