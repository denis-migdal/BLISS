from BLISS import *;

CSS_RULES = """
    :host {
        color: blue;
    }
"""

class MyComponent(BLISS(
                           content=  fetch("./component.html"),		      # str|Response|HTMLTemplateElement or a Promise of it.
                           css    = [fetch('./component.css'), CSS_RULES] # str|Response|HTMLStyleElement|CSSStyleSheet or a Promise of it, or an array of it.
                        )):
    pass

# Define your WebComponent
BLISS.define('my-component', MyComponent); # define the "my-component" component.