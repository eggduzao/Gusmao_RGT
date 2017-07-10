import os
import sys
import auxTool1
from numpy import array
from optparse import OptionParser,BadOptionError,AmbiguousOptionError
from pkg_resources import Requirement, resource_filename

"""
%usage Teste
"""
class PassThroughOptionParser(OptionParser):
    """
    An unknown option pass-through implementation of OptionParser.
    When unknown arguments are encountered, bundle with largs and try again,
    until rargs is depleted.
    sys.exit(status) will still be called if a known argument is passed
    incorrectly (e.g. missing arguments or bad argument types, etc.)
    """
    def _process_args(self, largs, rargs, values):
        while rargs:
            try:
                OptionParser._process_args(self,largs,rargs,values)
            except (BadOptionError,AmbiguousOptionError), e:
                largs.append(e.opt_str)


class MyObject():

    def __init__(self,att1,att2):
        self.att1 = att1
        self.att2 = att2

class Cons:
    class C1:
        TESTE1 = 0
        TESTE2 = 1

    def __init__(self):
        a = ""
        print self.C1.TESTE2

    def aa(self,tt=C1.TESTE1):
        print tt
        print C1.TESTE2

def main():
    """
    %usage teste
    """

    test = Cons.C1.TESTE1
    print test

    c = Cons()
    c.aa()

    """
    o1 = MyObject(1,"teste1")
    o2 = MyObject(2,"teste2")
    o3 = MyObject(1,"teste3")
    o4 = MyObject(2,"teste4")
    o5 = MyObject(1,"teste5")

    my_list = [o1,o2,o3,o4,o5]
    my_list = array(my_list)

    for e in my_list: print e.att2



    parser = PassThroughOptionParser(usage="%prog [lalala]", version="%prog 1.0")


    parser.add_option("--numberone", type="int", metavar="INT",
                  help="The first number",
                  dest="n1", default=5)

    parser.add_option("--numbertwo", type="int",
                  help="The second number", 
                  dest="n2")
    
    options, arguments = parser.parse_args()


    print type(options)
    print arguments
    print auxTool1.superSum(options.n1,options.n2)

    print os.getenv("USER")
    print os.getenv("SUDO_USER")

    #myDir = os.path.join("~","AAA/BBB/CCC"+str(auxTool1.superSum(options.n1,options.n2)))
    #print myDir, os.path.exists(myDir)
    #if not os.path.exists(myDir): os.makedirs(myDir)

    #for r,d,f in os.walk("/home/egg/Projects/TfbsPrediction/Tests/SvnPackage/eduardogadeproject/data"):
    #    print r
    #    print d
    #    print f
    #    print "---------------------------------------------"

    filename = resource_filename(Requirement.parse("myPackage"),"sample.conf")
    print filename
    """


