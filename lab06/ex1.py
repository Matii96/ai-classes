from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty
from functools import partial
import kivy.uix.button as kb
import numpy as np
from classify import Classify

Window.clearcolor = (.6, .6, .6, 1)
Window.set_system_cursor('hand')

class Grid(Widget):
  detection = StringProperty()

  def __init__(self, **kwargs):
    super(Grid, self).__init__(**kwargs)
    self.Clear()
    self.InitNumbersGrid()
    
  def InitNumbersGrid(self):
    grid = self.children[0].children[2]
    for i in range(self.matrix.shape[0] * self.matrix.shape[1]):
      btn = kb.Button(background_normal='', background_color='white')
      btn.bind(on_press=partial(self.ButtonClicked, i))
      grid.add_widget(btn)
  
  def ButtonClicked(self, idx, instance):
    y = idx // self.matrix.shape[1]
    x = idx % self.matrix.shape[1]
    self.matrix[y,x] = 1 - self.matrix[y,x]
    if self.matrix[y,x] == 0:
      instance.background_color = 'white'
    else:
      instance.background_color = 'black'

  def Classify(self):
    detection = Classify(self.matrix)
    self.detection = str(detection or '?')

  def Clear(self):
    buttons = self.children[0].children[2].children
    for button in buttons:
      button.background_color = 'white'

    self.matrix = np.array([
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]
    ])
    self.detection = '?'

class NumberClassifierApp(App):
  title = 'Number classifier'

  def build(self):
    return Grid()


if __name__ == "__main__":
  NumberClassifierApp().run()
