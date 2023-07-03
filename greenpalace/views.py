from django.shortcuts import render,redirect
from item.models import Category,Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'greenpalace/index.html', 
                  {'categories': categories, 
                  'items': items})

def contact(request):
    return render(request, 'greenpalace/contact.html')

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        return redirect('/login/')
    else:
        form=SignupForm()

    return render(request, 'greenpalace/signup.html',{
        'form': form
    } )