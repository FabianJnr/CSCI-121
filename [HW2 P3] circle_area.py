from math import pi
from math import ceil
def circle_area(radius):
    area = (pi * ((radius)**2))
    rounded_area = ceil(area)
    return(rounded_area)