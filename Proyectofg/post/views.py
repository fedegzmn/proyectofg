from django.shortcuts import render_to_response
from django.template import RequestContext

from post.models import Post
from post.forms import PostForm

from django.contrib.auth.decorators import login_required

@login_required
def write_post(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return show_timeline(request)
    else:
        form = PostForm()

    return render_to_response('post/post.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        }))

def home(request):
    return render_to_response(
        'index.html',        
        RequestContext(
            request,
            {}
        )
    )