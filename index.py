from tkinter import * #importa todos os módulos do tkinter
from tkinter import messagebox #importa o módulo de caixas de mensagem
from tkinter import ttk #importa o módulo de widgets
from DataBase import DataBase #importa a classe de módulos DataBase

#CRIAR JANELA
jan = Tk() #Cria uma instância da janela principal
jan.title('SL Systes - Painel de Acesso') #Define o título da janela
jan.geometry('600x300') #Define o tamanho da janela
jan.configure(background='white')
jan.resizable(width=False, height=False) #importa a redimencionalização da janela
jan.attributes('-alpha', 0.9) # define a tranparencia da janela (0.0 a 1.0)
jan.iconbitmap(default='icon/ilogoIcon.ico') #define o icone da janela
logo = PhotoImage(file='icons/LogoMatheusEduardo.png') #carrega a imagem no logo

#criar frame
Leftframe = Frame(jan, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise') #cria um frame a esquerda
Leftframe.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise') # cria um a direita
RightFrame.pack(side=RIGHT)

#adicionar logo
LogoLabel = Label(Leftframe, image=logo,bg='MIDNIGHTBLUE') # cria um label para a logo
LogoLabel.place(x=50,y=100)

#campos de usuario e senha
UsuarioLabel = Label(RightFrame,text='Usuario: ',font=(cenrury))