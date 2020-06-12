from rest_framework import viewsets
from rest_framework.response import Response
from api_comments.apps.comments.api_authentication import AdminOnlyAuth
from api_comments.apps.comments.models import Question, Choice
from api_comments.apps.comments.serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    # authentication_classes = (AdminOnlyAuth, )
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionCustomView(viewsets.ViewSet):
    def list(self, request, format=None):
        questions = [question.question_text for question in Question.objects.all()]
        return Response(questions)
