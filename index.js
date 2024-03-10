import LISS, { __set_cstr_host } from "./LISS/index.js";
function BLISS() {
    return class PyLISSBase {
        static __Liss = LISS();
        __liss;
        bliss_init() {
            this.__liss = new PyLISSBase.__Liss();
        }
        get content() {
            return this.__liss.content;
        }
    };
}
//TODO: auto add LISS fcts...
BLISS.define = function define(tagname, klass, opts) {
    return LISS.define(tagname, klass, opts);
};
//TODO: transform as define...
BLISS.test = function test(tagname, pyclass) {
    try {
        const Base = pyclass.$js_func.__Liss;
        //TODO: class ensure unicity...
        class PyClass extends Base {
            //TODO use symbol...
            pyobj;
            constructor() {
                super();
                __set_cstr_host(this.host);
                this.pyobj = __BRYTHON__.$call(pyclass, [0, 1, 1])();
            }
        }
        LISS.define(tagname, PyClass);
    }
    catch (e) {
        console.log(e);
    }
};
__BRYTHON__.imported.BLISS = __BRYTHON__.jsobj2pyobj(BLISS);
