from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import DemonSlayer, something, ContactUsNow
from .forms import AddDemonSlayer, ContactForm
from .serialisers import SlayerSerializer
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, "test.html")

def contact(request):
    submitted=False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact') + '?submitted=True')
    else:
        form = ContactForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, "contact.html", {'form': form, 'submitted': submitted})


def blog(request):
     return render(request, "blog.html", {})

def about(request):
     return render(request, "about.html", {})
# Elements include first_name, last_name, age, category, element_type
def index(request, first_name):
    ls = DemonSlayer.objects.get(first_name=first_name)
    return render(request, "charcter.html", {"person": f"{ls.first_name},{ls.last_name}",
                                             "age": ls.age,
                                             "category": ls.category,
                                             "element": ls.element_type})

def human(request):
     human_slayers = DemonSlayer.objects.filter(category="Human")
     return render(request, "categories/human.html", {'human_slayers': human_slayers,
                                                      "page title": "Humans"})

def demon(request):
     demons = DemonSlayer.objects.filter(category="Demon")
     return render(request, "categories/demons.html", {'demons': demons})


def submit_slayer(request):
    submitted = False
    if request.method == "POST":
        form = AddDemonSlayer(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submit_slayer') + '?submitted=True')
    else:
        form = AddDemonSlayer
    if 'submitted' in request.GET:
            submitted = True
    return render(request, "submit_slayer.html", {'form':form, 'submitted': submitted})

def slayer_list(request):
     slayer = DemonSlayer.objects.all()
     serializer = SlayerSerializer(slayer, many=True)
     return JsonResponse(serializer.data, safe=False)
