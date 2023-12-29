from django.shortcuts import render, redirect
from .models import Violin , Accessory
from .forms import TuneupForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def violins_index(request):
    violins=Violin.objects.all()
    return render(request, 'violins/index.html',{
    'violins': violins

})

def violins_detail(request, violin_id):
    violin = Violin.objects.get(id=violin_id)
    id_list = violin.accessories.all().values_list('id')
    accessories_violin_doesnt_have= Accessory.objects.exclude(id__in=id_list)
    tuneup_form=TuneupForm()
    return render(request,'violins/detail.html',{
      'violin':violin,'tuneup_form':tuneup_form,
      ' accessories': accessories_violin_doesnt_have
    })

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
  fields = '__all__'
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
    
                        