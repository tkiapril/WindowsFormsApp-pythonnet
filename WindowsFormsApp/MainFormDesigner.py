""":mod:`WindowsFormsApp.MainFormDesigner` --- MainForm designer file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
# python stdlib imports

# python otherlib imports (clr(pythonnet) on the end)
import clr

# .Net imports
from System.ComponentModel import Container, IContainer
from System.Windows.Forms import AutoScaleMode, Form

# project imports

class MainFormDesigner(Form):
    #: (:class:`System.ComponentModel.IContainer`) Required designer variable.
    __components: IContainer = None

    def Dispose(self, disposing: bool):
        """Clean up any resources being used.

        :param disposing: true if managed resources should be disposed;
                          otherwise, false.

        """
        if disposing and components is not None:
            components.Dispose()
        super().Dispose(disposing)


    def _MainForm__InitializeComponent(self):
        self.__components = Container()
        self.AutoScaleMode = AutoScaleMode.Font
        self.Text = "MainForm"
