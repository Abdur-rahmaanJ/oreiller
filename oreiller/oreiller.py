from PIL import Image

class Oreiller:

    @classmethod
    def open(cls, *args, **kwargs):
        return Image.open(*args, **kwargs)
    
    @classmethod
    def new(cls, *args, **kwargs):
        return Image.new(*args, **kwargs)