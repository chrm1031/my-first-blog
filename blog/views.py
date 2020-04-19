from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # {}の中で指定した変数名をテンプレートで表示することができる
    return render(request, 'blog/post_list.html', {'posts': posts})


# get_objects_or_404は取得したpkが存在しないときに返す404ページを整形する
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
