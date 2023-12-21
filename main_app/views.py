from django.shortcuts import render
from .models import Violin
from django.views.generic.edit import CreateView
# violins = [
#   {'name': 'German violin', 'provenance': 'Bebenreuth', 'year': '1970', 'inventory_no': '7710','tone':'bright,clear,rich in overtones','length':'35.8 cm','price':'$3500'},
#   {'name': 'Antique violin from Saxony', 'provenance': 'Saxony', 'year': '1900', 'inventory_no': '2342','tone':'warm','length':'35.6 cm','price':'$4700'},
#   {'name': 'Old violin,Czech Republic', 'provenance': 'Bohemia', 'year': '1940', 'inventory_no': '1298','tone':'rich in overtones','length':'36.2 cm','price':'$2500'}
 
# ]
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


