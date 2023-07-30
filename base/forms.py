from django import forms
from django.forms import ModelForm
from .models import Word
from random import *
# from .views import lis

import base.views
# WORD_CHOICES = [word['eng_word'] for word in Word.objects.all().values()]
# WORD_CHOICE = [[word.id, word.translate_word] for word in test_words]


# WORD_CHOICE = lis
# WORD_CHOICE = [[1,'Привіт'], (2, 'Бувай')]
class WordForm(ModelForm):
    class Meta:
        model = Word
        # fields = '__all__'
        fields = ['eng_word','translate_word']


class KnowledgeTestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        word_choices = kwargs.pop('word_choices', [])
        super(KnowledgeTestForm, self).__init__(*args, **kwargs)

        for word, answer_choices in word_choices:
            self.fields[word] = forms.ChoiceField(
                choices=[(choice, choice) for choice in answer_choices],
                widget=forms.RadioSelect,

            )

class ChooseTest(forms.Form):
    tests = ['Test for all words']
    tests_list = forms.ChoiceField(choices=[(choice, choice) for choice in tests],widget=forms.RadioSelect)


class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        word_choices = kwargs.pop('word_choices', [])
        super(TestForm, self).__init__(*args, **kwargs)

        for word, answer_choices in word_choices:
            self.fields[word] = forms.ChoiceField(
                choices=[(choice, choice) for choice in answer_choices],
                widget=forms.RadioSelect
            )