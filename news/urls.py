from django.urls import path

from news.views import home_page_view, contact_page_view, single_page_view, news_detail_page, \
    search_page_view, newsletter_view

app_name = 'news'

urlpatterns = [
    path('contact/', contact_page_view, name='contact'),
    path('single/', single_page_view),
    path('category/', search_page_view, name='search'),
    path('<int:pk>/', news_detail_page, name='news_detail_page'),
    path('newsletter/', newsletter_view, name='newsletter'),
    path('', home_page_view, name='home'),
]
