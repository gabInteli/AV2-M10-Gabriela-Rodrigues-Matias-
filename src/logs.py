# src/logs.py
import logging

logging.basicConfig(
    filename='logs/log.txt', 
    level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_info(message: str):
    logger.info(message)

def log_debug(message: str):
    logger.debug(message)

def log_warning(message: str):
    logger.warning(message)

def log_error(message: str):
    logger.error(message)

def log_critical(message: str):
    logger.critical(message)
