from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
	if request.method == 'POST':
		result = request.POST.get('result', '')

		return render(request, 'index.html', {'result': result})

	return render(request, 'index.html')
