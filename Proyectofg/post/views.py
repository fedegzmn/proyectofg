from django.shortcuts import render_to_response
from django.template import RequestContext

from post.models import Category
from post.models import Post
from post.forms import PostForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#Vista para un solo post
def one_post(request, idpost):
    post = Post.objects.get(id=idpost)
    lastposts = Post.objects.all() #Sirve para poder mostrar los posts en la barra del costado, a traves de un for
    cat = Category.objects.all() #Lo mismo, con las categorias
        
    return render_to_response(
        'post.html',
        {
            'post':post,
            'cat':cat,
            'lastposts':lastposts,
        },
    ) 

#Vista para filtrar posts por categoria
def posts_by_category(request, idcategory):
    category = Category.objects.get(id=idcategory)
    posts = category.post_set.order_by('-date_posted')
    lastposts = Post.objects.all()
    cat = Category.objects.all()
    
    return render_to_response(
        'index.html',
        {
            'posts': posts,
            'cat':cat,
            'lastposts':lastposts,
        },
    )

#La pagina de inicio, en la que se muestran los posts
def home(request):
    cat = Category.objects.all()
    lastposts = Post.objects.all()
    return render_to_response(
        'index.html',
        RequestContext(
            request,
            {
                'posts': Post.objects.order_by('-date_posted'),
                'cat':cat,
                'lastposts':lastposts,
            }
        )
    )

#Vista del login
def login(request):
    lastposts = Post.objects.all()
    cat = Category.objects.all()
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

    return render_to_response('registration/login.html',        
        RequestContext(
            request,
            {
                'state':state,
                'username': username,
                'cat':cat,
                'lastposts':lastposts,
            }
        )
        )

#Vista del formulario para escribir un nuevo post, requiere previamente haber iniciado sesion
@login_required
def write_post(request):
    lastposts = Post.objects.all()
    cat = Category.objects.all()
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
        'cat':cat,
        'lastposts':lastposts,
        }))