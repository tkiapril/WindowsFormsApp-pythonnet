""":mod:`WindowsFormsApp.MainForm` --- MainForm main file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
# python stdlib imports

# python otherlib imports (clr(pythonnet) on the end)
import clr

# .Net imports
from System.Windows.Forms import AutoScaleMode, Form

# project imports
from .MainFormDesigner import MainFormDesigner

class MainForm(MainFormDesigner):
    def __init__(self):
        self.__InitializeComponent()
