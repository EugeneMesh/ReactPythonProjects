"""
high level support for doing this and that.
"""
from django.http import HttpResponse


# Create your views here.
def index(request):
    """my index functions which does nothing"""
    msg = "Hello World" + str(request.method)
    return HttpResponse(msg)
