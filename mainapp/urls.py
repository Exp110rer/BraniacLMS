from django.contrib import admin
from django.urls import path
from mainapp.apps import MainappConfig
from mainapp.views import MainPageView, NewsPageView, CoursesPageView, ContactsPageView, DocSitePageView, LoginPageView

app_name = MainappConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name="ndex"),
    path("news/", NewsPageView.as_view()),
    path("courses/", CoursesPageView.as_view()),
    path("contacts/", ContactsPageView.as_view()),
    path("doc_site/", DocSitePageView.as_view()),
    path("login/", LoginPageView.as_view()),
]