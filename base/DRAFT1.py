from .models import Word

# lis = [[1,'Привіт'], (2, 'Бувай')]
lis = [[word.id, word.translate_word] for word in Word.objects.all()]
# lis = Word.objects.all()

