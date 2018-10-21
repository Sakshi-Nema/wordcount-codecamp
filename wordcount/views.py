from django.http import HttpResponse
def homepage(request):
    return render(request,'home.html')
def eggs(request):
    return HttpResponse('<h1>eggs</h1>')
from django.shortcuts import render
def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    no_is = wordList.count("is")
    old = request.GET['old']
    new = request.GET['new']
    newstring = fulltext.replace(old,new)
    return render(request,'count.html',{'fulltext' :fulltext,'count':len(wordList),'num_is':no_is,'newstring':newstring})
