import os
from delphivcl import *
from kinopoisk.movie import Movie

class Form3(Form):

    def __init__(self, owner):
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "KinolistGUI.pydfm"))
        self.Caption = "Поиск фильмов"
        self.Label1 = Label(self)
        self.Label1.Caption = "Поиск"
        self.Label2 = Label(self)
        self.Label2.Caption = "Результат"
                
        self.Edit1 = Edit(self)
        self.Edit1.Text = ""
        self.Edit2 = Edit(self)
        self.Edit2. Text = ""
        self.Button1 = Button(self)
        self.Button1.Caption = "Поиск"
        self.Button1.OnClick = self.button1_click
        
        self.Button2 = Button(self)
        self.Button1.Caption = "Сохранить   "
        # self.Button1.OnClick = self.button2_click
        
        self.ListBox1 = ListBox(self)
        self.Button3 = Button(self)
        self.Image1 = Picture(self)

    def button1_click(self, Sender):
        search = self.Edit1.Text
        movie_list = Movie.objects.search(search)
        self.Edit2.Text = movie_list[0]
        # print(type(movie_list))
    
    # def button2_click(self, Sender):
    #     self.ListBox1.
        


def main():
    Application.Initialize()
    Application.Title = 'Form3'
    MainForm = Form3(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
