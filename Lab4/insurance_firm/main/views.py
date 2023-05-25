from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('<h2>Main</h2>')

def about(request, name, age):
    return HttpResponse(f'''
            <h2>About user</h2>
            <p>Name: {name}</p>
            <p>Age: {age}</p>
            ''')

def contact(request):
    return HttpResponse('<h2>Contacts</h2>')
