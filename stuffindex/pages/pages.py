import time

from stuffindex.pages import BaseHandler
from stuffindex.application import application as app

from stuffindex.utils import stuffes_to_json

from stuffindex.models.stuff import Stuff
from stuffindex.models import gfs


@app.route('/', 'index')
class Index(BaseHandler):
    def get(self):
        return self.render('index.html', stuffes=Stuff.get_all())


@app.route('/add_stuff', 'add_stuff')
class AddStuff(BaseHandler):
    def get(self):
        return self.render('add_stuff_form.html')

    def post(self):
        print self.request.POST
        x_coord = self.request.POST.get('x_coord', 0)
        y_coord = self.request.POST.get('y_coord', 0)
        category = self.request.POST.get('category', 'Other')
        date = self.request.POST.get('date', str(int(time.time())))
        img = self.request.POST.get('img', None).value
        image_file_id = gfs.put(img)
        print image_file_id
        stuff = Stuff(image_file_id, (y_coord, x_coord), date, category)
        print stuff.push()


@app.route('/img/<stuff_id>', 'view_image')
class ViewImage(BaseHandler):
    def get(self, stuff_id):
        stuff = Stuff.get_by_id(stuff_id)
        img = gfs.get(stuff.image).read()
        self.response.content_type = "image/jpg"
        self.response.write(img)


@app.route('/choose_location', 'choose_location')
class ChooseLocation(BaseHandler):
    def get(self):
        return self.render('map.html')


@app.route('/list_stuff', 'list_stuff')
class ListStuff(BaseHandler):
    def get(self):
        all_stuff = self.request.GET.get('all', False)
        x_coord = self.request.GET.get('x_coord', 0)
        y_coord = self.request.GET.get('y_coord', 0)
        centre = (y_coord, x_coord)
        if all_stuff:
            stuffes = Stuff.get_all()
        else:
            stuffes = Stuff.get_near(centre, 100)
        return self.render('list_stuff.html', stuffes=stuffes, centre=centre)


@app.route('/api/list_stuff', 'api_list_stuff')
class APIListStuff(BaseHandler):
    def get(self):
        x_coord = self.request.GET.get('x_coord', 0)
        y_coord = self.request.GET.get('y_coord', 0)
        stuffes = Stuff.get_near((x_coord, y_coord), 100)
        self.response.content_type = 'application/json'
        self.response.write(stuffes_to_json(stuffes))
