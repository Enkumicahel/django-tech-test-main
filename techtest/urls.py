"""techtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from techtest.articles.views import ArticleView, ArticlesListView
from techtest.authors.views import AuthorsListView, AuthorView
from techtest.regions.views import RegionView, RegionsListView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Articles
    path("articles/", ArticlesListView.as_view(), name="articles-list"),
    path("articles/<int:article_id>/", ArticleView.as_view(), name="article"),
    # Authors
    path("authors/", AuthorsListView.as_view(), name="authors-list"),
    path("authors/<int:article_id>/", AuthorView.as_view(), name="author"),
    # Regions
    path("regions/", RegionsListView.as_view(), name="regions-list"),
    path("regions/<int:region_id>/", RegionView.as_view(), name="region"),
]
