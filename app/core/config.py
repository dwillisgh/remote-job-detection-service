from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    """
    class for settings, allowing values to be overridden by environment variables.

    """

    IS_ON_DEV_MACHINE: bool = (
        True  # True if the service is running locally on developer machine.
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str = "jobs-remote-detection-service"
    SERVER_NAME: str = "EKS"
    VERSION: str = "1.0"
    DD_SERVICE_NAME: str = "jobs-remote-detection-service"
    DEBUG: bool = False
    APP_ENV: str = "dev"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    OTEL_TRACES_EXPORTER: str = "otlp"
    OTEL_RESOURCE_ATTRIBUTES: str = "service.name=jobs-remote-detection-service,application=app"

    class Config:
        case_sensitive = True


settings = Settings()
