from fastapi import APIRouter, Depends, Query
import src.crud.weatherapis as crud
from src.auth.jwthandler import get_current_user


router = APIRouter()

@router.get(
    "/api/openweather-city/", 
    tags=['Open Weather'],
    dependencies=[Depends(get_current_user)]
)
async def get_weather_city(
    city: str = Query(
        ...,
        title="City",
        description="Query string for the weather to search based on City",
    ),
    app_id: str = Query(
        ...,
        title="app_id",
        description="Query string as a app_id which required by Open Weather"
    )
):
    response = await crud.get_weather_city(city, app_id)

    return response

@router.get(
    "/api/openweather-bulk/",
    tags=['Open Weather'],
    dependencies=[Depends(get_current_user)]
)
async def get_weather_bulk(
    cities: list = Query(
        default=[],
        title="List of City",
        description="Query string for the weather to search based on list of city",
    ),
    app_id: str = Query(
        ...,
        title="app_id",
        description="Query string as a app_id which required by Open Weather"
    )
):
    response = await crud.get_weather_bulk(cities, app_id)

    return response

@router.get(
    "/api/openweather-latlon/",
    tags=['Open Weather'],
    dependencies=[Depends(get_current_user)]
)
async def get_weather_latlon(
    lat: float = Query(
        ...,
        title="Latitude",
        description="Query string for the weather to search based on Latitude and Longitude",
    ),
    lon: float = Query(
        ...,
        title="Longitude",
        description="Query string for the weather to search based on Latitude and Longitude",
    ),
    app_id: str = Query(
        ...,
        title="app_id",
        description="Query string as a app_id which required by Open Weather"
    )
):
    response = await crud.get_weather_latlon(lat, lon, app_id)
    return response