from django.shortcuts import render
from django.db.models import Q

from news.form import ContactModelForm
from news.models import NewsModel, NewsCollectionModel, NewsLetterModel, CategoryModel, TagModel


def home_page_view(request):
    carousel_news = NewsCollectionModel.objects.filter(type='carousel').first().news.all()
    most_viewed_news = NewsModel.objects.all().order_by('views_count')[:6]
    latest_news = NewsModel.objects.all().order_by('-id')[:6]
    tags = TagModel.objects.all()
    categories = CategoryModel.objects.all()

    context = {
        "carousel_news": carousel_news,
        "most_viewed_news": most_viewed_news,
        "latest_news": latest_news,
        "tags": tags,
        "categories": categories,
    }
    return render(request, 'index.html', context)


def news_detail_page(request, pk):
    news = NewsModel.objects.filter(pk=pk)
    if news.exists():
        news = news.first()
        news.views_count += 1
        news.save()
        context = {"news": news}
        return render(request, 'news_detail.html', context)
    return render(request, '404.html')


def single_page_view(request):
    return render(request, 'news_detail.html')


def search_page_view(request):
    q = request.GET.get('q')
    category = request.GET.get('cat')
    tag = request.GET.get('tag')
    news = NewsModel.objects.filter(status=True)

    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()

    if q:
        news = news.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(author__first_name__icontains=q) |
            Q(author__last_name__icontains=q) |
            Q(tags__name__icontains=q) |
            Q(categories__name__icontains=q)
        ).distinct()

    category_name = None
    if category:
        news = NewsModel.objects.filter(status=True, categories__name=category)
        category_name = CategoryModel.objects.filter(name=category)

    tag_name = None
    if tag:
        news = NewsModel.objects.filter(status=True, tags__name=tag)
        tag_name = TagModel.objects.filter(name=tag)

    context = {
        "news": news,
        "category_name": category_name,
        "tag_name": tag_name,
        "categories": categories,
        "tags": tags,
        "q": q,
    }
    return render(request, 'search.html', context)



def contact_page_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
        else:
            context = {"errors": form.errors}
            return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')


def newsletter_view(request):
    nl = request.POST.get('nl')

    if nl:
        context = {}
        if not NewsLetterModel.objects.filter(email=nl).exists():
            NewsLetterModel.objects.create(email=nl)
            context = {'message': True}
        return render(request, 'newsletter_success.html', context)
