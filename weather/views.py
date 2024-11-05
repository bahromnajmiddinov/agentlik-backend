from django.templatetags.static import static

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

    eather_images = {
        0: static('weather/imgs/clear_sky.png'),
        1: static('weather/imgs/partly_cloudy.png'),
        2: static('weather/imgs/partly_cloudy2.png'),
        3: static('weather/imgs/overcast.png'),
        45: static('weather/imgs/fog.png'),
        48: static('weather/imgs/fog2.png'),
        51: static('weather/imgs/light_drizzle.png'),
        53: static('weather/imgs/moderate_drizzle.png'),
        55: static('weather/imgs/heavy_drizzle.png'),
        56: static('weather/imgs/light_freezing_drizzle.png'),
        57: static('weather/imgs/heavy_freezing_drizzle.png'),
        61: static('weather/imgs/light_rain.png'),
        63: static('weather/imgs/moderate_rain.png'),
        65: static('weather/imgs/heavy_rain.png'),
        66: static('weather/imgs/light_freezing_rain.png'),
        67: static('weather/imgs/heavy_freezing_rain.png'),
        71: static('weather/imgs/light_snow.png'),
        73: static('weather/imgs/moderate_snow.png'),
        75: static('weather/imgs/heavy_snow.png'),
        77: static('weather/imgs/snow_grains.png'),
        80: static('weather/imgs/light_rain_showers.png'),
        81: static('weather/imgs/moderate_rain_showers.png'),
        82: static('weather/imgs/heavy_rain_showers.png'),
        85: static('weather/imgs/light_snow_showers.png'),
        86: static('weather/imgs/heavy_snow_showers.png'),
        95: static('weather/imgs/thunderstorm.png'),
        96: static('weather/imgs/thunderstorm_light_hail.png'),
        99: static('weather/imgs/thunderstorm_heavy_hail.png'),
    }

    if region and region.lower() in coordinates:
        requested_coordinate = coordinates.get(region)

    if requested_coordinate:
        weather[region.lower()] = get_daily_weather_data(*requested_coordinate)
    else:
        for region, coordinate in coordinates.items():
            weather[region] = get_daily_weather_data(*coordinate)

    for weather_code in weather.values():
        for ind, code in enumerate(weather_code['current_weather_code']):
            weather_code['current_weather_code'][ind] = {'code': code, 'weather': eather_images.get(code)}

    return Response(weather)
