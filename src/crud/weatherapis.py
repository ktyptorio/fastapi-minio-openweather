import requests
import io
import os
from minio import Minio
from datetime import datetime
import json

from src.database.models import Transactions

def upload_file(action, data):
    client = Minio(
        os.getenv("MINIO_HOSTNAME")+":9000",
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False
    )
    
    bucket_name = "bucket1"
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
    else:
        print(f"Bucket {bucket_name} already exists")
    json_data = json.dumps(data)
    date_time = datetime.now()
    file_path = f"{action}/openweather-"+str(date_time)+".json"
    client.put_object(
        bucket_name,
        file_path,
        io.BytesIO(bytes(json_data, 'UTF-8')),
        length=-1,
        part_size=10*1024*1024,
        content_type="application/json"
    )

    return {
        "bucket_name":bucket_name,
        "file_path":file_path
    }


async def get_weather_city(city, app_id):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+app_id)
    data = response.json()
    action = "get_weather_city"
    transaction = upload_file(action, data)
    transaction_obj = {}
    transaction_obj['action'] = action
    transaction_obj['bucket_name'] = transaction['bucket_name']
    transaction_obj['file_path'] = transaction['file_path']
    await Transactions.create(**transaction_obj)
    return {
        "city":city,
        "transaction":transaction
    }

async def get_weather_bulk(cities, app_id):
    data = {}
    list_data = []
    for city in cities:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+app_id)
        json_response = response.json()
        list_data.append(json_response)
    data['data'] = list_data
    action = "get_weather_bulk"
    transaction = upload_file(action, data)
    transaction_obj = {}
    transaction_obj['action'] = action
    transaction_obj['bucket_name'] = transaction['bucket_name']
    transaction_obj['file_path'] = transaction['file_path']
    await Transactions.create(**transaction_obj)
    return {
        "city":cities,
        "transaction":transaction
    }

async def get_weather_latlon(lat, lon, app_id):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+app_id)
    data = response.json()
    action = "get_weather_latlon"
    transaction = upload_file(action, data)
    transaction_obj = {}
    transaction_obj['action'] = action
    transaction_obj['bucket_name'] = transaction['bucket_name']
    transaction_obj['file_path'] = transaction['file_path']
    await Transactions.create(**transaction_obj)
    return {
        "Latitude":lat,
        "Longitude":lon,
        "transaction":transaction
    }