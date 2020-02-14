class SecondModel(object):
    import models.model_1 as m1

    @classmethod
    def get_model_name(cls):
        return cls.__name__

    @classmethod
    def get_module_name(cls):
        return cls.__module__

    @classmethod
    def get_first_model_name(cls):
        return cls.m1.FirstModel.__name__


if __name__ == '__main__':
    print(SecondModel.get_module_name())
