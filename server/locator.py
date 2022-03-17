

# from constants import QUEUES

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class locator:
    pass
    # graphers = {}
    # for api in QUEUES:
    #     graphers[api] = grapher(api)
    
    # def getgrapher(self,apiname):
    #     return self.graphers[apiname]



