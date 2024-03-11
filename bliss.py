from browser import window
g = globals()
for x in window.Object.getOwnPropertyNames(window):
	if x not in g and not x.startswith("on") and x not in ["print", "opener", "frameElement", "InstallTrigger", "def_value", "print"]:
		g[x] = getattr(window, x, None)


#import LISS;
import BLISS_HELPERS;

def BLISS(attributes = []):
    return buildBlissBase(BLISS_HELPERS.LISS({
         "attributes": attributes
    }));

def buildBlissBase(liss):
    class BlissBase:

        @property
        def content(self):
            return self.LISS.content
        
        @property
        def host(self):
            return self.LISS.host
        
        @property
        def attrs(self):
            return self.LISS.attrs
        
        @property
        def params(self):
            return self.LISS.params
        
        def onAttrChanged(self, name, oldValue, newValue):
            pass

    BlissBase.LISS = liss
    return BlissBase

####

def define(tagname: str, pyclass:any):
    Base = pyclass.LISS

    def pyclass_builder(this):
        return build_PyBlissBase(pyclass, this)

    BLISS_HELPERS.define( tagname, pyclass_builder, Base )


BLISS.define = define

#__all__ = ["BLISS"]

#### PRIVATE ####

def build_PyBlissBase(Klass, liss):
    pybliss_base = Klass.__new__(Klass)
    pybliss_base.LISS = liss
    pybliss_base.__init__()
    return pybliss_base
