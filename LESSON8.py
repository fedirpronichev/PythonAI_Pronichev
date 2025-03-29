import logging


# logging.basicConfig(Level=logging.DEBUG)
# logging.debug
# logging.debug('debug')
# logging.info('info')
# logging.warning('info')
# logging.error('error')
# logging.critical('critical')


logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    filemode="w",
    format="We have next logging message: %(asctime)s - %(levelname)s - %(message)s"
)

try:
    print(10 / 0)
except Exception as e:
    logging.exception("Exception")


