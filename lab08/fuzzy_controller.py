from rules import rules

def fuzzy_controller(x, y, angle):
  result_nominator = 0
  result_denominator = 0

  for rule in rules:
    rule_activation = rule.activation(x, y, angle)
    result_nominator += rule_activation * rule.result_angle
    result_denominator += rule_activation

  try:
    next_angle =  result_nominator / result_denominator
  except:
    raise Exception('Combination {}, {}, {} doesn\'t belong to any rule'.format(x, y, angle))

  # Make sure we're in [-180, 180] degrees range
  return max(min(next_angle, 180), -180)
