from PIL import Image
from PIL import ImageDraw

class Oreiller:
    image = None

    @classmethod
    def open(cls, *args, **kwargs):
        return Image.open(*args, **kwargs)
    
    @classmethod
    def new(cls, *args, **kwargs):
        return Image.new(*args, **kwargs)
    
    @classmethod
    def line(cls, *args, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        draw = ImageDraw.Draw(cls.image)
        draw.line(*args, **kwargs)

    