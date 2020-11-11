from absl import app, flags
from absl.flags import FLAGS
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi, sin, cos
import numpy as np
from fuzzy_controller import fuzzy_controller

flags.DEFINE_integer('step', 5, 'car step')

path = [[-100, -50, 0]]
current_position = None

def animate(frame_idx):
  global current_position
  if current_position:
    current_position.remove()
  x, y, angle = path[frame_idx][0], path[frame_idx][1], path[frame_idx][2]

  arrow_direction = (cos(angle * pi / 180), sin(angle * pi / 180))
  current_position = plt.arrow(x, y, arrow_direction[0], arrow_direction[1], width=2, color='green', label='Car')

  plt.legend(loc='upper right')
  plt.title('Step {}'.format(frame_idx + 1))

def main(_argv):
  # Simulate driving
  global path
  while not (path[-1][0] >= -30 and path[-1][0] <= 30 and path[-1][1] >= -10 and path[-1][1] <= 0):
    # Get new angle from controller
    next_angle = fuzzy_controller(path[-1][0], path[-1][1], path[-1][2])

    # Calculate new coordinates
    new_x = path[-1][0] + FLAGS.step * cos(next_angle * pi / 180)
    new_y = path[-1][1] + FLAGS.step * sin(next_angle * pi / 180)

    path.append([new_x, new_y, next_angle])
    print('Step: ({:.2f},{:.2f}), {:.2f}'.format(new_x, new_y, next_angle))

  plt.axes().set_aspect('equal')
  plt.axis([-100, 100, -100, 0])
  plt.grid(True)

  # # Draw ramp
  plt.plot([-30, -30], [0, -10], linestyle='--', color='orange', linewidth=2)
  plt.plot([-30, 30], [-10, -10], linestyle='--', color='orange', linewidth=2)
  plt.plot([30, 30], [0, -10], linestyle='--', color='orange', linewidth=2, label='Ramp')

  fig = plt.figure(1)
  plt.legend(loc='upper right')
  anim = animation.FuncAnimation(fig, animate, frames=len(path), repeat=False, interval=250)
  plt.show()

if __name__ == '__main__':
  app.run(main)
