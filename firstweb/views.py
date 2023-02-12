from django.shortcuts import render 
def homepage(request):
    try:
        name=request.GET['name']
        email=request.GET['email']
        sub=request.GET['subject']
        message=request.GET['message']
        print(name,email,sub,message)
    except:
        pass
    return render(request , "index.html") 
def info(request):
    return render(request,"info.html")   

         
