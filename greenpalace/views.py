from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'greenpalace/index.html')

def contact(request):
    return render(request, 'greenpalace/contact.html')