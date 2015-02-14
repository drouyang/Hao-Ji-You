'''
The MIT License (MIT)

Copyright (c) 2015 Jiannan Ouyang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import signal, sys, logging
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class SimpleEcho(WebSocket):

   def handleMessage(self):
      if self.data is None:
         self.data = ''
      
      try:
         self.sendMessage(str(self.data))
      except Exception as n:
         print n

      print self.data
         
   def handleConnected(self):
      print self.address, 'connected'

   def handleClose(self):
      print self.address, 'closed'


   def handleConnected(self):
      print self.address, 'connected'
      for client in self.server.connections.itervalues():
         if client != self:
            try:
               client.sendMessage(str(self.address[0]) + ' - connected')
            except Exception as n:
               print n

   def handleClose(self):
      print self.address, 'closed'
      for client in self.server.connections.itervalues():
         if client != self:
            try:
               client.sendMessage(str(self.address[0]) + ' - disconnected')
            except Exception as n:
               print n


if __name__ == "__main__":

   parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
   parser.add_option("--host", default='', type='string', action="store", dest="host", help="hostname (localhost)")
   parser.add_option("--port", default=9999, type='int', action="store", dest="port", help="port (9999)")
   
   (options, args) = parser.parse_args()

   server = SimpleWebSocketServer(options.host, options.port, SimpleEcho)
   print "Start listen at port", options.port

   def close_sig_handler(signal, frame):
      server.close()
      sys.exit()

   signal.signal(signal.SIGINT, close_sig_handler)

   server.serveforever()
