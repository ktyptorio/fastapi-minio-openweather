# Simple OpenWeather API Service using FastAPI and Minio Object Storage

This project is a simple API service that uses [FastAPI](https://fastapi.tiangolo.com/) to call the API from [OpenWeather](https://openweathermap.org/). 

The service is deployed using Docker and can be easily set up with the provided `docker-compose` file. 

## Deployment

Before deploying, you need to create a `.env` file and define the following values:
- `SECRET_KEY`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

To deploy the service, run the following command:

```
docker-compose up --env-file=.env --build
```


This will start the API service and make it available at `http://localhost:5000`.

## Note

Please note that OpenWeather requires you to have an API key for their service, and the provided code is for demonstration purposes only. To use this code for production purposes, you must obtain an API key from OpenWeather and replace the placeholder in the code.
