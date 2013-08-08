from stuffindex.models import model


class Stuff(model()):
    def __init__(self, image, coordinates, date, category):
        self.data = {'image': image,
                     'coordinates': coordinates,
                     'date': date,
                     'category': category, }

    @classmethod
    def from_dict(cls, data):
        inst = cls(None, None, None, None)
        inst.data = data
        return inst

__all__ = ["Stuff"]
