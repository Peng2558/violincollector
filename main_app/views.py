from django.shortcuts import render
from .models import Violin
from django.views.generic.edit import CreateView,UpdateView,DeleteView

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
    return render(request,'violins/detail.html',{
     'violin':violin
    })

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
