from django.db import models


class Word(models.Model):
    eng_word = models.CharField(max_length=50, blank=False)
    translate_word = models.CharField(max_length=200, blank=False)

    date = models.DateField(auto_now=True)
    score = models.IntegerField(default=0)
    objects = models.Manager

    def __str__(self):
        return f'{self.eng_word} : {self.translate_word} '  # it makes model objects reader-friendly on admin page

