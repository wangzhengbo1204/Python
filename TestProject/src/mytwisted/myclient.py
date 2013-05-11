'''
Created on 2013-5-6

@author: Administrator
'''
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.protocol import Factory, Protocol

class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("MESSAGE %s\n" % msg)
        
    def dataReceived(self, data):
        print "from server:", data

class GreeterFactory(Factory):
    def buildProtocol(self, addr):
        return Greeter()

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sendMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)

point = TCP4ClientEndpoint(reactor, "localhost", 1234)
d = point.connect(GreeterFactory())
d.addCallback(gotProtocol)
reactor.run()

