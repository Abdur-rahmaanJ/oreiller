from PIL import Image
from PIL import ImageDraw

class Oreiller:
    image = None
    _images = []

    @classmethod
    def open(cls, *args, **kwargs):
        img = Image.open(*args, **kwargs)
        cls._images.append(img)
        return img
    
    @classmethod
    def new(cls, *args, **kwargs):
        img = Image.new(*args, **kwargs)
        cls._images.append(img)
        return img
    
    @classmethod
    def line(cls, *args, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        draw = ImageDraw.Draw(cls.image)
        draw.line(*args, **kwargs)

    @classmethod
    def cleanup(cls):
        for img in cls._images:
            img.close()