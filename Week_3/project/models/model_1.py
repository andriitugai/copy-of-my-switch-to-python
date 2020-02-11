from model_2 import SecondModel


class FirstModel(object):
    import model_2

    def get_model_name(self):
        return self.__class__.__name__

    def get_second_model_name(self):
        pass


