from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    rc = RequestContext(request)
    return render_to_response('index.html', {'header': 'Djumpstarting Development'}, rc)
