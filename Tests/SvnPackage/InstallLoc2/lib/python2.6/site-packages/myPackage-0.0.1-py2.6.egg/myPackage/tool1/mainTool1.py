
import os
import sys

import auxTool1

from pkg_resources import Requirement, resource_filename

def main():

    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    print auxTool1.superSum(n1,n2)

    filename = resource_filename(Requirement.parse("myPackage"),"sample.conf")
    #print filename


