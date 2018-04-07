import logging

class Engine:
    def __init__(self, config):
        section = config['general']
        self.print_text = section['print_text']
        self.print_count = int(section['print_count'])

    def start(self):
        for i in range(0, self.print_count):
            logging.info(self.print_text)
