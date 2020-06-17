from django.views.generic import ListView, DetailView, CreateView
from api_comments.apps.comments.forms import VoteForm
from api_comments.apps.comments.mixins import RequireLoginMixin
from api_comments.apps.comments.models import Question, Choice
from django.urls import reverse_lazy


class VoteCreate(RequireLoginMixin, CreateView):
    model = Choice
    form_class = VoteForm
    template_name = 'comments/results.html'
    success_url = reverse_lazy('choice_list')


class VoteList(RequireLoginMixin, ListView):
    template_name = 'comments/list_choices.html'
    context_object_name = 'latest_choices_list'

    def get_queryset(self):
        return Choice.objects.order_by('-votes')


class VoteDetail(RequireLoginMixin, DetailView):
    model = Choice
    template_name = 'comments/detail_choice.html'

