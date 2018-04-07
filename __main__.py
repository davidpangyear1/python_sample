import sys
import configparser
import logging
import logging.config
from python_sample.engine import Engine # import ./engine.py and get the class Engine

### Read arguments
if len(sys.argv) < 3:
    print(f"usage:\npython {sys.argv[0]} <config_file> <logging_config_file>")
    sys.exit(1)
CONFIG_FILE = sys.argv[1]
LOGGING_CONFIG_FILE = sys.argv[2]

### Load logging config
try:
    logging.config.fileConfig(LOGGING_CONFIG_FILE)
except Exception as e:
    print(f"error loading config:{LOGGING_CONFIG_FILE}\n{repr(e)}")
    sys.exit(1)

### Start
logging.info("python_sample start")
try:
    logging.info(f"Reading config from:{CONFIG_FILE}")
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    logging.info("Initiating Engine")
    engine = Engine(config)

    logging.info("Starting Engine")
    engine.start()
except Exception as e:
    logging.exception("Unexpected error")
    sys.exit(1)
