class ExecutionFlowMiddleWare(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed at preprocessing of request')
        response = self.get_response(request)
        print("this line printed at post processing of request")
        return response

#uncomment the middleware in settings.py to run above code

from django.http import HttpResponse

class AppMaintaineneceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        return HttpResponse('<h1> Application in maintenence.Please wait for 2 hours </h1>')


class ErroMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s='<h1> Currently we are facing some technical problems.Please try after some time </h1>'
        s2='<h2> Raised exception is {} </h2> '.format(exception.__class__.__name__)
        s3='<h2> Description/Message : {} </h2>'.format(exception)
        return HttpResponse(s+s2+s3)


class firstMiddleWare(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed at first middleware at pre processing of request')
        response = self.get_response(request)
        print("this line printed at first middleware post processing of request")
        return response


class secondMiddleWare(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed at second middleware at pre processing of request')
        response = self.get_response(request)
        print("this line printed at second middleware post processing of request")
        return response

class thirdMiddleWare(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed at third middleware at pre processing of request')
        response = self.get_response(request)
        print("this line printed at third middleware post processing of request")
        return response
