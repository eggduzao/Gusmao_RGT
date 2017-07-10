
import os
import sys
sys.path.append(os.path.abspath("/".join(os.path.realpath(__file__).split("/")[:-2])))
from myMath import *

def main():
    print sys.argv[1], sys.argv[2]
    v = mathModule.add(3, 7)
    print "The result of 3 and 7 is "+str(v)

if __name__ == '__main__':
    main()


