from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty
from functools import partial
import kivy.uix.button as kb
import numpy as np
from patterns import patterns
from hopfield import Train, Correct

Window.clearcolor = (.6, .6, .6, 1)
Window.set_system_cursor('hand')

class Grid(Widget):
  def __init__(self, **kwargs):
    super(Grid, self).__init__(**kwargs)
    self.weights = Train(patterns)
    self.Clear()
    self.InitNumbersGrid()
    
  def InitNumbersGrid(self):
    grid = self.children[0].children[1]
    for i in range(self.matrix.shape[0] * self.matrix.shape[1]):
      btn = kb.Button(background_normal='', background_color='white')
      btn.bind(on_press=partial(self.ButtonClicked, i))
      grid.add_widget(btn)

  def AdjustGrid(self):
    buttons = self.children[0].children[1].children
    matrixFlatten = self.matrix.flatten()
    for buttonIdx in range(len(matrixFlatten)):
      if matrixFlatten[buttonIdx]:
        buttons[buttonIdx].background_color = 'black'
      else:
        buttons[buttonIdx].background_color = 'white'
  
  def ButtonClicked(self, idx, instance):
    y = idx // self.matrix.shape[1]
    x = idx % self.matrix.shape[1]
    self.matrix[y,x] = 1 - self.matrix[y,x]
    if self.matrix[y,x]:
      instance.background_color = 'black'
    else:
      instance.background_color = 'white'

  def Correct(self):
    self.matrix = Correct(self.weights, self.matrix)
    self.AdjustGrid()

  def Reverse(self):
    self.matrix = np.where(self.matrix, 0, 1)
    self.AdjustGrid()

  def Clear(self):
    buttons = self.children[0].children[1].children
    for button in buttons:
      button.background_color = 'white'

    self.matrix = np.array([
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]
    ])

class ImageCorrectorApp(App):
  title = 'Image corrector'

  def build(self):
    return Grid()

if __name__ == "__main__":
  ImageCorrectorApp().run()
