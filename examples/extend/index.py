from BLISS import *;

class MyComponent(BLISS(
                            host = HTMLTableRowElement, # the component is a <tr>
                            extends = BLISS.EventTarget,# the component is able to send events.
                            content = "<td>Hello World ;)</td>"
                        )):

    # Initialize your WebComponent
    def __init__(self):

        def click_handler(ev):
            self.dispatchEvent( CustomEvent.new('click', {"details": None}) )
            pass

        self.host.addEventListener('click', click_handler)

# Define your WebComponent
BLISS.define('my-component', MyComponent); # define the "my-component" component.


#const component = await LISS.qs(...);
elem = document.querySelector('tr[is="my-component"]');

async def main():
    component = await BLISS.getBLISS( elem )

    def click_handler(ev):
        alert('click')
    
    component.addEventListener('click', click_handler);

BLISS.run( main )