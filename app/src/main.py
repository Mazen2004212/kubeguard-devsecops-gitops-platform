from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
import random
import os

app = FastAPI(title="KubeGuard Demo App")

REQUEST_COUNT = Counter(
    "kubeguard_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "kubeguard_http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"]
)

APP_HEALTH = Gauge(
    "kubeguard_app_health_status",
    "Application health status, 1 means healthy and 0 means unhealthy"
)

START_TIME = time.time()


@app.middleware("http")
async def metrics_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(duration)

    return response


@app.get("/")
def root():
    return {
        "app": "KubeGuard Demo App",
        "status": "running",
        "message": "GitOps, monitoring, logging, alerting, and security demo"
    }


@app.get("/health")
def health():
    APP_HEALTH.set(1)
    return {
        "status": "healthy",
        "service": "kubeguard-demo-app"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready",
        "uptime_seconds": int(time.time() - START_TIME)
    }


@app.get("/stress")
def stress():
    start = time.time()
    result = 0

    while time.time() - start < 0.5:
        for number in range(1, 10000):
            result += number * number

    return {
        "status": "stress_completed",
        "duration_seconds": 0.5,
        "result": result
    }


@app.get("/random-error")
def random_error():
    if random.choice([True, False]):
        REQUEST_COUNT.labels(method="GET", endpoint="/random-error", status=500).inc()
        return Response(
            content='{"status":"error","message":"Simulated application error"}',
            status_code=500,
            media_type="application/json"
        )

    return {
        "status": "success",
        "message": "No error this time"
    }


@app.get("/config")
def config():
    return {
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "v1.0.0")
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)