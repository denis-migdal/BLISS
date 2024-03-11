declare var __BRYTHON__: any;
const $B = __BRYTHON__;

import LISS from "./LISS/index.js";

__BRYTHON__.imported.LISS = LISS;
__BRYTHON__.imported.BLISS_HELPERS = {
    run: function(e) { e() },
    LISS: function(opts: any){ // dunno why required...
        return LISS(opts);
    },
    define: function(tagname: string, pyclass_builder:(a:any) => any, Base: ReturnType<typeof LISS>) {
        
        class LISSBaseForBLISS extends Base {

            //TODO use symbol...
            readonly pyobj: any;
       
            constructor() {
                super();

                this.pyobj = pyclass_builder(this);
       
                /*const _b_ = $B.builtins;
                const pyobj = $B.$call($B.$getattr(_b_.object, '__new__'), [4,4,21])(pyclass)
                $B.$setattr(pyobj, "LISS", $B.jsobj2pyobj(this)); // is jsobj2pyobj required ?
                $B.$call($B.$getattr(pyobj, '__init__'), [0,0,12])();*/
       
            }

            protected override onAttrChanged(name: string, oldValue: string, newValue: string) {
                $B.$call($B.$getattr(this.pyobj, 'onAttrChanged'), [4,4,21])(name, oldValue, newValue);
            }
        }
        LISS.define(tagname, LISSBaseForBLISS );
    },
};

// fetch and execute brython script.
const CURRENT_SCRIPT_URL = import.meta.url;
const BRYTHON_SCRIPT_URL = CURRENT_SCRIPT_URL.slice(0, CURRENT_SCRIPT_URL.lastIndexOf("/") ) + "/bliss.py";
const BRYTHON_SCRIPT = await (await fetch(BRYTHON_SCRIPT_URL)).text();

__BRYTHON__.runPythonSource(BRYTHON_SCRIPT, "BLISS");