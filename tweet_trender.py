import time
import json
import zmq
import sys
import pprint
import numpy

if __name__ == "__main__":
      if (len(sys.argv) != 3):
            print "Format arguments as tweet_trender.py keyword daterange, please"
            exit()

dateRange = sys.argv[1]

# connect to zmq  
context = zmq.Context()  
socket = context.socket(zmq.REQ)   
address = ("tcp://%s:5555" % sys.argv[1])  
print "connecting to server %s" % address  
socket.connect(address)

# format and send data package to zmq server
dataset = {'type' : "tweet_pull", 'keyword' : keyword, 'dateRange' : dateRange }
message = json.dumps(dataset)
socket.send(message)

message = socket.recv()

