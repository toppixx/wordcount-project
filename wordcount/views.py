from django.http import HttpResponse
from django.shortcuts import render
import json
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
    #aboutButton = request.GET['aboutButton']
    #if aboutButton == 'submit':
    #    return render(request, 'about.html')
    #body_unicode = request.body.decode('utf-8')
    #body_data = json.loads(body_unicode)
    itemGet = request.GET
    print(itemGet)
    if  request.GET.get('textBox') is not None:
        textBox = request.GET['textBox']
        wordlist = textBox.split()
        wordDictionary = {}
        for word in wordlist:
            if word in wordDictionary:
                #increase counter in wordDictionary
                wordDictionary[word] += 1
            else:
                #add to wordDictionary
                wordDictionary[word] = 1

        sortedwordDictionary = sorted(wordDictionary.items(), key=operator.itemgetter(1),reverse=True)
        return render(request,'count.html', {'textBox':textBox, 'count':len(wordlist),'sortedwordDictionary':sortedwordDictionary})

    if request.GET.get('aboutButton') is not None:
        return render(request,'about.html')

    return render(request,'error.html')


def about(request):
    aboutButton = request.GET['aboutButton']
    if aboutButton == 'submit':
        return render(request, 'about.html')
