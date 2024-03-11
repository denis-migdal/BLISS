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


#const component = await LISS.qs(...);
elem = document.querySelector('tr[is="my-component"]');

async def main():
    component = await BLISS.getBLISS( elem )
    #component.addEventListener('click', () => {
    #    alert('click');
    #});

BLISS.run( main )

