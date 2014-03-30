from jsonrpclib.jsonrpc import ServerProxy
from pprint import pprint


class OpenNLP:
    def __init__(self, host='localhost', port=8080):
        uri = "http://%s:%d" % (host, port)
        self.server = ServerProxy(uri)

    def parse(self, text):
        return self.server.parse(text)

if __name__ == '__main__':
    nlp = OpenNLP()
    results = nlp.parse("Shhh . Be vewy vewy quiet, I'm hunting wabbits .")
    print(results)
