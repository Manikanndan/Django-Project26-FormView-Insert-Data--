from django.shortcuts import render
from django.http import HttpResponse
from app.form import *
from app.models import *
from django.views.generic import View,TemplateView,FormView,ListView
# Create your views here.

# returning string as response by using FBV

def fbv_string(request):
    return HttpResponse('This is FBV String')

class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>This is class based view</h1>')

# returning Html Page as response by using FBV
def fbv_html(request):
    return render(request,'fbv.html')

# returning Html Page as response by using Class BV

class Cbv_html(View):
    def get(self,request):
        return render(request,'cbv.html')

# dealing with forms in FBV

def fbv_form(request):
    if request.method=='POST':
        username=request.POST['name']
        age=request.POST['age']
        return HttpResponse(f'name is {username} and age is {age}')
    return render(request,'fbv_form.html')

# dealing with forms in Class BV

class cbv_form(View):
    def get(self,request):
        return render(request,'cbv_form.html')

    def post(self,request):
        username=request.POST['name']
        age=request.POST['age']
        return HttpResponse(f'name is {username} and age is {age}')

#template view class
class Cbv_TemplateView(TemplateView):
    template_name='template1.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=NameForm()
        return context
    
    def post(self,request):
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

class Cbv_FormView(FormView):
    template_name='template2.html'
    form_class=NameForm

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))

class CBVModel_FormView(FormView):
    template_name='template3.html'
    form_class=TopicForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data inserted sucessfully')

class CBVModel_ListView(ListView):
    model=Topic

    context_object_name='list'
    ordering=['topic_name']