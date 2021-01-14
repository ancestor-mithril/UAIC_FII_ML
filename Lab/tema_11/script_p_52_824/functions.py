import os
from typing import List, Tuple
import math


def em(data_path: str, init_path: str, max_iterations: int, debug: bool = False):
    """

    :param data_path: path to input file
    :param init_path: path to init file
    :param max_iterations: number of iterations to be made
    :param debug: flag for parameters displaying during iterations
    :return: void
    """
    assert os.path.isfile(data_path), "data is not a valid path"
    assert os.path.isfile(init_path), "init is not a valid path"
    assert max_iterations > 0, "iterations is not bigger than 0"
    data, pi, mu, sigma = read_data(data_path, init_path)
    print(
        f"""
        data: {data}
        pi: {pi}
        mu: {mu}
        sigma^{2}: {sigma}
        """
    )
    for iteration in range(max_iterations):
        # E
        gamma = [compute_gamma(pi, mu, sigma, data[i]) for i in range(len(data))]
        # M
        gamma_sum = sum([gamma[i][0] for i in range(len(gamma))]), sum([gamma[i][1] for i in range(len(gamma))])
        pi = (
                gamma_sum[0] / len(gamma),
                gamma_sum[1] / len(gamma)
        )
        mu = (
            sum([gamma[i][0] * data[i] for i in range(len(gamma))]) / gamma_sum[0],
            sum([gamma[i][1] * data[i] for i in range(len(gamma))]) / gamma_sum[1]
        )
        sigma = (
            (sum([gamma[i][0] * (data[i] - mu[0]) ** 2 for i in range(len(gamma))]) / gamma_sum[0]) ** 0.5,
            (sum([gamma[i][1] * (data[i] - mu[1]) ** 2 for i in range(len(gamma))]) / gamma_sum[1]) ** 0.5
        )

        if debug:
            lambda_string = "\n".join([str(x) for x in gamma])
            print("\ngamma:" + f"{lambda_string}" + "\n")
            print(f"pi: {pi}")
            print(f"mu: {mu}")
            print(f"sigma: {sigma}")

    if not debug:
        print(f"pi: {pi}")
        print(f"mu: {mu}")
        print(f"sigma: {sigma}")


def compute_gamma(pi: List[float], mu: List[float], sigma: List[float], x: float) -> (float, float):
    """
    Computes lambda 1 and lambda 2
    :param pi: current iteration pi
    :param mu: current iteration mu
    :param sigma: current iteration sigma
    :param x: x for each lambda is computed
    :return: gamma_{i1}, gamma_{i2}
    """
    lam1 = pi[0] * normal_distribution(sigma[0], mu[0], x)
    lam2 = pi[1] * normal_distribution(sigma[1], mu[1], x)
    return lam1 / (lam1 + lam2), lam2 / (lam1 + lam2)


def normal_distribution(sigma: float, mu: float, x: float) -> float:
    """

    :param sigma:
    :param mu:
    :param x:
    :return: normal distribution with current parameters
    """
    return 1 / ((2 * math.pi) ** 0.5 * sigma) * math.exp(- 0.5 * ((x - mu) / sigma) ** 2)


def read_data(data_path: str, init_path: str) -> Tuple[List[float], List[float], List[float], List[float]]:
    """

    :param data_path: path to input file
    :param init_path: path to init file
    :return: data=list of 1D coordinates, initial [pi_1, pi_2], initial [mu_1, mu_2], initial [sigma_1, sigma_2]
    """
    with open(data_path, "r") as fp:
        data = list(map(float, [x.split()[0] for x in fp.readlines()]))
    with open(init_path, "r") as fp:
        lines = list(map(lambda x: list(map(float, x)), [x.split() for x in fp.readlines()]))
        pi, mu, sigma = zip(lines[0], lines[1])
    return data, pi, mu, sigma
