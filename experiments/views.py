from django.views.generic import ListView, DetailView, CreateView
from .models import Experiment

class ExperimentListView(ListView):
    model = Experiment
    template_name = 'experiments/experiment_list.html'
    context_object_name = 'experiments'
    ordering = ['-date_created']

class ExperimentDetailView(DetailView):
    model = Experiment
    template_name = 'experiments/experiment_detail.html'

class ExperimentCreateView(CreateView):
    model = Experiment
    template_name = 'experiments/experiment_form.html'
    fields = ['title', 'description', 'wavelength', 'power']