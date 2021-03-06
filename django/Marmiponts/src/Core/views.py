from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Core.models import Information, Ingredient
from Core.forms import SearchField, InformationForm, IngredientField
import urllib.request
import json
from django.contrib.auth.models import User
import time
import random

@login_required
def dashboard(request):
	context={}
	Information_list = Information.objects.filter(user=request.user)
	Ingredient_list = Ingredient.objects.filter(user=request.user)
	Text_Info_Perso= "You did not edited your Personal Data! Do it ASAP to enjoy MarmiPonts"
	Text_Info_Ingred= "You have nothing in your Ingredient list!"
	if len(Information_list)>0:
		context["info"]= Information_list[0]
	else:
		context["textinfo_perso"]= Text_Info_Perso
	if len(Ingredient_list)>0:
		context["ingred"] = Ingredient_list
	else:
		context["textinfo_ingred"]=Text_Info_Ingred
	return render(request, "dashboard.html",context)


@login_required
def search(request): 
	form = SearchField(request.POST or None)
	f2f_api = 'e9e8a1b93cc2b48c60c0459bb0bc25b5'
	count = 0
	context = {"form": form,
				"count": count}
	if request.POST.get('search'):
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
			context = {"search_recipe": search_recipe,
 						"count": count} 
			for i in range(min(8,count)):
				context["Title"+str(i+1)]=ListTitles[i]
				context["ImgURL"+str(i+1)]=ListImgURL[i]
				context["F2FURL"+str(i+1)]=ListF2FURL[i]
				context["Id"+str(i+1)]=ListId[i]
				context["SrcURL"+str(i+1)]=ListSrcURL[i]

	return render(request, "search.html", context)


@login_required
def recipe(request,recipe_id):
	f2f_api = 'e9e8a1b93cc2b48c60c0459bb0bc25b5'

	url_get_recipe='http://food2fork.com/api/get?key=' + f2f_api

	final_url_get_recipe = url_get_recipe + '&rId=' + recipe_id  
	json_obj_get_recipe=urllib.request.urlopen(final_url_get_recipe).read()
	data_get_recipe = json.loads(json_obj_get_recipe.decode('utf-8'))
	Ingr = data_get_recipe['recipe']['ingredients']
	Title = data_get_recipe['recipe']['title']
	ImgURL = data_get_recipe['recipe']['image_url']
	SrcURL = data_get_recipe['recipe']['source_url']
	context = {"Ingr": Ingr, "Title":Title, "ImgURL":ImgURL, "SrcURL":SrcURL}

	return render(request, "recipe.html", context)

@login_required
def ingredients(request):
	Ingredient_list = Ingredient.objects.filter(user=request.user)
	text_limit = ""
	if request.POST.get('add_ingr'):
			form = IngredientField(request.POST, instance=Ingredient(user=request.user))
			if form.is_valid():
				ingredient = form.cleaned_data['ingredient']
				form.save()
			form=IngredientField()

	else:
		form=IngredientField()
	len_ingr = len(Ingredient_list)
	if len_ingr>9:
		form.fields['ingredient'].widget.attrs['readonly'] = True
		text_limit= "You can only have 10 ingredients"
	context={"form": form,
	"text_limit": text_limit,
	"len_ingr": len_ingr
	}
	if len_ingr>0:
		context["ingred_list"] = Ingredient_list
		if request.POST.get('delete0'):			
			Ingredient_list[0].delete()
			len_ingr-=1
	if len_ingr>1:
		if request.POST.get('delete1'):			
			Ingredient_list[1].delete()
			len_ingr-=1
	if len_ingr>2:
		if request.POST.get('delete2'):			
			Ingredient_list[2].delete()
			len_ingr-=1
	if len_ingr>3:
		if request.POST.get('delete3'):			
			Ingredient_list[3].delete()
			len_ingr-=1
	if len_ingr>4:
		if request.POST.get('delete4'):			
			Ingredient_list[4].delete()
			len_ingr-=1
	if len_ingr>5:
		if request.POST.get('delete5'):			
			Ingredient_list[5].delete()
			len_ingr-=1
	if len_ingr>6:
		if request.POST.get('delete6'):			
			Ingredient_list[6].delete()
			len_ingr-=1
	if len_ingr>7:
		if request.POST.get('delete7'):			
			Ingredient_list[7].delete()
			len_ingr-=1
	if len_ingr>8:
		if request.POST.get('delete8'):			
			Ingredient_list[8].delete()
			len_ingr-=1
	if len_ingr>9:
		if request.POST.get('delete9'):			
			Ingredient_list[9].delete()
			len_ingr-=1
	context['len_ingr']= len_ingr
	Ingredient_list = Ingredient.objects.filter(user=request.user)
	context["ingred_list"] = Ingredient_list
	return render(request, "ingredients.html",context)


@login_required
def personalinfo(request):
	Information_list = Information.objects.filter(user=request.user)
	Text_Edit=''
	if request.POST.get('edit'):  
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

@login_required
def suggest(request):
	f2f_api = '3bfb06fc13de32b982be4c417aa05826'
	User_Ingredient_List = Ingredient.objects.filter(user=request.user)
	Others_Ingredient_List= Ingredient.objects.exclude(user=request.user)
	
	list_o_users_ingred = [[],[]]
	for i in range(len(Ingredient.objects.exclude(user=request.user).values('user'))):
		list_o_users_ingred[0].append(Ingredient.objects.exclude(user=request.user).values('user')[i]['user'])
		list_o_users_ingred[1].append(Ingredient.objects.exclude(user=request.user).values('ingredient')[i]['ingredient'])



	list_o_users = list(set(list_o_users_ingred[0]))
	list_o_users.sort()
	print(list_o_users)
	list_users_info=[[],[]]


	list_o_users_ingred_organized=[]
	for i in list_o_users:
		list_o_users_ingred_organized.append([i])
		index = list_o_users_ingred_organized.index([i])
		list_o_users_ingred_organized[index].append(Information.objects.filter(user=i).values('First_name')[0]['First_name'])
		list_o_users_ingred_organized[index].append(Information.objects.filter(user=i).values('Room_number')[0]['Room_number'])
		list_o_users_ingred_organized[index].append(Information.objects.filter(user=i).values('Telephone_number')[0]['Telephone_number'])
		for j in range(len(Ingredient.objects.filter(user=i).values('ingredient'))):
			list_o_users_ingred_organized[index].append(Ingredient.objects.filter(user=i).values('ingredient')[j]['ingredient'])

	print(list_o_users_ingred_organized)

	U_Ingredient_List=[]
	for i in range(len(User_Ingredient_List)):
		U_Ingredient_List[len(U_Ingredient_List):]=[User_Ingredient_List[i].ingredient]
	Text_Partner = "No match"

	if len(list_o_users_ingred_organized)>0:	
		Text_Partner = ""
		U_Ingredient_List = U_Ingredient_List + list_o_users_ingred_organized[0][4:len(list_o_users_ingred_organized[0])]
		if len(list_o_users_ingred_organized)>1:
			U_Ingredient_List = U_Ingredient_List + list_o_users_ingred_organized[1][4:len(list_o_users_ingred_organized[1])]
		


	print(U_Ingredient_List)


	url_search='http://food2fork.com/api/search?key=' + f2f_api
	ListId=[]
	ingredient_string = ','.join(U_Ingredient_List)
	ingredient_string_url = ','.join(U_Ingredient_List).replace(' ', '+').replace(',',"%2C")
	final_url_search = url_search + '&q=' + ingredient_string_url
	print(final_url_search)
	json_obj_search=urllib.request.urlopen(final_url_search).read()
	data_search = json.loads(json_obj_search.decode('utf-8'))
	count = data_search['count']

	ingredient_liste = ingredient_string.split(',')
	print(ingredient_liste)
	while count == 0 :
		del ingredient_liste[random.randint(0,len(ingredient_liste)-1)]
		print(",".join(ingredient_liste))
		ingredient_string_url = ','.join(ingredient_liste).replace(' ', '+').replace(',',"%2C")
		final_url_search = url_search + '&q=' + ingredient_string_url
		json_obj_search=urllib.request.urlopen(final_url_search).read()
		data_search = json.loads(json_obj_search.decode('utf-8'))
		count = data_search['count']

	for item in data_search['recipes']:
		ListId = ListId + [item['recipe_id']]
	rand_recipe = int(time.clock())%count

	url_get_recipe='http://food2fork.com/api/get?key=' + f2f_api + '&rId=' + str(ListId[rand_recipe])
	json_obj_recipe=urllib.request.urlopen(url_get_recipe).read()
	data_recipe = json.loads(json_obj_recipe.decode('utf-8'))
	Title = data_recipe['recipe']['title']
	Recipe_ingredients = data_recipe['recipe']['ingredients']
	Source_url = data_recipe['recipe']['source_url']
	Image_url = data_recipe['recipe']['image_url']
 	




	context={"ingredient_list": "ingredient_list",
			"title": Title,
			"recipe_ingred": Recipe_ingredients,
			"source_url": Source_url,
			"image_url": Image_url,
			"match": Text_Partner
	}
	if len(list_o_users_ingred_organized)>0:
		for i in range(len(list_o_users_ingred_organized)):
			context['user'+str(i)]= list_o_users_ingred_organized[i][0]
			context['name'+str(i)]= list_o_users_ingred_organized[i][1]
			context['room'+str(i)]= list_o_users_ingred_organized[i][2]
			context['cell'+str(i)]= list_o_users_ingred_organized[i][3]
			context['list_ingr'+str(i)]= list_o_users_ingred_organized[i][4:len(list_o_users_ingred_organized[i])]
	return render(request, "suggest.html",context)