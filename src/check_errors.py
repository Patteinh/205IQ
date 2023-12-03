from src.utils import help

def check_args(ac, av):
    if ac == 2 and av[1] == "-h":
        help()
        exit(0)
    if ac not in (3, 4, 5):
        raise Exception("ERROR: The number of arguments must be (3, 4, 5).")
    for arg in av[1:]:
        try:
            arg_value = float(arg)
        except ValueError:
            raise Exception("ERROR: The provided argument must be a number.")
        if arg_value < 0:
            raise Exception("ERROR: The provided argument must be a positive number.")
        if ac == 5:
            iq1 = float(av[3])
            iq2 = float(av[4])
            if iq2 < iq1:
                raise Exception("ERROR: iq2 need to be greater than to iq1.")
