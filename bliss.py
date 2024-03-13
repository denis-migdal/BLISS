from browser import window
import javascript

g = globals()
for x in window.Object.getOwnPropertyNames(window):
	if x not in g and not x.startswith("on") and x not in ["print", "opener", "frameElement", "InstallTrigger", "def_value", "print"]:
		g[x] = getattr(window, x, None)


import LISS;
import BLISS_HELPERS;

def BLISS(extends = object, css = javascript.UNDEFINED, content = javascript.UNDEFINED, host = HTMLElement, attributes = []):

    class BlissBase(extends):

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

    BlissBase.LISS = BLISS_HELPERS.LISS({
         "attributes": attributes,
         "host"      : host,
         "content"   : content,
         "css"       : css
    })

    return BlissBase

####

def define(tagname: str, pyclass:any):
    Base = pyclass.LISS

    def pyclass_builder(this):
        return build_PyBlissBase(pyclass, this)

    BLISS_HELPERS.define( tagname, pyclass_builder, Base )

BLISS.define = define

async def getBLISS(elem):
    return (await LISS.getLISS(elem)).pyobj

BLISS.getBLISS = getBLISS


def run(coroutine):
    BLISS_HELPERS.run(coroutine)

BLISS.run = run


class BryEventTarget:
    __eventTarget = EventTarget.new()
    
    def dispatchEvent(self, event ):
        self.__eventTarget.dispatchEvent( event )

    def addEventListener(self, event, listener):
        self.__eventTarget.addEventListener( event, listener )

BLISS.EventTarget = BryEventTarget

#__all__ = ["BLISS"]

#### PRIVATE ####

def build_PyBlissBase(Klass, liss):
    pybliss_base = Klass.__new__(Klass)
    pybliss_base.LISS = liss
    pybliss_base.__init__()
    return pybliss_base

def BLISSAuto_defineWebComponent(tagname, files, opts):

    opts = dict(opts)

    WebComp = None
    if "index.py" in files:
        loc = {}
        exec( files["index.py"], globals(), loc )
        WebComp = loc["BLISSBuilder"](opts)

    elif "index.html" in files:

        class WebComponent( BLISS(**opts) ):
            pass
        WebComp = WebComponent

    if WebComp is not None:
        BLISS.define(tagname, WebComp);
        return

    raise Exception(f"Missing files for WebComponent $tagname.")