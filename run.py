from stuffindex import utils
from stuffindex.application import application
from stuffindex.pages import pages
from paste import httpserver
from paste.cascade import Cascade
from paste.urlparser import StaticURLParser

static = StaticURLParser("./")

app = Cascade([application, static])

if __name__ == "__main__":
    print "blah"
    httpserver.serve(app, host="", port="8080")
    print "blah blah"
