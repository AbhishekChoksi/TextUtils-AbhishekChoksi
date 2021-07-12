# I have created this file - Abhishek Choksi
from django.http import HttpResponse
from django.shortcuts import render


# Code for video: 6
# def index(request):
#     return HttpResponse('''<h1>Hello Abhishek</h1> <a href="https://youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Python Django Tutorials In Hindi By CodeWithHarry</a>''')
#
# def about(request):
#     return HttpResponse("About Abhishek")

# Code for video: 7
# def index(request):
#     return HttpResponse("Home")
#
# def removepunc(request):
#     return  HttpResponse("remove punc <a href='/'>Back</a>")
#
# def capfirst(request):
#     return  HttpResponse("capitalize first <a href='/'>Back</a>")
#
# def newlineremove(request):
#     return  HttpResponse("new line remove <a href='/'>Back</a>")
#
# def spaceremove(request):
#     return  HttpResponse("space remover <a href='/'>Back</a>")
#
# def charcount(request):
#     return  HttpResponse("char count")

# Code for video: 8
# def index(request):
#     params = {'name': 'Abhishek Choksi', 'place': 'Surat'}
#     return render(request, 'index.html', params)
#
# def removepunc(request):
#     return  HttpResponse("remove punc <a href='/'>Back</a>")
#
# def capfirst(request):
#     return  HttpResponse("capitalize first <a href='/'>Back</a>")
#
# def newlineremove(request):
#     return  HttpResponse("new line remove <a href='/'>Back</a>")
#
# def spaceremove(request):
#     return  HttpResponse("space remover <a href='/'>Back</a>")
#
# def charcount(request):
#     return  HttpResponse("char count")

# Code for video: 9
# def index(request):
#     return render(request, 'index.html')
#
#
# def removepunc(request):
#     # print(request.GET.get('text', 'default'))
#     # return HttpResponse(request.GET.get('text', 'default'))
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first <a href='/'>Back</a>")
#
#
# def newlineremove(request):
#     return HttpResponse("new line remove <a href='/'>Back</a>")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>Back</a>")
#
#
# def charcount(request):
#     return HttpResponse("char count")

# Code for video: 12
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}

        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on":
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)