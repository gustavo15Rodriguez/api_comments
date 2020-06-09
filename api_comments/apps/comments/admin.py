from django.contrib import admin
from api_comments.apps.comments.models import Question, Choice

admin.register(Question)
admin.register(Choice)
