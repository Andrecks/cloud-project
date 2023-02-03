from django.shortcuts import render

def my_view(request):
    dots = [
    {'x': 50, 'y': 50, 'text': 'Text 1))))))))))))'},
    {'x': 100, 'y': 100, 'text': 'Text 2'},
    {'x': 150, 'y': 150, 'text': 'Text 3'},
    ]
    return render(request, 'home.html', {'dots': dots})