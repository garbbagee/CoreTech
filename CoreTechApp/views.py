from django.shortcuts import render

def index(request):
    return render(request, 'html/index.html')

def acercade(request):
    return render(request, 'html/acercade.html')

def carrocompras(request):
    return render(request, 'html/carrocompras.html')

def cuenta(request):
    return render(request, 'html/cuenta.html')

def gama_alta(request):
    return render(request, 'html/GamaAlta.html')

def gama_media(request):
    return render(request, 'html/GamaMedia.html')

def gama_baja(request):
    return render(request, 'html/GamaBaja.html')

# Agregar las vistas para los otros archivos HTML
def torrega1(request):
    return render(request, 'html/torrega1.html')

def torrega2(request):
    return render(request, 'html/torrega2.html')

def torrega3(request):
    return render(request, 'html/torrega3.html')

def torrega4(request):
    return render(request, 'html/torrega4.html')

def torregb1(request):
    return render(request, 'html/torregb1.html')

def torregb2(request):
    return render(request, 'html/torregb2.html')

def torregb3(request):
    return render(request, 'html/torregb3.html')

def torregb4(request):
    return render(request, 'html/torregb4.html')

def torregm1(request):
    return render(request, 'html/torregm1.html')

def torregm2(request):
    return render(request, 'html/torregm2.html')

def torregm3(request):
    return render(request, 'html/torregm3.html')

def torregm4(request):
    return render(request, 'html/torregm4.html')
