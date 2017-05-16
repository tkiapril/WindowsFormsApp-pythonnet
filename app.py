""":mod:`app` --- the executable app entry script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
# python stdlib imports

# python otherlib imports (clr(pythonnet) on the end)
import clr

# .Net imports
from System.Threading import Thread, ThreadStart, ApartmentState

# project imports
from WindowsFormsApp import Program

if __name__ == '__main__':
    thread = Thread(ThreadStart(Program.Main))

    # [STAThread] attribute is set here
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()

    # fall into ui loop
    thread.Join()
