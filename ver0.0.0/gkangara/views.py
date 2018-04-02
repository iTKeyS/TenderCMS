from django.shortcuts import render

def startpage(request):
    query = request.GET.get('name')
    message = "{}, Добро пожаловать в приложения".format(query)
    template = 'startpage.html'
    context = {'message': message,}
    return render(request, template, context)
