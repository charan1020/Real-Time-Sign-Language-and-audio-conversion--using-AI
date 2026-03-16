'''
from django.shortcuts import render, redirect
from django.http import HttpResponse

def homepage(request):
    return render(request,"index.html",{})

#import MySQLdb
#con=MySQLdb.connect("localhost","root","","SignTranslator")
c1=con.cursor()
def registration(request):
    if request.method=="POST":
        name = request.POST["t1"]
        mailid = request.POST["t2"]
        mno = request.POST["t3"]
        uid = request.POST["t4"]
        pwd = request.POST["t5"]
        c1.execute("insert into users values('%s','%s','%s','%s','%s')"
                   %(name,mailid,mno,uid,pwd))
        con.commit()
        return render(request, "registration.html",
                      {"msg": "New User Registered!!"})
    return render(request,"registration.html",{})

def login(request):
    if request.method=="POST":
        uid = request.POST["t1"]
        pwd = request.POST["t2"]
        c1.execute("select * from users where userid='%s' and password='%s'"%
                   (uid,pwd))
        if c1.rowcount>=1:
            return redirect(userhome)
        else:
            return render(request, "login.html", {"msg":"You're not authorized user"})
    return render(request,"login.html",{})

import os
def audio_sign(request):
    os.system("python ./blogs/main2.py")
    return HttpResponse("")

def sign_audio(request):
    os.system("python ./detect_gesture.py")
    return HttpResponse("")

def userhome(request):
    return render(request, "userhome.html", {})

def about(request):
    return render(request,"about.html",{})

def contact(request):
    return render(request,"contact.html",{})
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse


import os


def homepage(request):
    return render(request, "index.html", {})


def registration(request):
    if request.method == "POST":
        return render(request, "registration.html",
                      {"msg": "User Registered Successfully (Demo Mode)"})
    return render(request, "registration.html", {})


def login(request):
    if request.method == "POST":
        return redirect(userhome)
    return render(request, "login.html", {})


def audio_sign(request):
    os.system("python ./blogs/main2.py")
    return HttpResponse("Audio to Sign Executed")

def sign_audio(request):
    import os
    import sys

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    script_path = os.path.join(project_root, "detect_gesture.py")

    os.system(f'"{sys.executable}" "{script_path}"')

    return HttpResponse("Sign to Audio Executed")


def userhome(request):
    return render(request, "userhome.html", {})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})