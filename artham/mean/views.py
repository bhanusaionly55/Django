from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def home(request):
    return render(request,'home.html')
def mean(request):
    dict = PyDictionary()
    val = request.POST['word']
    meaning = dict.meaning(val)
    return render(request,'result.html',{'text':meaning})