import LISS;
import BLISS_HELPERS;

def BLISS():
    return buildBlissBase(LISS());

def buildBlissBase(liss):
    class BlissBase:
        @property
        def content(self):
            return self.LISS.content

    BlissBase.LISS = liss
    return BlissBase

####

def test(tagname: str, pyclass:any):
    Base = pyclass.LISS

    def pyclass_builder(this):
        build_PyBlissBase(pyclass, this)

    BLISS_HELPERS.define( tagname, pyclass_builder, Base )


BLISS.test = test

#__all__ = ["BLISS"]

#### PRIVATE ####

def build_PyBlissBase(Klass, liss):
    pybliss_base = Klass.__new__(Klass)
    pybliss_base.LISS = liss
    pybliss_base.__init__()
    return pybliss_base
