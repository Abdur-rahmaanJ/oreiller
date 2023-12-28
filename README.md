# oreiller

The package for easy image manipulation backed by pillow power. 

The package for clean Pillow codebases.

```python
from oreiller import Oreiller as orey

w, h = 220, 190

img = orey.new("RGB", (w, h)) 
orey.fill(None)
orey.oline(40, 40, w-10, h-10, width=0) # use .line for normal
img.show() 

orey.cleanup()
```

## Docs

### .new

Returns Image.new 


### .fill

Modifies fill value

### .line

Draws line without the need of ImageDraw

### .oline

Processing api of line(x1, y1, x2, y2)

### .otext

- x
- y
- text
- pilmoji keyword arguments

### .font

- font(ImageDraw.font(...))

### .arc 

- args same as pillow args

### .oarc

- x1
- y1
- x2
- y2
- Keyword arguments same as pillow

### .chord 

- args same as pillow args

### .ochord

- x1
- y1
- x2
- y2
- Keyword arguments same as pillow

## Changelog

[Emojilog 1.0](https://github.com/Abdur-rahmaanJ/emojilog)

```
latest
🎉 .otext
🎉 .font
🎉 .arc
🎉 .oarc
🎉 .chord
🎉 .ochord

0.1.0
🎉 Package skeleton
🎉 Oreiller class
🎉 .line
🎉 .oline
🔧 Fix cleanup: inform when closing closed images
```
