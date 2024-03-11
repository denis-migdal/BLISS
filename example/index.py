from BLISS import *;

class X( BLISS() ):

    def __init__(self):
        self.content.append("Hello world ;)")

BLISS.test("hello-world", X)