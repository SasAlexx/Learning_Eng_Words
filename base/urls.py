from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('mywords/', views.words, name='mywords'),
    path('mywords/details/<int:id>/', views.details, name='details'),
    path('create_word/', views.createWord, name='create_word'),
    path('update-word/<int:id>/', views.updateWord, name='update-word'),
    path('delete-word/<int:id>/', views.deleteWord, name='delete-word'),
    path('choose-test/knowledge-test/<str:test>/', views.knowlegeTest, name='knowledge-test'),
    path('your-results/', views.results, name='your-results'),
    path('choose-test/', views.chooseTest, name='choose-test'),

]

