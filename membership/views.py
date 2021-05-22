from django.shortcuts import render

# Create your views here.

def membership(request):
    """ A view to return membership page """

    return render(request, 'membership/membership.html')
    