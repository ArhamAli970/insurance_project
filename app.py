from src.exception import MyException
import sys
from src.logger import logging

try:
    a=2/0
except Exception as e:
    logging.info(e)
    raise MyException(e,sys) from e