import os
from delphivcl import *

class Form3(Form):

    def __init__(self, owner):
        self.Label1 = None
        self.Label2 = None
        self.Edit1 = None
        self.Edit2 = None
        self.Button1 = None
        self.Button2 = None
        self.ListBox1 = None
        self.Button3 = None
        self.Image1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Unit3.pydfm"))

def main():
    Application.Initialize()
    Application.Title = 'Form3'
    MainForm = Form3(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
