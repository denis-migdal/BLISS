# Brython LISS

Bliss enables to use [LISS](https://github.com/denis-migdal/LISS) with Brython


Web Components are simple to use... but, due to a multitude of non-intuitives behaviors and rules, **hard to use *correctly***. Most of examples and documentation found on the Internet are **unsafe** (cf [List of issues solved by LISS](https://github.com/denis-migdal/LISS#list-of-issues-solved-by-liss)).

**LISS enables you to easily use Web Components without worrying about all of that.**

## Install LISS

In order to use BLISS in your project, copy the `BLISS/bliss.py` and `BLISS/index.js` files into your project.

💡 If you need to rebuild the JS file, use the command: `tsc index.ts --strict --target esnext --module esnext`.

## Basic usage

To create a new components, simply create a class extending `BISS()` and register it using `BISS.define()`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>BLISS example</title>
    <!-- Brython and BLISS scripts -->
    <script src="$BRYTHON" defer></script>
    <script src="$BLISS" type="module" defer></script>

    <!-- your script -->
    <script type="text/python" src="./index.py"></script>
  </head>
  <body>
    <my-component></my-component> <!-- Prints "Hello World ;)" -->
  </body>
</html>
```

```python
from BLISS import *;

class MyComponent(BLISS()):

    # Initialize your WebComponent
    def __init__(self):
        super();

        # Use this.content to initialize your component's content
        self.content.append('Hello World ;)');

        console.log('State (initial)', {
            # Use this.content to access your component's content:
            "Content"   : self.content, # ShadowRoot
            # Use this.host to access the component's host:
            "Host"      : self.host,    # <my-component></my-component>
            # Use this.attrs to efficiently access the component's host's attributes:
            "Attributes": self.attrs, # {}
            # Use this.params to access the component parameters.
            "Parameters": self.params      # {}
        });

# Define your WebComponent
BLISS.define('my-component', MyComponent); # define the "my-component" component.
```

[📖 See the auto mode for easier usage.](#auto-mode)

[📖 And a lot more features and examples below.](#features-and-examples)

## Features and examples

You can see all examples below in the [`BLISS/examples/` directory](./examples/).

- [Management of HTML attributes](#manage-html-attributes)
- [Extend Brython and HTML classes](#extend-brython-and-html-classes)
- [Dynamically build component instances](#dynamically-build-component-instances)
- [Access components through the DOM](#access-components-through-the-dom)
- [Use HTML/CSS files/strings to fill the component](#use-htmlcss-filesstrings-to-fill-the-component)
- [Auto mode](#auto-mode)
- **Advanced features**
  - [ShadowRoot helpers](#shadowroot-helpers)
  - dependancies / async constructor
- **[LISS full API](#liss-full-API)**

### Manage HTML attributes

BLISS enables to observe the host HTML attributes, simply by specifying their names when building the component (`extends BLISS(attributes =[...])`).

Then, `self.onAttrChanged()` will be called at each modification of the observed attributes. If `self.onAttrChanged()` returns False, the changed attribute will be reverted to its previous value.

`self.attrs` enables to access them in an efficient way, i.e. without requiring multiples access to the DOM. Modification of an attribute through `self.attrs` will update the HTML attributes without firing `self.onAttrChanged()`.

```python
# cf /examples/attributes
from BLISS import *;

class MyComponent(BLISS(
                            attributes = ["counter"] # observed attributes.
                        )):

    __interval = None;

    # Initialize your WebComponent
    def __init__(self):

        # self.attrs contains the current values of the observed attributes.
        console.log("Attributes (initial)", self.attrs);

        def update_counter():
            self.host.setAttribute("counter", int(self.attrs.counter)+1); # will trigger onAttrChanged

        self.__interval = setInterval( update_counter, 1000); # setInterval...

        self.content.textContent = self.attrs.counter = 0; # will NOT trigger onAttrChanged.

    def onAttrChanged(self, name, oldValue, newValue):

        console.log("AttrChanged", name, oldValue, "->", newValue);
        console.log("Attributes (now):", self.attrs);

        # you can validate self.attrs here.
        if self.attrs.counter == "5":
            clearInterval(self.__interval);
            return False; # cancel the change.

        self.content.textContent += self.attrs.counter;

# Define your WebComponent
BLISS.define('my-component', MyComponent); # define the "my-component" component.
```

```html
<my-component counter="null"></my-component><!-- prints 01234 -->
```

### Extend Brython and HTML classes

`BLISS()` allows you to extends existing classes thanks to the `extends` (Brython classes) and `host` (HTMLElement classes) options.

```python
# cf /examples/extend
from BLISS import *;

class MyComponent(BLISS(
                            host = HTMLTableRowElement, # the component is a <tr>
                            #TODO: make BRYTHON class for that... (extending JS class is an issue)
                            #extends = EventTarget,      # the component is able to send events.
                            content = "<td>Hello World ;)</td>"
                        )):

    # Initialize your WebComponent
    def __init__(self):
        pass
        #this.host.addEventListener('click', () => {
        #    this.dispatchEvent(new CustomEvent('click', {detail: null}));
        #})

# Define your WebComponent
BLISS.define('my-component', MyComponent); # define the "my-component" component.

#const component = await LISS.qs('tr[is="my-component"]');

#component.addEventListener('click', () => {
#    alert('click');
#});
```

```html
<table>
    <tr is="my-component"></tr>
</table>
```
### Dynamically build component instances

<mark>TODO</mark>

### Access components through the DOM

<mark>TODO</mark>

### Use HTML/CSS files/strings to fill the component

`BLISS()` allows to inject HTML and CSS files/strings into your component thanks to the `content` and `css` options:

```python
# cf /examples/inject-html-css/
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
```

### Auto mode

<mark>TODO</mark>

### ShadowRoot helpers

<mark>TODO</mark>

### BLISS full API

## TODO

- [ ] Access components through the DOM

- [ ] Use HTML/CSS files/strings to fill the component

- [ ] EventTarget for Brython

- [ ] TODO auto mode



- [ ] Dynamically build component instances

- [ ] ShadowRoot helpers

- [ ] BLISS full API

- [ ] Doc for onDOM(dis)connected