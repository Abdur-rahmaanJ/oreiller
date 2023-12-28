
try:
    from PIL import Image
    from PIL import ImageDraw
    from pilmoji import Pilmoji
except ImportError:
    pass

class Oreiller:
    image = None
    _images = []
    _fill = None
    _font = None

    @classmethod
    def open(cls, *args, **kwargs):
        img = Image.open(*args, **kwargs)
        cls._images.append(img)
        return img
    
    @classmethod
    def new(cls, *args, **kwargs):
        img = Image.new(*args, **kwargs)
        cls._images.append(img)
        cls.image = img
        return img
    
    @classmethod
    def font(cls, font):
        cls.font = font
    
    @classmethod
    def fill(cls, fillval):
        cls._fill = fillval
    
    @classmethod
    def line(cls, *args, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        draw = ImageDraw.Draw(cls.image)
        draw.line(*args, **kwargs)


    @classmethod
    def oline(cls, x1, y1, x2, y2, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        draw = ImageDraw.Draw(cls.image)
        shape = [(x1, y1), (x2, y2)]
        draw.line(shape, fill=cls._fill, **kwargs)

    @classmethod
    def otext(cls, x, y, text, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        with Pilmoji(cls.image) as pilmoji:
            pilmoji.text((x, y), text, cls._fill, cls._font, **kwargs)

    @classmethod
    def arc(cls, *args, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        img1 = ImageDraw.Draw(cls.image)   
        img1.arc(*args, **kwargs) 

    @classmethod
    def oarc(cls, x1, y1, x2, y2, start, end, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        img1 = ImageDraw.Draw(cls.image) 
        shape = [(x1, y1), (x2, y2)] 
        img1.arc(shape, start, end, **kwargs) 


    @classmethod
    def chord(cls, *args, **kwargs):
        if cls.image is None:
            raise Exception('Please open or set an image')
        img1 = ImageDraw.Draw(cls.image)   
        img1.chord(*args, **kwargs) 

    @classmethod
    def cleanup(cls):
        for img in cls._images:
            try:
                img.close()
            except Exception as e:
                print(e)