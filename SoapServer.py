import socket
from flask import Flask
from flask_spyne import Spyne
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer, Unicode
from spyne.protocol.soap import Soap11


app = Flask(__name__)
spyne = Spyne(app)

class StringReversalService(spyne.Service):
    __service_url_path__ = '/stringreverse'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, _returns = Unicode)
    def stringReverse(str):
        reversedString = ''
        index = len(str)
        while index:
            index -= 1                       
            reversedString += str[index]
        return reversedString

# ip_address = socket.gethostbyname(socket.gethostname())
# print ip_address

if __name__ == '__main__':
    app.run(host = '127.0.0.1')