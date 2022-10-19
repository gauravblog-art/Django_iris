from django.shortcuts import render

# Create your views here.

def welcome(request):

    return render(request, 'index.html')
    # return HttpResponse("Hello word")
def User(request):
    # now I am going to get the form data using username

    usern = request.GET['username']
    # print(usern)
    return render(request, 'user.html', {'name':usern})