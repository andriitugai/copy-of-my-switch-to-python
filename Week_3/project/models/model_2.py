import sys


class SecondModel(object):

    def get_model_name(self):
        return self.__class__.__name__

    def get_first_model_name(self):
        print(model_1.FirstModel.__class__.__name__)


from model_1 import FirstModel 

if __name__ == '__main__':
    y = SecondModel()
    print(y.get_first_model_name())
    print(sys.modules)
