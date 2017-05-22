from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'first_app/index.html')

def ninjas(request):
	return render(request, 'first_app/ninjas.html')

def ninja_display(request, color):
	if color != 'red' and color != 'blue' and color != 'orange' and color != 'purple':
		color = 'other'
	context = {
		'color': color
	}
	return render(request, 'first_app/' + color + '.html', context)