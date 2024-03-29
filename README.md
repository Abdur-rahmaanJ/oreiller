
<p align="center">
  <br>
  <a href="https://github.com/Abdur-rahmaanJ/oreiller">
    <img src="https://github.com/Abdur-rahmaanJ/oreiller/blob/stable/logo.png?raw=true" alt="Oreiller" width=300px></a>
  <br>
</p>

# oreiller

The package for easy image manipulation backed by pillow power. 

The package for clean Pillow codebases.

Oreiller means a pillow in french.

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

Methods prefixed by o is inspired by the [processing API](https://processing.org/reference).

### .new

Returns Image.new 


### .fill

Modifies fill value. Impacts all functions. No need to re-specify fill=

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
- start
- end
- Keyword arguments same as pillow

### .chord 

- args same as pillow args

### .ochord

- x1
- y1
- x2
- y2
- start
- end
- Keyword arguments same as pillow

### .rectangle

- args same as pillow args

### .orect

- x1
- y1
- x2
- y2
- Keyword arguments same as pillow

### .ellipse

- args same as pillow args

### .oellipse

- x1
- y1
- x2
- y2
- Keyword arguments same as pillow

### .rectangle

- args same as pillow args

### .orounded_rect

- x1
- y1
- x2
- y2
- radius
- Keyword arguments same as pillow

### .polygon 

- args same as pillow args

## Changelog

[Emojilog 1.0](https://github.com/Abdur-rahmaanJ/emojilog)

```
0.2.0
🎉 .otext
🎉 .font
🎉 .arc
🎉 .oarc
🎉 .chord
🎉 .ochord
🎉 .polygon
🎉 .fill impacts all functions
🎉 .rectangle
🎉 .orect
🎉 .ellipse
🎉 .oellipse
🎉 .rectangle
🎉 .orounded_rect
🔧 Fix otext

0.1.0
🎉 Package skeleton
🎉 Oreiller class
🎉 .line
🎉 .oline
🔧 Fix cleanup: inform when closing closed images
```
