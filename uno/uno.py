"""
    uno.py
    (c) David Merrell 2024
    merrell@broadinstitute.org

    TODO description
"""

import argparse



def uno_script():

    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="TODO")
    parser.add_argument("out_file", help="")
    parser.add_argument("--option1", default=None, help="")
    parser.add_argument("--option2", nargs="+", help="") 

    args = parser.parse_args()



if __name__=="__main__":

    uno_script()


