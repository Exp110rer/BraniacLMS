from django.contrib import admin
from django.urls import path
from mainapp.apps import MainappConfig
from mainapp.views import MainPageView, NewsPageView, CoursesPageView, ContactsPageView, DocSitePageView, LoginPageView

app_name = MainappConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name="index"),
    path("news/", NewsPageView.as_view(), name="news"),
    path("courses/", CoursesPageView.as_view(), name="courses"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", DocSitePageView.as_view(), name="doc_site"),
    path("login/", LoginPageView.as_view(), name="login"),
]