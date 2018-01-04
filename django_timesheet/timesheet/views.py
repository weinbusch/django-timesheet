
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from django_timesheet.timesheet.models import File, Task
from django_timesheet.timesheet.forms import TaskForm

class HomePage(generic.TemplateView):

    template_name = 'timesheet/index.html'

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = TaskForm()
        kwargs['object_list'] = Task.objects.filter(timer__status__in=['', 'running', 'paused'])
        return super().get_context_data(**kwargs)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        return self.render_to_response(self.get_context_data(form=form))

class FileListView(generic.ListView):

    model = File

    def get_queryset(self):
        queryset = super().get_queryset()
        lookup = self.request.GET.get('reference', None)
        if lookup:
            queryset = queryset.filter(reference__icontains=lookup)
        return queryset

class FileCreateView(generic.CreateView):

    model = File
    fields = ('reference',)

class FileUpdateView(generic.UpdateView):

    model = File
    fields = ('reference',)

class TaskCreateView(generic.CreateView):

    model = Task
    fields = ('file', 'description')

    def get_initial(self):
        if 'pk' in self.kwargs:
            file = get_object_or_404(File, pk=self.kwargs['pk'])
            return {'file': file.pk}

class TaskUpdateView(generic.UpdateView):

    model = Task
    fields = ('description',)
