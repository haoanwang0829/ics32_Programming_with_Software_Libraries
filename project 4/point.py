class Point:
    def __init__(self, frac_x: float, frac_y:float):
        self._frac_x = frac_x
        self._frac_y = frac_y
    
    def frac(self) -> (float,float):
        return (self._frac_x, self._frac_y)

    def pixel(self, pixel_width: float, pixel_height: float)-> (float,float):
        pixel_x = pixel_width * self._frac_x
        pixel_y = pixel_height * self._frac_y
        return (pixel_x,pixel_y)

def from_frac(frac_x:float, frac_y:float)-> Point:
    return Point(frac_x,frac_y)

def from_pixel(pixel_x: float, pixel_y:float,
               pixel_width: float, pixel_height:float) -> Point:
    frac_x = pixel_x/pixel_width
    frac_y = pixel_y/pixel_height
    return Point(frac_x, frac_y)
