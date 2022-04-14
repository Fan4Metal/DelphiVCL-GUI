import os
from delphivcl import *
from kinopoisk.movie import Movie

class Form1(Form):

    def __init__(self, owner):
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "KinolistGUI.pydfm"))
        self.Label1 = Label(self)
        self.Label1.Caption = ""
        self.Edit1 = Edit(self)
        self.Button1 = Button(self)
        self.Button1.OnClick = self.button1_click
        self.ListBox1 = ListBox(self)
        self.Button2 = Button(self)
        self.Button2.OnClick = self.button2_click
        self.Button3 = Button(self)
        self.Button4 = Button(self)
        self.Button5 = Button(self)
        self.Button6 = Button(self)
        
        
    def button1_click(self, Sender):
        search = self.Edit1.Text
        movie_list = Movie.objects.search(search)
        self.Label1.Caption = movie_list[0]


    def button2_click(self, Sender):
        self.ListBox1.Items.Add(self.Label1.Caption)   
    

def main():
    Application.Initialize()
    Application.Title = 'Form1'
    MainForm = Form1(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
