# Brython LISS

Bliss enables to use [LISS](https://github.com/denis-migdal/LISS) with Brython


Web Components are simple to use... but, due to a multitude of non-intuitives behaviors and rules, **hard to use *correctly***. Most of examples and documentation found on the Internet are **unsafe** (cf [List of issues solved by LISS](#list-of-issues-solved-by-liss)).

**LISS enables you to easily use Web Compoments without worrying about all of that.**

## Install LISS

In order to use BLISS in your project, copy the `/bliss.py` and `/index.js` files into your project.

💡 If you need to rebuild the JS file, use the command: `tsc index.ts --strict --target esnext --module esnext`.

## Basic usage

To create a new components, simply create a class extending `BISS()` and register it using `BISS.define()`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>BLISS example</title>
    <!-- Brython and BLISS scripts -->
    <script src="/brython/www/src/brython.js" defer></script>
    <script src="/index.js" type="module" defer></script>

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

[📖 And a lot more features and examples below.
