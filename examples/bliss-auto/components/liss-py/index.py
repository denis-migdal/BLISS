from BLISS import *;

def BLISSBuilder(options):

	class BLISSComponent(BLISS(**options)):

		def __init__(self):
			
			# do stuff...
			COLORS = ['blue', 'yellow'];
			cidx   = 0;

			self.host.style.setProperty('--color', COLORS[cidx]);

			def handler():
				nonlocal cidx
				cidx += 1
				cidx = cidx % len(COLORS)
				self.host.style.setProperty('--color', COLORS[cidx] );

			setInterval(handler, 1000);

	return BLISSComponent
