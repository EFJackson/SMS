from geopy import point
from geopy import distance

from stuffindex.models import model


class Stuff(model()):
    def __init__(self, image, coordinates, date, category):
        self.data = {'image': image,
                     'coordinates': coordinates,
                     'date': date,
                     'category': category, }

    @property
    def point(self):
        return point.Point(self.coordinates)

    @classmethod
    def from_dict(cls, data):
        inst = cls(None, None, None, None)
        inst.data = data
        return inst

    @classmethod
    def get_near(cls, location, range_km=5):
        centre = point.Point(location)
        all_stuff = cls.get_all()
        for stuff in all_stuff:
            d = distance.distance(stuff.point, centre).km
            if d < range_km:
                yield stuff

__all__ = ["Stuff"]
