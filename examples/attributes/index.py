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