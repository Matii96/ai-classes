from math import exp

class Rule:
  def __init__(self, x, y, angle, result_angle, imprecision=40):
    self.x = x
    self.y = y
    self.angle = angle
    self.result_angle = result_angle
    self.imprecision = imprecision

  def gaussian(self, value, center):
    return exp((-(value - center) ** 2) / self.imprecision)

  def activation(self, x, y, angle):
    return self.gaussian(x, self.x) * self.gaussian(y, self.y) * self.gaussian(angle, self.angle)
