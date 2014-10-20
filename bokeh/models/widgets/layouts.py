from __future__ import absolute_import

from ...properties import Int, Instance, List
from ..widget import Widget

class Layout(Widget):
    width = Int
    height = Int

class HBox(Layout):
    children = List(Instance(Widget))
class VBox(Layout):
    children = List(Instance(Widget))

#parent class only, you need to set the fields you want
class VBoxForm(VBox):
    pass
