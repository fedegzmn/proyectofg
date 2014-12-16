from django.shortcuts import render_to_response
from django.template import RequestContext

from post.models import Category
from post.models import Post
from post.forms import PostForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def one_post(request, idpost):
    post = Post.objects.get(id=idpost)
    
    return render_to_response(
        'post.html',
        {
            'post':post,
        },
    ) 

def posts_by_category(request, idcategory):
    category = Category.objects.get(id=idcategory)
    posts = category.post_set.order_by('-date_posted')
    
    return render_to_response(
        'index.html',
        {
            'posts':posts,
        },
    )

def home(request):
    return render_to_response(
        'index.html',
        RequestContext(
            request,
            {'posts': Post.objects.order_by('-date_posted')}
        )
    )

def sidebar(request):
    return render_to_response(
        'sidebar.html',
        RequestContext(
            request,
            {'posts': Post.objects}
        )
    )

def login(request):
    state = 'Inicie sesion'
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = 'Ha iniciado sesion exitosamente'
            else:
                state = 'Su cuenta no esta activada, contacte al administrador'
        else:
            state = 'El nombre de usuario y/o password son incorrectos'

    return render_to_response('registration/login.html',{'state':state, 'username': username})

@login_required
def write_post(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return home(request)
    else:
        form = PostForm()

    return render_to_response('writepost.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        }))