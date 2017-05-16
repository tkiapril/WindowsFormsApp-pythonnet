""":mod:`WindowsFormsApp.Program` --- Startup object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
# python stdlib imports

# python otherlib imports (clr(pythonnet) on the end)
import clr

# .Net imports
from System.Windows.Forms import Application

# project imports
from .MainForm import MainForm

class Program:
    def Main():
        """The main entry point for the application."""
        Application.EnableVisualStyles()
        Application.SetCompatibleTextRenderingDefault(False)
        Application.Run(MainForm())
