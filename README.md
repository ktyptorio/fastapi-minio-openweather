# Simple OpenWeather API Service using FastAPI and Minio Object Storage

This project is a simple API service that uses [FastAPI](https://fastapi.tiangolo.com/) to call the API from [OpenWeather](https://openweathermap.org/). 

The service is deployed using Docker and can be easily set up with the provided `docker-compose` file. 

## Deployment

Before deploying, you need to create a `.env` file and define the following values:
- `SECRET_KEY`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `MINIO_ROOT_USER`
- `MINIO_ROOT_PASSWORD`
- `MINIO_ACCESS_KEY`
- `MINIO_SECRET_KEY`

(Set up `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` after Minio Server is running. Stop and Run again the service after updating it in .env file)

To deploy the service, run the following command:

```
docker-compose up --env-file=.env --build
```

To migrate the database, run the following command:

```
docker-compose exec backend aerich init-db
docker-compose exec backend aerich upgrade
```

This will start the API service and make it available at `http://localhost:5000`.

## Note

Please note that OpenWeather requires you to have an API key for their service, and the provided code is for demonstration purposes only. To use this code for production purposes, you must obtain an API key from OpenWeather and replace the placeholder in the code.
