from webapp2 import uri_for

import time

import gridfs

from stuffindex.pages import BaseHandler
from stuffindex.application import application as app

from stuffindex.utils import redirect, render

from stuffindex.models.stuff import Stuff
from stuffindex.models import gfs


@app.route('/', 'index')
class Index(BaseHandler):
    def get(self):
        return self.render('index.html', stuffes=stuff.get_all())


@app.route('/add_stuff', 'add_stuff')
class AddStuff(BaseHandler):
    def post(self):
        print self.request.POST
        x_coord = self.request.POST.get('x_coord', 0)
        y_coord = self.request.POST.get('y_coord', 0)
        category = self.request.POST.get('category', 'Other')
        date = self.request.POST.get('date', str(int(time.time())))
        img = self.request.POST.get('img', None).value
        image_file_id = gfs.put(img)
        print image_file_id
        stuff = Stuff(image_file_id, (x_coord, y_coord), date, category)
        print stuff.push()

@app.route('/img/<stuff_id>', 'view_image')
class ViewImage(BaseHandler):
    def get(self, stuff_id):
        stuff = Stuff.get_by_id(stuff_id)
        img = gfs.get(stuff.image).read()
        self.response.content_type = "image/jpg"
        self.response.write(img)
