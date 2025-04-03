import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("This is a debug message.")
logging.info("This is an info.")
logging.warning("This is a warning.")
logging.error("This is an error.")
logging.critical("This is critical message.")