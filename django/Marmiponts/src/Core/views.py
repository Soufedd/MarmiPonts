from django.shortcuts import render

# Create your views here.
def dashboard(request):


	context={

	}
	return render(request, "dashboard.html",context)

def ingredients(request):

	context={

	}
	return render(request, "ingredients.html",context)

def personalinfo(request):

	context={

	}
	return render(request, "personalinfo.html",context)
