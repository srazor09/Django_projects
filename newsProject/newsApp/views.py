from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'newsAppHtmls/index.html')

def moviesinfo(request):
    head_msg='Sourabh latest movie info'
    msg1='The falcon and winter soldier'
    msg2='Wandavision'
    msg3='Modi is going to act in movie'
    my_dict={'HM':head_msg,'M1':msg1,'M2':msg2,'M3':msg3}
    return render(request, 'newsAppHtmls/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Sourabh latest movie info'
    msg1='The falcon and winter soldier'
    msg2='Wandavision'
    msg3='Modi is going to act in movie'
    my_dict={'HM':head_msg,'M1':msg1,'M2':msg2,'M3':msg3}
    return render(request, 'newsAppHtmls/news.html',context=my_dict)

def politicsinfo(request):
    head_msg='Sourabh latest movie info'
    msg1='The falcon and winter soldier'
    msg2='Wandavision'
    msg3='Modi is going to act in movie'
    my_dict={'HM':head_msg,'M1':msg1,'M2':msg2,'M3':msg3}
    return render(request, 'newsAppHtmls/news.html',context=my_dict)
