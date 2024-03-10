import BLISS

class X( BLISS() ):
    def __init__(self):
        self.bliss_init();
        self.content.append("Hello ;)")
        pass

BLISS.test("hello-world", X)