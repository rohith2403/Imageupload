from django.shortcuts import render
from .models import Image
from .forms import ImageForm

# Create your views here.
def img_view(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    form=ImageForm()
    img = Image.objects.all()
    return render(request,'testapp/home.html',{'img':img,'form':form})
