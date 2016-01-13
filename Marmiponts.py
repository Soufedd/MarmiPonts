
import urllib.request
import json

f2f_api = '3bfb06fc13de32b982be4c417aa05826'




def f2f_search_getrecipe(query,rank):
    url_search='http://food2fork.com/api/search?key=' + f2f_api
    ListId=[]
    ListTitles=[]
    ListImgURL=[]
    url_get_recipe='http://food2fork.com/api/get?key=' + f2f_api
    ingredient = query.replace(' ','+').replace(',','%2C')
    final_url_search = url_search + '&q=' + ingredient 

    json_obj_search=urllib.request.urlopen(final_url_search).read()
    
    data_search = json.loads(json_obj_search.decode('utf-8'))
    
    #print(data_search['count'])
    for item in data_search['recipes'][0:3]:
        ListId= ListId + [item['recipe_id']]
        ListTitles= ListTitles + [item['title']]
        ListImgURL= ListImgURL + [item['image_url']]
    return [ListTitles,ListImgURL]
     
    final_url_get_recipe = url_get_recipe + '&rId=' + ListId[rank]
    print(final_url_get_recipe)
    json_obj_get_recipe=urllib.request.urlopen(final_url_get_recipe).read()
    data_get_recipe = json.loads(json_obj_get_recipe.decode('utf-8'))
    print(data_get_recipe['recipe']['title'])
    print(data_get_recipe['recipe']['ingredients'])
    print(data_get_recipe['recipe']['source_url'])  
    
f2f_search_getrecipe('chicken,potato',0)
f2f_search_getrecipe('pesto pasta', 0)
print(f2f_search_getrecipe('', 0)[0][0],f2f_search_getrecipe('', 0)[1][0])
