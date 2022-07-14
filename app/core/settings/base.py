from enum import Enum

from pydantic import BaseSettings


class AppEnvTypes(Enum):
    dev: str = "dev"
    # prod: str = "prod"
    # test: str = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev
