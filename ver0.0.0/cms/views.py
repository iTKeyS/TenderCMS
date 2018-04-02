from django.shortcuts import render, get_object_or_404, redirect
#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib import messages
from gkangara.config import pagination

from .models import Post, Category
from .forms import PostForm#, CommentForm

def post_list(request):
    template = 'post_list.html'
    object_list = Post.objects.filter(status='Published')

    pages = pagination(request, object_list, num=1)

    context = {
    'items': pages[0],
    'page_range': pages[1]
    }
    return render(request, template, context)

def post_detail(request, slug):
    template = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, template, context)

def category_detail(request, slug):
    template = 'category_detail.html'
    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=category)
    context = {
    'category': category,
    'post': post,
    }
    return render(request, template, context)

def search(request):
    template = 'post_list.html'

    query = request.GET.get('q')

    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        results = Post.objects.filter(status="Published")

    pages = pagination(request, results, num=1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
    }
    return render(request, template, context)

def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    template = 'category/list_of_post_by_category.html'
    context = {'categories': categories, 'post': post, 'category': category}
    return render(request, template, context)

def list_of_post(request):
    post = Post.objects.all()
    #filter(status='published')
    paginator = Paginator(post, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'post/list_of_post.html'
    context = {'post': post, 'page': page}
    return render(request, template, context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    if post.status == 'published':
        template = 'post/post_detail.html'
        return render(request, template, context)
    else:
        template = 'post/post_preview.html'
        return render(request, template, context)

def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'post/add_comment.html'
    content = {'form': form}
    return render(request, template, context)

###############
##Backend##
###############
def new_post(request):
    template = 'new_post.html'
    form = PostForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно добавлен аукцион')

    except Exception as e:
        form = PostForm()
        messages.warning(request, "Аукцион не сохронён. Ошибка: {}".format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)

#custom admin

def edit_post(request, id):
    template = 'new_post.html'
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Успешно сохронение изменений аукцион")

        except Exception as e:
            messages.warning(request, 'Изменения аукцион не сохронено. Ошибка: {}'.format(e))

    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)

def delete_post(request, id):
    template = 'new_post.html'

    post = get_object_or_404(Post, id=id)

    try:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            post.delete()
            messages.success(request, 'Аукцион успешно удалён')
        else:
            form = PostForm(instance=post)
    except Exception as e:
        messages.warning(request, 'Аукцион не удалён. Ошибка {}'.format(e))

    context = {
        'form': form,
    }
    return render(request, template, context)

def post_list_admin(request):
    template = 'post_list_admin.html'

    post = Post.objects.all()

    form = PostForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно добавлен аукцион')

    except Exception as e:
        form = PostForm()
        messages.warning(request, "Аукцион не сохронён. Ошибка: {}".format(e))


#    pages = pagination(request, post, 5)

    context = {
        'items': post,
        'form': form,
#        'items': pages[0],
#        'page_range': pages[1]
    }
    return render(request, template, context)
