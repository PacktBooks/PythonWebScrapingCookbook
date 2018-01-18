from __future__ import print_function
from twisted.internet.task import react

import treq


def print_response(response):
    print(response.code, response.phrase)
    print(response.headers)

    return treq.text_content(response).addCallback(print)

def main(reactor, *args):
    d = treq.get('http://httpbin.org/get')
    d.addCallback(print_response)
    return d

react(main, [])
