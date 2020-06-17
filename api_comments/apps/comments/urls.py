from django.urls import path
from api_comments.apps.comments.views import VoteList, VoteDetail, VoteCreate

urlpatterns = [
    path('', VoteList.as_view(), name='choice_list'),
    path('detail/<int:pk>/', VoteDetail.as_view(), name='choice_detail'),
    path('vote/', VoteCreate.as_view(), name='vote_result'),
]
