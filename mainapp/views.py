from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from mainapp.models import News, Courses, CourseTeachers, Lesson

# Create your views here.

class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'
    extra_context = {'title': 'Main page'}
    

class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_qs'] = News.objects.all()[0:7]
        context['title'] = 'News'
        return context


class NewsPageDetailView(TemplateView):
    template_name = 'mainapp/news_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_object'] = get_object_or_404(News, pk = pk)
        context['title'] = context['news_object'].title
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_objects'] = Courses.objects.all()[0:7]
        context['title'] = 'Courses'
        return context


class CoursesPageDetailView(TemplateView):
    template_name = 'mainapp/courses_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_object'] = get_object_or_404(Courses, pk=pk)
        context['teachers'] = CourseTeachers.objects.filter(course=context['course_object'])
        context['lessons'] = Lesson.objects.filter(course=context['course_object'])
        context['title'] = context['course_object'].name
        return context

class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"