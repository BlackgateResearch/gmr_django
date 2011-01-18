from django.template import Context, RequestContext, loader
from django.http import HttpResponse

def index(request):
    c = RequestContext(request) 
    t = loader.get_template('index.html')
    return HttpResponse(t.render(c))