from BLISS import *;

class MyComponent(BLISS()):

    # Initialize your WebComponent
    def __init__(self):

        # Use self.content to initialize your component's content
        self.content.append('Hello World ;)');

        console.log('State (initial)', {
            # Use self.content to access your component's content:
            "Content"   : self.content, # ShadowRoot
            # Use self.host to access the component's host:
            "Host"      : self.host,    # <my-component></my-component>
            # Use self.attrs to efficiently access the component's host's attributes:
            "Attributes": self.attrs, # {}
            # Use self.params to access the component parameters.
            "Parameters": self.params      # {}
        });

# Define your WebComponent
BLISS.define('my-component', MyComponent); # define the "my-component" component.