# oreiller



```python
from oreiller import Oreiller as orey

w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)] 

img = orey.new("RGB", (w, h)) 
orey.fill(None)
orey.oline(40, 40, w-10, h-10, width=0) # use .line for normal
img.show() 

orey.cleanup()
```

## Changelog

[Emojilog 1.0](https://github.com/Abdur-rahmaanJ/emojilog)

```
0.1.0
🎉 Package skeleton
🎉 Oreiller class
🎉 .line
🎉 .oline
```