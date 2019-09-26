import os


class BaseConfigModel(object):

    def __init__(self):
        self.__BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        with open(os.path.join(self.__BASE_DIR, 'test.conf'), encoding='utf-8') as config:
            row = config.readline()
            data = row.replace(' ', '').split('=')
            key = data[0]
            value = data[1]

            self.__class__.__setattr__(self, key, value)


class ConfigModel(BaseConfigModel):
    pass
