from math import sqrt


def solve_quadratic_equation(a: float, b: float, c: float) -> (float, float):
    """
    return the 2 solutions for quadratic equation, should they exist
    :param a: float
    :param b: float
    :param c: float
    :return: (sol_1: float, sol_2, float)
    """
    determinant = (b ** 2) - (4 * a * c)
    if determinant < 0:
        return None, None
    return (-b - sqrt(determinant)) / (2 * a), (-b + sqrt(determinant)) / (2 * a)
