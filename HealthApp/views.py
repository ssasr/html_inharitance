from django.shortcuts import render

# Create your views here.
def header_view(request):
    return render(request,'healthapp/head_footer.html')
def home_view(request):
    return render(request,'healthapp/home.html')
