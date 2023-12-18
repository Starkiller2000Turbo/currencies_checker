import logging
from logging.config import dictConfig
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Project Settings."""

    model_config = SettingsConfigDict(env_file='.env', extra='allow')

    ACCESS_KEY: str


settings = Settings()

DATA_EXPORT_LOCATION = str(BASE_DIR / 'data')
TARGET_API_URL = 'https://api.currencybeacon.com/v1/'

LOGGER_NAME = 'logger'


class LoggingConfig(BaseModel):
    """Logging configuration."""

    LOGGER_NAME: str = LOGGER_NAME
    LOG_FORMAT: str = '%(levelprefix)s | %(asctime)s | %(message)s'
    LOG_LEVEL: str = 'DEBUG'

    version: int = 1
    disable_existing_loggers: bool = False
    formatters: Dict[str, Dict[str, str]] = {
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    }
    handlers: Dict[str, Dict[str, str]] = {
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
    }
    loggers: Dict[str, Dict[str, Any]] = {
        LOGGER_NAME: {'handlers': ['default'], 'level': LOG_LEVEL},
    }


dictConfig(LoggingConfig().model_dump())
logger = logging.getLogger(LOGGER_NAME)
