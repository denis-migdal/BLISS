declare var __BRYTHON__: any;
const $B = __BRYTHON__;

import LISS, {LISS_Auto} from "./LISS/index.js";

__BRYTHON__.imported.LISS = LISS;
__BRYTHON__.imported.BLISS_HELPERS = {
    run: function(e: any) { e() },
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

//const BRYTHON_SCRIPT = await (await fetch(BRYTHON_SCRIPT_URL)).text();
var request = new XMLHttpRequest();
request.open("GET", BRYTHON_SCRIPT_URL, false);
request.send();
const BRYTHON_SCRIPT = request.responseText;


const BLISS = __BRYTHON__.runPythonSource(BRYTHON_SCRIPT, "BLISS");


class BLISS_Auto extends LISS_Auto {

    protected override resources() {
        return [
            "index.py",
            "index.html",
            "index.css"
        ];
    }

    protected override async defineWebComponent(tagname: string, files: Record<string, any>, opts: Partial<{content: string, css: string}>) {
        BLISS.BLISSAuto_defineWebComponent(tagname, files, opts );
	}
}

LISS.define("bliss-auto", BLISS_Auto);