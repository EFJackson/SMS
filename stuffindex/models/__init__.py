import pymongo
import gridfs
from bson.objectid import ObjectId

client = pymongo.MongoClient()
db = client.stuffindex

gfs = gridfs.GridFS(db, 'img_fs')


def model(host='localhost', port=27017, database='stuffindex', collection='stuff'):
    client = pymongo.MongoClient(host, port)
    db = client[database]
    coll = db[collection]

    class Model(object):
        collection = coll

        def __getattr__(self, name):
            try:
                return self.data[name]
            except KeyError:
                raise AttributeError

        def push(self):
            self.data['_id'] = self.collection.insert(self.data)
            return self.data['_id']

        def remove(self):
            self.collection.remove(self.data['_id'])

        def save(self):
            self.collection.save(self.data)

        @classmethod
        def get_by_id(cls, _id):
            i = ObjectId(_id)
            data = cls.collection.find_one({'_id': i})
            return cls.from_dict(data)

        @classmethod
        def get(cls, **kwargs):
            data = cls.collection.find_one(kwargs)
            return cls.from_dict(data)

        @classmethod
        def get_all(cls, **kwargs):
            results = cls.collection.find(kwargs)
            return map(cls.from_dict, results)

        @classmethod
        def from_dict(cls, data):
            inst = cls()
            inst.data = data
            return inst

    return Model
