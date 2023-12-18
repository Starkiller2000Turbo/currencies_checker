import json
from datetime import datetime, timedelta

import requests
from fastapi import APIRouter

from app.api.v1.schemas import MessageSchema
from app.api.v1.utils import daterange
from app.config import DATA_EXPORT_LOCATION, TARGET_API_URL, settings

router_currencies = APIRouter(prefix='/currencies')


@router_currencies.get('/')
def save_currencies_info() -> MessageSchema:
    """Save currencies information.

    Returns:
        Message if operation succeeded.
    """
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)
    response = requests.get(
        TARGET_API_URL + 'timeseries/',
        params={
            'api_key': settings.ACCESS_KEY,
            'start_date': str(start_date),
            'end_date': str(end_date),
            'symbols': 'USD,EUR,RUB',
        },
    )
    response_data = response.json().get('response')
    file_data = {}
    for date_item in daterange(start_date, end_date):
        date_data = response_data.get(str(date_item))
        EUR_data = date_data.get('EUR')
        RUB_data = date_data.get('RUB')
        file_data[str(date_item)] = {
            'USD': RUB_data,
            'EUR': RUB_data / EUR_data,
        }
    with open(
        f'{DATA_EXPORT_LOCATION}/{end_date.strftime("%d-%m-%Y")}.json',
        'w',
    ) as json_file:
        json.dump(file_data, json_file)
    return MessageSchema(message='successfull')


router_v1 = APIRouter(
    prefix='/v1',
    tags=['API V1'],
)

router_v1.include_router(router_currencies)
