from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
import urllib.request
import json
import time


# Create your views here.
def home(request):
	f2f_api = 'e9e8a1b93cc2b48c60c0459bb0bc25b5'
	url_search='http://food2fork.com/api/search?key=' + f2f_api
	ListTitles=[]
	ListImgURL=[]
	ListF2FURL=[]
	final_url_search = url_search + '&q='
	rand = int(time.clock())%25

	json_obj_search=urllib.request.urlopen(final_url_search).read()
    
	data_search = json.loads(json_obj_search.decode('utf-8'))
    
	for item in data_search['recipes'][rand:rand+4]:
		ListTitles= ListTitles + [item['title']]
		ListImgURL= ListImgURL + [item['image_url']]
		ListF2FURL= ListF2FURL + [item['f2f_url']]
	
	context = {
		"Title1": ListTitles[0],
		"ImgURL1": ListImgURL[0],
		"F2FURL1": ListF2FURL[0],
		"Title2": ListTitles[1],
		"ImgURL2": ListImgURL[1],
		"F2FURL2": ListF2FURL[1],
		"Title3": ListTitles[2],
		"ImgURL3": ListImgURL[2],
		"F2FURL3": ListF2FURL[2],
		"Title4": ListTitles[3],
		"ImgURL4": ListImgURL[3],
		"F2FURL4": ListF2FURL[3],
		
	}
	return render(request, "home.html", context)



def about(request):
	return render(request, "about.html", {})


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = 'MarmiPonts Contact'
		from_email = settings.EMAIL_HOST_USER
		to_email = from_email
		contact_message = """
		%s: %s via %s
		"""%(form_full_name,form_message,form_email)
		send_mail(subject, contact_message, from_email, [to_email],fail_silently=False)
	return render(request, "contact.html",{"form":form})
