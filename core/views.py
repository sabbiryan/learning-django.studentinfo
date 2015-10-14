from django.shortcuts import render


from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import core.models as coremodels

from django.core.urlresolvers import reverse_lazy

# Create your views here.

class LandingView(TemplateView):
	template_name = "base/index.html"


class StudentListView(ListView):
	model = coremodels.Student
	template_name = "student/list.html"


class StudentDetailView(DetailView):
	model = coremodels.Student
	template_name = "student/detail.html"
	context_object_name = 'student'


class StudentCreateView(CreateView):
	model = coremodels.Student
	template_name = "base/form.html"
	fields = "__all__"
	success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
	model = coremodels.Student
	template_name = "base/form.html"
	fields = "__all__"

class StudentDeleteView(DeleteView):
	model = coremodels.Student
	template_name = "student/delete.html"
	success_url = reverse_lazy('student_list')