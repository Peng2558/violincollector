from django.shortcuts import render, redirect
from .models import Violin , Accessory
from .forms import TuneupForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

@login_required
def violins_index(request):
    violins=Violin.objects.all()
    return render(request, 'violins/index.html',{
    'violins': violins

})

@login_required
def violins_detail(request, violin_id):
    violin = Violin.objects.get(id=violin_id)
    id_list = violin.accessories.all().values_list('id')
    accessories_violin_doesnt_have= Accessory.objects.exclude(id__in=id_list)
    tuneup_form=TuneupForm()
    return render(request,'violins/detail.html',{
      'violin':violin,'tuneup_form':tuneup_form,
      'accessories': accessories_violin_doesnt_have
    })


@login_required
def add_tuneup(request, violin_id):
  form = TuneupForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_tuneup = form.save(commit=False)
    new_tuneup.violin_id = violin_id
    new_tuneup.save()
  return redirect('detail', violin_id=violin_id)


class ViolinCreate(CreateView):
  model = Violin
  fields = ['name','provenance','year','inventory_no','tone','length','price']
#   success_url = '/violins' in it's here will be override the detail page

class ViolinUpdate(UpdateView):
  model = Violin
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'


class ViolinDelete(DeleteView):
  model = Violin
  success_url = '/violins'


class AccessoryList(ListView):
   model= Accessory

class AccessoryDetail(DetailView):
   model = Accessory  

class AccessoryCreate(CreateView):
   model= Accessory
   fields = '__all__'

class AccessoryUpdate(UpdateView):
   model= Accessory
   fields = ['name', 'color']

class AccessoryDelete(DeleteView):
   model= Accessory
   success_url = '/accessories'

@login_required
def assoc_accessory(request, violin_id, accessory_id):
  Violin.objects.get(id=violin_id).accessories.add(accessory_id)
  return redirect('detail', violin_id=violin_id)

@login_required
def unassoc_accessory(request,violin_id,accessory_id):
    Violin.objects.get(id=violin_id).accessories.remove(accessory_id)
    return redirect('detail', violin_id=violin_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



                        