from django.shortcuts import render

# Create your views here.


def blog_list(request):
    return render(request, 'blog/blog_list.html')

def blog_details(request):
    return render(request, 'blog/blog_details.html')