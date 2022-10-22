from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse

# to mimic Single Page Application functionality, we have to keep track of the active page globally
active_page = 'home'

@require_GET
def index(request):
    return redirect('home')

@require_GET
def home(request):
    global active_page
    active_page = 'home'
    return render(request, 'info/base.html')

@require_GET
def update_active(request):
    active_link = request.GET.get('active')
    print(f'ACTIVE LINK: {active_link}')
    global active_page
    if active_link == 'projects':
        active_page = 'projects'
        return HttpResponse("""
        <button id="home" class="navbutton" hx-get="/update_active/?active=home" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Home</button>
        <button id="projects" class="active navbutton" hx-get="/update_active/?active=projects" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Projects</button>
        <button id="blog" class="navbutton" hx-get="/update_active/?active=blog" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Blog</button>
        """)
    elif active_link == 'blog':
        active_page = 'blog'
        return HttpResponse("""
        <button id="home" class="navbutton" hx-get="/update_active/?active=home" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Home</button>
        <button id="projects" class="navbutton" hx-get="/update_active/?active=projects" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Projects</button>
        <button id="blog" class="active navbutton" hx-get="/update_active/?active=blog" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Blog</button>
        """)
    else:
        active_page = 'home'
        return HttpResponse("""
        <button id="home" class="active navbutton" hx-get="/update_active/?active=home" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Home</button>
        <button id="projects" class="navbutton" hx-get="/update_active/?active=projects" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Projects</button>
        <button id="blog" class="navbutton" hx-get="/update_active/?active=blog" hx-trigger="click" hx-target="#main-nav-links" hx-swap="innerhtml">Blog</button>
        """)

@require_GET
def update_content(request):
    print(f'ACTIVE LINK FOR CONTENT: {active_page}')
    if active_page == 'projects':
        return render(request, 'info/projects.html')
    elif active_page == 'blog':
        return render(request, 'info/blog.html')
    else:
        return render(request, 'info/home.html')