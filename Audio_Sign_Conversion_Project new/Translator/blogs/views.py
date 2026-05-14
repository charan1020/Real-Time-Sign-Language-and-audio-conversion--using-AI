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
import subprocess
import sys


BLOGS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BLOGS_DIR)


def run_script(script_path):
    subprocess.Popen(
        [sys.executable, script_path],
        cwd=PROJECT_ROOT,
        creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0,
    )


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
    run_script(os.path.join(BLOGS_DIR, "main2.py"))
    return render(request, "userhome.html", {"msg": "Audio to Sign started. Use the popup window to continue."})

def sign_audio(request):
    run_script(os.path.join(PROJECT_ROOT, "detect_gesture.py"))
    return render(request, "userhome.html", {"msg": "Sign to Audio started. Use the camera window to continue."})


def userhome(request):
    return render(request, "userhome.html", {})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})
