from django.shortcuts import render,redirect
from django.http import HttpResponse

def create_session(request):
    request.session['name']='cbit'
    request.session['password']='cbitsession'
    return HttpResponse("<h1>Session Demo App<br> the session is set</h1>")
def access_session(request):
    response="<h1>Welcome to Sessions Demo app</h1><br>"
    if request.session.get('name'):
        response+="Name:{0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response+="Password:{0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('/create')
def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>DataFlair<br>Session Data cleared</h1>")