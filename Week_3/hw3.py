from models import model_1 as m1, model_2 as m2
from controllers import controller_1 as c1, controller_2 as c2


def main():
    print("CONTROLLER NAMES: {}, {}"
        .format(
            c1.FirstController.get_class_name(), c2.SecondController.get_class_name()
        )
    )
    print("CONTROLLER MODELS: {}, {}"
        .format(
            c1.FirstController.get_model_name(), c2.SecondController.get_model_name()
        )
    )
    print("IMPORTED MODELS: {} include: {}, {} include {}"
        .format(
            m1.FirstModel().get_module_name(), m1.FirstModel().get_second_model_name(),
            m2.SecondModel().get_module_name(), m2.SecondModel().get_first_model_name()
        )
    )


if __name__ == '__main__':
    main()
