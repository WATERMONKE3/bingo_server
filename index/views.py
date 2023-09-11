from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'lp.html')

def raffle(request):
    return render(request, 'raffle.html')