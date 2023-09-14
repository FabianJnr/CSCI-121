from math import sqrt
def distance(x1, y1, x2, y2):
    cal_distance = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return(cal_distance)