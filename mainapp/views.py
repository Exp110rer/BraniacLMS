from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'
    

class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['range'] = range(5)
    #     return context

class NewsPagePaginatedView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_num'] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"