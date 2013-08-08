from stuffindex.models import model


class stuff(model()):
    def __init__(self, uid, he_said, it_means):
        self.data = {'uid': uid,
                     'he_said': he_said,
                     'it_means': it_means,
                     }

    def has_user(self):
        return 'uid' in self.data.keys()

    @classmethod
    def from_dict(cls, data):
        inst = cls(None, None, None)
        inst.data = data
        return inst

__all__ = ["stuff"]
