from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if register.objects.filter(email=email,password=password).first():
            request.session['email']=email
            return redirect('add_note')
        else:
            return render(request,'login.html',{'msg':"invalid password or email"})
    return render(request,'login.html')

def sign(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if (password == cpassword):
            register(fname=fname,lname=lname,email=email,password=password,cpassword=cpassword).save()
            return render(request,'sign_up.html',{'msg':'registration done'})
        else:
            return render(request,'sign_up.html',{'msg':'wrong password'})

    return render(request,'sign_up.html')

def add_notes(request):
    if 'email' not in request.session:
        return redirect('login')
    user = register.objects.get(email=request.session['email'])
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        
        note(title=title,content=content,user=user).save()
        messages.success(request,"successfully saved")
    return render(request,'add_note.html',{'user':user})


def logout(request):
    request.session.flush()
    return redirect('login')

def my_note(request):
    if 'email' not in request.session:
        return redirect ('login')
    
    user = register.objects.get(email=request.session['email'])
    notes=note.objects.filter(user=user)
    return render(request,'my_note.html',{'user':user,'notes':notes})


def delete_note(request, pk):
    notes = note.objects.get(id=pk)  # database se note fetch karo
    notes.delete()                   # delete kar do
    return redirect('my_note') 

def edit_note(request,pk):
    notes = get_object_or_404(note, id=pk)   # us id ka note uthao
    if request.method == "POST":
        notes.title = request.POST['title']   # naya title
        notes.content = request.POST['content'] # naya content
        notes.save()   # database update
        return redirect('my_note') 
    
def update_pass(request):
    if "email" not in request.session:
        return redirect('login')
    
    user=register.objects.get(email=request.session['email'])

    if request.method=="POST":
        email=request.POST['email']
        oldpassword=request.POST['old']
        newpassword=request.POST['new']
        confirmpassword=request.POST['confirm']
        if (user.password == oldpassword):
            if (newpassword == confirmpassword):
                register.objects.filter(password=oldpassword).update(password=newpassword,cpassword=confirmpassword)
                messages.success(request,"password updated")
            else:
                messages.success(request,"new password and confirm password are not same")
                return render(request,"update_pass.html",{'user':user})
        else:
            messages.success(request,"old password is not matched")
            return render(request,"update_pass.html",{'user':user})

    return render(request,"update_pass.html",{'user':user})


def update_profile(request):
    if "email" not in request.session:
        return redirect('login')
    user=register.objects.get(email=request.session['email'])
    if request.method=="POST":
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        if (user.password == password):
            register.objects.filter(email=email).update(fname=fname,lname=lname)
            messages.success(request,'update successfully')
        else:
            messages.error(request,'your password is wrong')
            return render(request,"update_profile.html",{'user':user})
    
    return render(request,"update_profile.html",{'user':user})