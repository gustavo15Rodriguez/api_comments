from django.contrib import admin
from api_comments.apps.comments.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
