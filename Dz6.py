import logging
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d',
    handlers=[
        logging.FileHandler('logfile.log'),
        logging.StreamHandler()
    ]
)

current_date = datetime.now().strftime('%Y-%m-%d')

logging.info(f'Поточна дата: {current_date}')