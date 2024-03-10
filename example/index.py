import BLISS

class X( BLISS() ):

    def __init__(self):
        self.content.append("Hello ;)")

BLISS.test("hello-world", X)