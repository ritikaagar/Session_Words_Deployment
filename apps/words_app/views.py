anfrom django.shortcuts import render,redirect, HttpResponse
from time import gmtime, strftime

def index(request):
	try:
		request.session["final_word"]
	except:
		request.session["final_word"] = []
	
	return render(request,'words_app/index.html')

def process(request):
	if request.POST.get("font") == "font":
		fontsize = "big"
	else:
		fontsize = "small"

	context = {
	"word": request.POST.get("word"),
	"color": request.POST.get("color"),
	"font": fontsize,
	"time": strftime("%B %d, %Y %H:%M %p", gmtime())
	}

	request.session["final_word"].append(context)
	request.session.modified = True  #allows to append information 
	print request.session['final_word']
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')