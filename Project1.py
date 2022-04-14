from delphivcl import *
from KinolistGUI import Form1

def main():
    Application.Initialize()
    Application.Title = 'KinolistGUI'
    MainForm = Form1(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
