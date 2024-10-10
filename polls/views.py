from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Poll, Choice
from .serializers import PollSerializer


class PollListView(ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetailView(RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = 'id'

    def post(self, request, id):
        choice_id = request.GET.get('choice_id', 0)

        poll = get_object_or_404(Poll, id=id)
        choice = get_object_or_404(poll.choices, id=choice_id)

        choice.clicks += 1
        choice.save()

        return Response(status=200)
