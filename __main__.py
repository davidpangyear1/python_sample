import sys
from python_sample.engine import Engine # import ./engine.py and get the class Engine

print("arguments:%s" % (str(sys.argv)))

engine = Engine()
engine.start()
