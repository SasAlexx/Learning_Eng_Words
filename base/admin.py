from django.contrib import admin
from base.models import Word  # This step makes your model available for management on admin page

# admin.site.register(Word)  # This we do for register a new model on Admin page

# This way you can change view of your model objects on admin page.(Also you can do it by __str__() in your model)
class WordAdmin(admin.ModelAdmin):
    list_display = ('eng_word', 'translate_word', 'date','score')


admin.site.register(Word, WordAdmin)
