from PIL import Image

class Oreiller:

    @classmethod
    def open(cls, *args, **kwargs):
        return Image.open(*args, **kwargs)