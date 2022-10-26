from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse
from .models import Project, Post
from .my_data import personal_data, tech_data, contact_data
import marko

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
    elif active_link == 'blog':
        active_page = 'blog'
    else:
        active_page = 'home'
    context = {'active_page': active_page}
    return render(request, 'info/navbar.html', context)

@require_GET
def update_content(request):
    print(f'ACTIVE LINK FOR CONTENT: {active_page}')
    if active_page == 'projects':
        all_projects = Project.objects.all()
        context = {'projects': all_projects}
        return render(request, 'info/projects.html', context)
    elif active_page == 'blog':
        all_blog_posts = Post.objects.all()
        context = {'posts': all_blog_posts}
        return render(request, 'info/blog.html', context)
    else:
        context = {'personal': personal_data, 'tech': tech_data, 'contact': contact_data}
        return render(request, 'info/home.html', context)

@require_GET
def get_blog_post(request, id):
    curr_post = Post.objects.get(id=id)
    # generate file name for txt file
    filename = curr_post.title.lower().replace(' ', '_') + '.txt'
    # read content from txt file
    content = list()
    filename = 'why_htmx_is_awesome.txt'
    with open('/home/default/Code/my_public_portal/info/static/info/posts/' + filename) as rf:
        line = rf.readline()
        while line:
            if "```" in line:
                code_block = True
                while code_block:
                    next_line = rf.readline()
                    if "```" in next_line:
                        code_block = False
                    line = line + next_line
                content.append(marko.convert(line))
            else:
                content.append(marko.convert(line))
            line = rf.readline()
    context = {'post': curr_post, 'content': content}
    return render(request, 'info/post.html', context)