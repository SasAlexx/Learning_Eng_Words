from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .DRAFT1 import lis
from random import *

from base.forms import *
from base.models import *





def words(request):
    mywords = Word.objects.all().values()
    template = loader.get_template('base/mywords.html')
    context = {
        'mywords': mywords,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myword = Word.objects.get(id=id)
    template = loader.get_template('base/details.html')
    context = {
        'myword': myword,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('base/home.html')
    return HttpResponse(template.render())

def createWord(request):
    form = WordForm()
    saved_words = [word.eng_word.lower() for word in Word.objects.all()]
    print(saved_words)
    if request.method == 'POST':
        form = WordForm(request.POST)
        #Checking if word user want to add hasn't already been added in your db
        if form.is_valid() and request.POST['eng_word'].lower() not in saved_words:
        # if form.is_valid():
            Word.objects.create(**form.cleaned_data)
            return redirect('mywords')
        else:
            raise ValueError('This word has been already added')
    context = {'form': form}
    return render(request, 'base/word_form.html', context)

def updateWord(request, id):
    word = Word.objects.get(id=id)

    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('mywords')
    else:
        form = WordForm(instance=word)
    context = {'form': form}
    return render(request, 'base/word_form.html', context)

def deleteWord(request, id):
    word = Word.objects.get(id=id)

    if request.method == 'POST':
        word.delete()
        return redirect('mywords')
    return render(request, 'base/delete.html', {'obj': word})

def chooseTest(request):
    test = ('1', '2','3')
    all_words = len(Word.objects.all())

    context = {
        'test': test,
        'all_words': all_words
    }
    return render(request, 'base/choose_the_test.html', context)
    # return render(request, 'base/knowledge_test.html', context)
def knowlegeTest(request, test):
    #test in arguments must be the same with <str:test> in url
    print(test) #Test which user has chosen.

    results = {}
    num = len(Word.objects.all()) #Amount of all words
    word_answer = {word['eng_word']: word['translate_word'] for word in Word.objects.all().values()}
    answers = [word['translate_word'] for word in Word.objects.all().values()]
    word_choices = [(word, sample([word_answer[word]] + list(filter(lambda x: x != word_answer[word],
                    sample(answers, len(answers))))[:3], 4)) for word in word_answer]

    print(type(word_choices))
    if test == '1':
        word_choices = sample(word_choices, num)
    elif request.method == 'POST' and test == '2':
        num = int(request.POST['test'])
        word_choices = sample(word_choices, num)
    elif request.method == 'POST' and test == '3':
        if 'check' in request.POST:
            num = -int(request.POST['test'])
            word_choices = word_choices[:num-1:-1]
            print(word_choices)
        else:
            num = int(request.POST['test'])
            word_choices = word_choices[:num]
    print(num)

    #we take eng_word and translate_word from db and fill the rest with random translate words

    if request.method == 'POST':
        form = KnowledgeTestForm(request.POST, word_choices=word_choices)
        if form.is_valid():
            for word, _ in word_choices:
                selected_answer = form.cleaned_data[word]
                # print(f"Для слова '{word}' выбраны ответы: {selected_answer}")
                results[word] = selected_answer

    else:
        form = KnowledgeTestForm(word_choices=word_choices)
    context = {
        'form': form,
        'results': results,
    }

    return render(request, 'base/knowledge_test.html', context)

def results(request):
    word_answer = {word['eng_word']: word['translate_word'] for word in Word.objects.all().values()}
    # scores = {word['eng_word']: [word['translate_word'], word['score']] for word in Word.objects.all().values()}
    # print(word_answer)
    # print(scores)

    results_lis = []
    if request.method == 'POST':
        results = request.POST
        # from request.POST dictionary remove crsf-token and answer button to show only choosen words on result-page
        results = {key: results[key] for key in results if key not in ['csrfmiddlewaretoken', 'answer']}

        for key in results:
            if results[key] == word_answer[key]:
                #If user choose the correct answer, lis will get True value
                results_lis.append([key, results[key], True])
                # score = Word.objects.get(score=score)

                x = Word.objects.get(eng_word=key)
                if x.score < 10:
                    x.score += 1
                    x.save()
            else:
                results_lis.append([key, results[key], False])

    else:
        results = {}
    # scores = Word.objects.all().filter(eng_word__in=results)
    # print(scores)
    context = {
        'results':results,
        'results_lis':results_lis,
        'lis':[['qwewqe', 1],['asdf', 0]],
    }
    return render(request, 'base/result_page.html', context)


def testing(request):
    word_choices = [
        ('apple', ['яблоко', 'банан', 'груша']),
        ('dog', ['собака', 'кошка', 'крыса']),
        ('sun', ['солнце', 'луна', 'звезда']),
        ('frog', ['жаба', 'жопа', 'жук']),
    ]

    if request.method == 'POST':
        form = TestForm(request.POST, word_choices=word_choices)
        if form.is_valid():
            for word, _ in word_choices:
                selected_answers = form.cleaned_data[word]
                # Обработка выбранных ответов для каждого слова
                print(f"Для слова '{word}' выбраны ответы: {selected_answers}")

    else:
        form = TestForm(word_choices=word_choices)

    context = {
        'form': form,
    }
    return render(request, 'base/template.html', context)