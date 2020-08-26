import datetime
import json
import logging
import os
import pprint
from datetime import date

# import requests
from sqlalchemy import create_engine, MetaData, text, Table, Column, Integer, String, DateTime, Boolean, Numeric

SAMPLE_ENDPOINT = "https://api.coinmarketcap.com/v1/ticker"
DB_CONN=os.environ.get('DB_CONN')

logging.getLogger('boto').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

#### Raw API calls
def get_data(limit):
    payload = {
        'limit': limit
    }

    # resp = requests.get(SAMPLE_ENDPOINT, params=payload)
    # resp.raise_for_status()
    # data = resp.json()

    return ""

def cleanup(item):
    return {
        "name": item.get("name", ''),
        "symbol": item.get("symbol", ''),
        "rank": int(item.get("rank", 0)),
        "price_usd": float(item.get("price_usd", 0.0)),
        "24h_volume_usd": float(item.get("24h_volume_usd", 0.0)),
        "total_supply": float(item.get("total_supply", 0.0)),
        "percent_change_1h": float(item.get("percent_change_1h", 0.0)),
        "last_updated": make_datetime(int(item.get("last_updated", 0))),
    }

#### util methods
def make_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp / 1000)


# SQL Tables
metadata = MetaData()

sample_table = Table('sample_coinmarketcap', metadata,
                     Column('name', String(100), nullable=True),
                     Column('symbol', String(100), nullable=True),
                     Column('rank', Integer, nullable=True),
                     Column('price_usd', Numeric, nullable=True),
                     Column('24h_volume_usd', Numeric, nullable=True),
                     Column('total_supply', Numeric, nullable=True),
                     Column('percent_change_1h', Numeric, nullable=True),
                     Column('last_updated', DateTime, nullable=False)
                     )

def init_tables(engine):
    sample_table.drop(engine, checkfirst=True)
    metadata.create_all(engine)

def main(event, context):

    # get sample data
    # data = get_data(5)

    # sample_data = [cleanup(item) for item in data]
    sample_data = [{
        '24h_volume_usd': 8529300000.0,
        'last_updated': datetime.datetime(1970, 1, 18, 13, 55, 9, 567000),
        'name': 'Bitcoin',
        'percent_change_1h': 2.01,
        'price_usd': 11077.9,
        'rank': 1,
        'symbol': 'BTC',
        'total_supply': 16870925.0
    },
        {
            '24h_volume_usd': 2510770000.0,
            'last_updated': datetime.datetime(1970, 1, 18, 13, 55, 9, 551000),
            'name': 'Ethereum',
            'percent_change_1h': 0.7,
            'price_usd': 975.651,
            'rank': 2,
            'symbol': 'ETH',
            'total_supply': 97679773.0
        },
        {
            '24h_volume_usd': 1172320000.0,
            'last_updated': datetime.datetime(1970, 1, 18, 13, 55, 9, 541000),
            'name': 'Ripple',
            'percent_change_1h': 0.96,
            'price_usd': 1.21,
            'rank': 3,
            'symbol': 'XRP',
            'total_supply': 99992725510.0
        },
        {
            '24h_volume_usd': 663760000.0,
            'last_updated': datetime.datetime(1970, 1, 18, 13, 55, 9, 553000),
            'name': 'Bitcoin Cash',
            'percent_change_1h': 0.78,
            'price_usd': 1547.14,
            'rank': 4,
            'symbol': 'BCH',
            'total_supply': 16973175.0
        },
        {
            '24h_volume_usd': 865458000.0,
            'last_updated': datetime.datetime(1970, 1, 18, 13, 55, 9, 542000),
            'name': 'Litecoin',
            'percent_change_1h': 0.19,
            'price_usd': 230.273,
            'rank': 5,
            'symbol': 'LTC',
            'total_supply': 55263408.0
        }
    ]

    engine = create_engine(DB_CONN)
    init_tables(engine)
    conn = engine.connect()

    conn.execute(sample_table.insert().values(sample_data))

    pprint.pprint(sample_data)


if __name__ == "__main__":
    main(None, None)
