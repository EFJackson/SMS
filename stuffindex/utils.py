import webapp2
import logging
import json

from webapp2_extras.routes import RedirectRoute

from markdown2 import markdown


import html5lib
from html5lib import sanitizer, treebuilders, treewalkers, serializer


class WSGIApplication(webapp2.WSGIApplication):
    def __init__(self, *args, **kwargs):
        super(WSGIApplication, self).__init__(*args, **kwargs)
        self.router.set_dispatcher(self.__class__.custom_dispatcher)

    @staticmethod
    def custom_dispatcher(router, request, response):
        rv = router.default_dispatcher(request, response)
        if isinstance(rv, basestring):
            rv = webapp2.Response(rv)
        elif isinstance(rv, tuple):
            rv = webapp2.Response(*rv)

        return rv

    def route(self, url, name):
        def outer_wrapped(cls):
            logging.info("Adding route %s to class %s with name %s"
                         % (url, cls, name))
            self.router.add(RedirectRoute(url, cls,
                                          name=name,
                                          strict_slash=True))
            return cls
        return outer_wrapped


def redirect(url):
    """ Redirect the user to a given url, generally after a POST action has
    completed """
    return webapp2.redirect(url, abort=True)


def sanitizer_factory(*args, **kwargs):
    san = sanitizer.HTMLSanitizer(*args, **kwargs)
    return san


def clean_html(buf):
    """Cleans HTML of dangerous tags and content."""
    buf = buf.strip()
    if not buf:
        return buf

    p = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"),
                            tokenizer=sanitizer_factory)
    dom_tree = p.parseFragment(buf)

    walker = treewalkers.getTreeWalker("dom")
    stream = walker(dom_tree)

    s = serializer.htmlserializer.HTMLSerializer(omit_optional_tags=False,
                                                 quote_attr_values=True)
    return s.render(stream)


def render(untrusted_input):
    return markdown(clean_html(untrusted_input))


def stuffes_to_json(stuffes):
    def stuff_data_filter(stuff):
        d = stuff.data
        d['image'] = str(d['image'])
        d['_id'] = str(d['_id'])
        return d
    return json.dumps([stuff_data_filter(s) for s in stuffes])
