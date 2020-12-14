from django.shortcuts import render
from django.http import JsonResponse
from Statistics import plots
# Create your views here.
def home(request):
    return render(request, 'home.html')

def create_chart(request):
    # try:
        plots.create_plots()
        return JsonResponse({'status':'sucess'})
    # except:
    #     return JsonResponse({'status':'error'})
