class SecondController(object):
    import models.model_2 as md2

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @classmethod
    def get_model_name(cls):
        return cls.md2.SecondModel.__name__
