from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import MainTodo

#for register
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
	#re
from django.shortcuts import redirect

#for message in form
from django.contrib import messages
#custom user form
from .myforms import NewUserForm



# Create your views here.
def homepage(request):
	return render(request=request,template_name="main/home.html")


def viewlist(request):
	#return HttpResponse("wow this is awesome")
	print(request.user.id," \t",request.user)
	return render(request=request,template_name="main/viewlist.html",context={"todos":MainTodo.objects.filter(todo_username=request.user.id)})

def register(request):

	if request.method=="POST":
		form =NewUserForm(request.POST)
		if form.is_valid() :
			user=form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f"New Account Created :{username}")
			#user is created so loginthe user
			login(request,user)
			messages.info(request,f"You are now logged in as :{username}")
			return redirect("main:homepage") # u could write like redirect("app_name:name_in_path")
		else:

			for err in form.error_messages:
				messages.error(request,f"{err}:{form.error_messages[err]}")

	form =NewUserForm()
	return render(request=request,template_name="main/register.html",context={"form":form})

def logout_user(request):
	logout(request)
	messages.info(request,"You are logged out ")
	return redirect("main:homepage")

#we import authenticationForm for login
def login_user(request):
	if request.method=="POST":
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid() :
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			if user is not None:
				messages.success(request,f"logged in as :{username}")
				#user is created so loginthe user
				login(request,user)
				return redirect("main:homepage") # u could write like redirect("app_name:name_in_path")
			else:
				messages.error(request,f"Invalid username or password ")
	form = AuthenticationForm()
	return render(request = request,template_name = "main/login.html",context={"form":form})


from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django import forms
from .models import MainTodo

class BookForm(forms.ModelForm):
	class Meta:
		model = MainTodo
		widgets={'todo_username':forms.HiddenInput()}

		fields = ['todo_title','todo_deadline','todo_content','todo_status']
		

def book_list(request, template_name='main/book_list.html'):
    #book = MainTodo.objects.all()
    book = MainTodo.objects.filter(todo_username=request.user.id)
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_create(request, template_name='main/book_form.html'):
	print("hello ",request.user.id,"name ",request.user.username)

	form = BookForm(request.POST or None)
	if form.is_valid():
		data = form.save(commit=False)
		data.todo_username=request.user
		print("field ","hello ",request.user.id,"name ",request.user.username)
		data.save()
		#form.save()
		return redirect('main:book_list')
	return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='main/book_form.html'):
    book= get_object_or_404(MainTodo, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('main:book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='main/book_confirm_delete.html'):
    book= get_object_or_404(MainTodo, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('main:book_list')
    return render(request, template_name, {'object':book})