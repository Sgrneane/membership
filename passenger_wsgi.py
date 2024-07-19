import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

from membership.wsgi import application

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'Hello,Sagar correct me!\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     response = '\n'.join([message, version])
#     return [response.encode()]
