from django.shortcuts import render
from PVP.forms import YTForm
# Create your views here.


def app(request):
	form = YTForm()
	if request.method == 'POST':
		form = YTForm(request.POST)
		if form.is_valid():
			link = str(request.POST['link'])
			url = list(link)
			code =[]
			for i in range (32,len(url)):
				code.append(url[i])
			rad= list("https://www.youtube.com/embed/")
			cod = "".join(rad + code)
			print(cod)
			context = {'link': cod}
			return render(request,'PVP/app.html',context)
		else:
			form = YTForm()
	return render(request, 'PVP/app.html',{'form' : form})




	