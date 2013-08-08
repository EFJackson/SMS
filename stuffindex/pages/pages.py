from webapp2 import uri_for

from stuffindex.pages import BaseHandler
from stuffindex.application import application as app

from stuffindex.utils import redirect, render

from stuffindex.models.stuff import stuff


@app.route('/', 'index')
class Index(BaseHandler):
    def get(self):
        return self.render('index.html', stuffes=stuff.get_all())


@app.route('/add_stuff', 'add_stuff')
class Addstuff(BaseHandler):
    def get(self):
        return self.render('add_stuff.slim')

    def post(self):
        if self.user is not None:
            uid = self.profile['id']
            he_said = render(self.request.get('he_said'))
            it_means = render(self.request.get('it_means'))
            b = stuff(uid, he_said, it_means)
            b.push()
        raise redirect(uri_for('index'))


@app.route('/stuff/<stuff_id>', 'view_stuff')
class Viewstuff(BaseHandler):
    def get(self, stuff_id):
        b = stuff.get_by_id(stuff_id)
        return self.render('view_stuff.slim', stuff=b)
