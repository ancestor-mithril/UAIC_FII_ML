"""Run the program as following:
python em.py --help
    - displays help
python em.py data init iterations [--debug]
    - data: path to input data text file
        - contains 1D coordinates for a point each line
    - init: path to init data text file
        - contains 2 lines
        - each line has \\pi_i, \\mu_i, \\sigma_i^{2} in SSV format
    - iterations: positive integer which specifies number of iterations to be made
    - `--debug` option prints parameters for each iteration
"""

import sys

from functions import em


def run():
    if sys.argv[1] == "--help":
        print(__doc__)
        exit()
    # if True:
    try:
        data_path = sys.argv[1]
        init_path = sys.argv[2]
        max_iterations = int(sys.argv[3])
        try:
            debug = (sys.argv[4] == "--debug")
        except IndexError:
            debug = False
        em(data_path, init_path, max_iterations, debug)
    except Exception as e:
        print(e)
        print("Run `python em.py --help`")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Run `python em.py --help`")
        exit()
    run()
