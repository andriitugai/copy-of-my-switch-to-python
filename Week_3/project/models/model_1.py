class FirstModel(object):
    import models.model_2 as m2

    @classmethod
    def get_model_name(cls):
        return cls.__name__

    @classmethod
    def get_module_name(cls):
        return cls.__module__

    @classmethod
    def get_second_model_name(cls):
        return cls.m2.SecondModel.__name__
