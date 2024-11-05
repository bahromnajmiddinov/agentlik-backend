from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from .models import Poll
from .serializers import PollSerializer


class PollListView(ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetailView(RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Add click to poll",
        description="This endpoint to add new clicks for poll.",
        responses={200: PollSerializer},
        parameters=[
            OpenApiParameter(
                name="choice_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Choice ID of poll.',
            )
        ]
    )
    def put(self, request, id):
        choice_id = request.GET.get('choice_id', 0)

        poll = get_object_or_404(Poll, id=id)
        choice = get_object_or_404(poll.choices, id=choice_id)

        choice.clicks += 1
        choice.save()

        return Response(status=200, data=PollSerializer(poll).data)
