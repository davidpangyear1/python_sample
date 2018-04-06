import logging

class Engine:
    def __init__(self):
        self.text = "Hello? I am good at fight!"

    def start(self):
        logging.info("Engine starting")
        logging.info(self.text)
