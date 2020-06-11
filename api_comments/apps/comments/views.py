from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, DeleteView,View
from django.views.generic.base import TemplateResponseMixin

from api_comments.apps.comments.mixins import RequireLoginMixin
from api_comments.apps.comments.models import Question, Choice


class IndexView(ListView):
    template_name = 'comments/list_comments.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class QuestionDetail(RequireLoginMixin, DetailView):
    model = Question
    template_name = 'comments/detail_comments.html'


class QuestionDelete(RequireLoginMixin, DeleteView):
    model = Question
    success_url = "/polls/"


class VoteView(View):
    def get_queryset(self, choice_id):
        return Choice.objects.get(pk=choice_id)

    def post(self, request, pk):
        question_id = pk
        choice_id = request.POST.get('choice', None)

        try:
            queryset = self.get_queryset(choice_id)
        except(KeyError, Choice.DoesNotExist):
            return redirect('detail', pk=question_id)

        else:
            queryset.votes += 1
            queryset.save()
            return redirect('result', pk=question_id)


class ResultView(TemplateResponseMixin, View):
    template_name = 'comments/results.html'

    def get_queryset(self, question_id):
        return Question.objects.get(pk=question_id)

    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        context = {'question': queryset}
        return self.render_to_response(context)


class SwitchBoardView(View):
    def get(self, request, pk):
        view = ResultView.as_view()
        return view(request, pk)

    def post(self, request, pk):
        view = VoteView.as_view()
        return view(request, pk)
