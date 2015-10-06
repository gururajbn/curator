from django.shortcuts import render
from django.views.generic import View
from .models import products,selected
from django.http import HttpResponseRedirect,HttpResponse,Http404
import json
# Create your views here.
class home(View):

	def get(self,request):
		template_name="home.html"
		pro= products.objects.filter(curated=False).order_by("?")[:17]
		sel= selected.objects.filter(user=request.user)
		return render(request,template_name,{
			"products":pro,
			"selected":sel
			})

	def post(self,request):
		user= request.user
		itemId= request.POST["itemId"]
		proId=products.objects.get(pk=itemId)
		select= selected(user=user,product=proId)
		select.save()
		proId.curated=True
		proId.save()
		data={"pk":itemId}
		return HttpResponse(json.dumps(data),content_type="application/json")
		
class delete(View):

	def post(self,request):
		user= request.user
		itemId= request.POST["itemId"]
		print "itemID:",itemId
		proId=products.objects.get(pk=itemId)
		remove=selected.objects.filter(user=user,product=proId).order_by("-time")[0]
		remove.delete()
		proId.curated=False
		proId.save()
		data={"pk":itemId}
		return HttpResponse(json.dumps(data),content_type="application/json")

class search(View):

	def get(self,request):
		itemId= request.GET["itemId"]
		print "itemId:",itemId
		product= products.objects.get(pk=itemId)
		data={
				"name":product.name,
				"brand":product.brand,
				"price":product.price,
				"description":product.description,
				"category":product.category,
				"image":product.image,
				"pk":product.pk
		}
		return HttpResponse(json.dumps(data),content_type="application/json")

	def post(self,request):
		category= request.POST["selectbasic"]
		if category == "all":
			return HttpResponseRedirect('/')
		itemList= products.objects.filter(category=category)
		print itemList,category
		template_name="home.html"
		data={"results":itemList,
		      "message": "%d items found in %s" % (len(itemList),category.capitalize()),
		      "selected":selected.objects.filter(user=request.user)
			  }
		return render(request,template_name,data)
		
class crop(View):

	def get(self,request,pk):
		image= products.objects.get(pk=pk)
		template_name="crop.html"
		data={
			"item":image
		}
		return render(request,template_name,data)
		