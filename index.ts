declare var __BRYTHON__: any;
const $B = __BRYTHON__;

import LISS from "./LISS/index.js";

const PyBLISS = __BRYTHON__.runPythonSource(`
def buildBlissBase(liss):
    class BlissBase:
        @property
        def content(self):
            return self.LISS.content

    BlissBase.LISS = liss
    return BlissBase

def build_PyBlissBase(Klass, liss):
    pybliss_base = Klass.__new__(Klass)
    pybliss_base.LISS = liss
    pybliss_base.__init__()
    return pybliss_base

`, "BLISS");

const buildBlissBase = PyBLISS.buildBlissBase

function BLISS() {

    //TODO: LISSOpts...
    return buildBlissBase(LISS());
}

//TODO: AutoLISS
//TODO: Bliss function : use python definitions when possible...
BLISS.define = function define(tagname: string, klass: any, opts: any) {
    return LISS.define(tagname, klass, opts);
}

function buildLISSBaseForBLISS(pyclass: any) {
 
    //TODO: class ensure unicity...
    const Base = $B.$getattr(pyclass, "LISS") as ReturnType<typeof LISS>;
    
    return class LISSBaseForBLISS extends Base {

     //TODO use symbol...
     pyobj: any;

     constructor() {
         super();

         PyBLISS.build_PyBlissBase(pyclass, this);

         /*const _b_ = $B.builtins;
         const pyobj = $B.$call($B.$getattr(_b_.object, '__new__'), [4,4,21])(pyclass)
         $B.$setattr(pyobj, "LISS", $B.jsobj2pyobj(this)); // is jsobj2pyobj required ?
         $B.$call($B.$getattr(pyobj, '__init__'), [0,0,12])();*/

     }
 }
}

//TODO: transform as define...
BLISS.test = function test(tagname: string, pyclass:any) {

    LISS.define(tagname, buildLISSBaseForBLISS(pyclass) );
};

__BRYTHON__.imported.BLISS = __BRYTHON__.jsobj2pyobj(BLISS);