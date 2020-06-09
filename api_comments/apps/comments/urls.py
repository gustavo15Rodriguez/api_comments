from django.urls import path
from api_comments.apps.comments.views import IndexView, QuestionDetail, QuestionDelete, SwitchBoardView

urlpatterns = [
    path('', IndexView.as_view(), name='question_list'),
    path('detail/<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
    path('delete/<int:pk>/', QuestionDelete.as_view(), name='question_delete'),
    path('vote/<int:pk>/', SwitchBoardView.as_view(), name='vote_result'),
]
