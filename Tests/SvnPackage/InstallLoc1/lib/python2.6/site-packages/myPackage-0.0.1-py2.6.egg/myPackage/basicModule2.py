
import os
import sys
import math

class MyStrings:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def append_to_end(self,s3=""):
        return self.s1 + self.s2 + s3

    def append_to_start(self,s3=""):
        return s3 + self.s1 + self.s2


