from oreiller import Oreiller as orey

w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)] 

img = orey.new("RGB", (w, h)) 
orey.fill(None)
orey.oline(40, 40, w-10, h-10, width=0) 
img.show() 

orey.cleanup()