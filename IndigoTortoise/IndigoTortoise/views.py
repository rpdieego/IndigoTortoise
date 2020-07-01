from django.shortcuts import render


'''
HOME PAGE

-  Landpage with general information;

'''

def home(request):
    return render(request, 'index.html')



'''
ABOUT PAGE

- Social Network Links;
- Short Bio;
- Explain the reason for the site and motivation;

'''

def about(request):
    return render(request, 'about.html')