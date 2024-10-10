from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from .get_weather import get_daily_weather_data


@extend_schema(
        summary="Retrieve Weather Date",
        description="This endpoint returns weather data.",
        responses={200: 'string'},
        parameters=[
            OpenApiParameter(
                name="region",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Category of servers to retrieve',
            )
        ]
    )
@api_view(['GET'])
@permission_classes([AllowAny])
def get_region_weather(request):
    region = request.GET.get('region', '')
    requested_coordinate = None
    weather = {}

    coordinates = {
        'tashkent':  [41.2995, 69.2401],
        'samarkand': [39.6542, 66.9597],
        'bukhara':   [39.7747, 64.4286],
        'andijan':   [40.7821, 72.3442],
        'fergana':   [40.3894, 71.7839],
        'namangan':  [40.9983, 71.6726],
        'karshi':    [38.8606, 65.7847],
        'nukus':     [42.4606, 59.617],
        'gulistan':  [40.4897, 68.7852],
        'khiva':     [41.3783, 60.3568],
        'navoiy':    [40.1039, 65.3686],
        'jizzakh':   [40.1164, 67.8423],
        'termez':    [37.2245, 67.2783],
    }

    if region and region.lower() in coordinates:
        requested_coordinate = coordinates.get(region)

    if requested_coordinate:
        weather['tashkent'] = get_daily_weather_data(*requested_coordinate)
    else:
        for region, coordinate in coordinates.items():
            weather[region] = get_daily_weather_data(*coordinate)

    return Response(weather)
