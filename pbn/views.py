from django.shortcuts import get_object_or_404,render_to_response, redirect

# Create your views here.
def index(request):

    mensaje = "Hola Mundo, Esto es el nacimiento de pubnuk.com"
    return render_to_response('main/index.html',
                                    {'mensaje':mensaje})

