from rule import Rule

rules = [
  Rule(x=-75, y=-50, angle=0, result_angle=0),
  Rule(x=-60, y=-50, angle=0, result_angle=0),
  Rule(x=-50, y=-50, angle=0, result_angle=0),
  Rule(x=-40, y=-50, angle=0, result_angle=0),
  Rule(x=-20, y=-40, angle=10, result_angle=40),
  Rule(x=-10, y=-35, angle=40, result_angle=50, imprecision=20),
  Rule(x=-5, y=-31, angle=50, result_angle=65, imprecision=15),
  Rule(x=0, y=-30, angle=80, result_angle=90, imprecision=15),
  Rule(x=0, y=0, angle=0, result_angle=90)
]
