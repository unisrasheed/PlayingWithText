# // I have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # dict = {'name': 'younis', 'place': 'Mars', 'age':19}
    return render(request, 'index.html')
    # return HttpResponse("<button>hello</button> application...") 

def about(request):
    return HttpResponse("<h1>about application...</h1>") 

# def capitilize(request):
#     capital=request.GET.get('capitilize', 'off')
#     djtext= request.GET.get('text', 'default')
#     print(capital)
#     if capitilize == "on":
#         capital=djtext.upper()
#         dic={'capitalll':capital}
#         return render(request, 'capitilize.html', dic)
#     else:
#         return HttpResponse("Error..")    
#     # return HttpResponse("capitilize first")    

# def spaceremover(request):
#     # print(request.GET.get('text', 'default'))
#     return HttpResponse("<a href='http://127.0.0.1:8000/newlineremover''><button>Back</button></a>space remover")  

# def newlineremover(request):
#     return HttpResponse("new line remover")  

def analyze(request):
    # get the text
    djtext= request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitilize=request.GET.get('capitilize', 'off')
    newliner= request.GET.get('newliner', 'off')
    extraspaceremover=request.GET.get('extraspaceremover', "off")

    print(removepunc)
    print(djtext)
    #  analyse the text
    punctuations='''()[],./<>?()-@#!$%^%&*"";:'''
    analyzed=""
    if removepunc =="on":

        for a in djtext:
            if a not in punctuations:
                analyzed = analyzed + a
    # purpose=analyzed
        params={'name':'removed punctuation', 'purpose':analyzed}        
        return render(request, 'analyze.html', params)
    elif(capitilize == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params={'name':'change to uppercase', 'purpose':analyzed}        
        return render(request, 'analyze.html', params)
    
    elif(newliner=="on"):
        analyzed=""
        for char in djtext:
            if char != '\n':
                analyzed=analyzed+char 
        params={'name':'newline removed', 'purpose':analyzed}        
        return render(request, 'analyze.html', params)   

    elif(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " " :
                pass
            else:
                analyzed=analyzed+char    
            
        params={'name':'Extra Space Removed', 'purpose':analyzed}        
        return render(request, 'analyze.html', params)   

    else:
        return HttpResponse("eroorr..")    

    
           


\












# def charcount(request):
#     return HttpResponse("char counter")      