from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Core.models import Information
from Core.forms import SearchField, InformationForm
import urllib.request
import json
from django.contrib.auth.models import User

@login_required
def dashboard(request):
	Information_list = Information.objects.filter(user=request.user)
	Text_Info= "You did not edited your Personal Data! Do it ASAP to enjoy MarmiPonts"
	if len(Information_list)>0:
		context= {"info": Information_list[0],
				"textinfo": ""}
	else:
		context={"textinfo":Text_Info}
	return render(request, "dashboard.html",context)

@login_required
def search(request): 
	form = SearchField(request.POST or None)
	f2f_api = 'e9e8a1b93cc2b48c60c0459bb0bc25b5'
	count = 0
	context = {"form": form,
				"count": count}
	if request.method == 'POST':
		if form.is_valid():
			search_recipe = form.cleaned_data.get("search_recipe")
			if not search_recipe:
				search_recipe = " "
			search_query= search_recipe.replace(' ','+').replace(',','%2C')
			ListTitles=[]
			ListImgURL=[]
			ListF2FURL=[]
			ListSrcURL=[]
			ListId=[]
			ListIngr=[]
			url_search='http://food2fork.com/api/search?key=' + f2f_api
			url_get_recipe='http://food2fork.com/api/get?key=' + f2f_api
			final_url_search = url_search + '&q=' + search_query
			json_obj_search=urllib.request.urlopen(final_url_search).read()
			data_search = json.loads(json_obj_search.decode('utf-8'))
			count= data_search['count']
			for item in data_search['recipes'][0:min(8,count)]:
				ListTitles= ListTitles + [item['title']]
				ListImgURL= ListImgURL + [item['image_url']]
				ListF2FURL= ListF2FURL + [item['f2f_url']]
				ListSrcURL= ListSrcURL + [item['source_url']]
				ListId= ListId + [item['recipe_id']]
			for ID in ListId:
				final_url_get_recipe = url_get_recipe + '&rId=' + ID  
				json_obj_get_recipe=urllib.request.urlopen(final_url_get_recipe).read()
				data_get_recipe = json.loads(json_obj_get_recipe.decode('utf-8'))
				ListIngr= ListIngr + [data_get_recipe['recipe']['ingredients']]
			context = {"search_recipe": search_recipe,
						"count": count}
			for i in range(min(8,count)):
				context["Title"+str(i+1)]=ListTitles[i]
				context["ImgURL"+str(i+1)]=ListImgURL[i]
				context["F2FURL"+str(i+1)]=ListF2FURL[i]
				context["Ingr"+str(i+1)]=ListIngr[i]
				context["SrcURL"+str(i+1)]=ListSrcURL[i]

	return render(request, "search.html", context)



@login_required
def ingredients(request):

	context={

	}
	return render(request, "ingredients.html",context)


@login_required
def personalinfo(request):
	Information_list = Information.objects.filter(user=request.user)
	Text_Edit=''
	if request.method == 'POST':  
		form = InformationForm(request.POST, instance=Information(user=request.user)) 
		if form.is_valid():
			First_name = form.cleaned_data['First_name']
			Last_name = form.cleaned_data['Last_name']
			Departement = form.cleaned_data['Departement']
			Room_number = form.cleaned_data['Room_number']
			Telephone_number = form.cleaned_data['Telephone_number']
			if len(Information_list)>0 :
				Information_list[0].delete() 
			form.save()
			Text_Edit='Data Edited! Go back to the Dashboard'
	else:
		if len(Information_list)>0 :
			init={'user' : request.user,
				'First_name': Information_list[0].First_name,
				'Last_name': Information_list[0].Last_name,
				'Departement': Information_list[0].Departement,
				'Room_number': Information_list[0].Room_number,
				'Telephone_number': Information_list[0].Telephone_number,
				} 
		else:
			init={'user' : request.user,
				} 
		form = InformationForm(initial=init)

	context={"form": form,
			"textedit": Text_Edit}
	return render(request, "personalinfo.html",context)
