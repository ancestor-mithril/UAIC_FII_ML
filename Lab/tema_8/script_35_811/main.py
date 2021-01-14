"""Run the program as following:
python main.py path-to-input-file similarity-function [--all-solutions]
        => where `path-to-input-file` is the path to the input file
            * input file should contain each point on separated lines, and point coordinates should be in SSV format
        => the `similarity-function` may be:
            * `-single-linkage`
            * `-complete-linkage`
            * `-average-linkage`
            * `-ward-linkage`
        => if `--all_solutions` flag is used the program returns all possible clusterizations
"""

import sys
import os


from clustering import prepare_clustering
from utils import error_print, color_print, CustomError

similarity_functions = ["-single-linkage", "-complete-linkage", "-average-linkage", "-ward-linkage"]


def run():
    global similarity_functions
    if sys.argv[1] == "--help":
        color_print(__doc__)
    else:
        # try:
        if len(sys.argv) < 3:
            raise CustomError("Script does not have enough arguments. Run `python main.py --help` for help")
        input_file = sys.argv[1]
        similarity_function = sys.argv[2]
        if similarity_function not in similarity_functions:
            raise CustomError(f"Second argument should be one of the following: {', '.join(similarity_functions)}")
        all_solutions = False
        try:
            if sys.argv[3] == "--all-solutions":
                all_solutions = True
        except IndexError:
            pass
        prepare_clustering(input_file, similarity_function, all_solutions)
        # except CustomError as e:
        #     error_print(f"Error: {e}")
        # except Exception as e:
        #     error_print(f"Other error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        error_print("Run the program as following for help:\npython main.py --help")
    run()
