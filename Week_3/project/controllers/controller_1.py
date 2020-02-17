class FirstController(object):

    import models.model_1 as md1

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @classmethod
    def get_model_name(cls):
        return cls.md1.FirstModel.__name__

    @classmethod
    def get_module_name(cls):
        return cls.md1.__name__


if __name__ == '__main__':
    print(FirstController.get_module_name())
