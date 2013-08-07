import webapp2
import pprint

from webapp2_extras import sessions

from mako import lookup
import plim

from stuffindex import config

mako_render = lookup.TemplateLookup(directories=['stuffindex/pages/templates'],
                                    preprocessor=plim.preprocessor)


class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        self.render_globals = {'uri_for': webapp2.uri_for,
                               'current_url': self.request.url,
                               'current_page': self.request.path_qs,
                               'request': self.request,
                               'user': self.user,
                               'pretty': pprint.pformat,
                               }
        if self.user is not None:            self.profile = graph.get_object("me")
            self.render_globals['profile'] = self.profile

        try:
            # Dispatch the request.
            return webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def render(self, template, **kwargs):
        kwargs.update(self.render_globals)
        return mako_render.get_template(template).render(**kwargs)
