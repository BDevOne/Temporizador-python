from plyer import notification 
from tkinter import messagebox
from tkinter import *
import time

#Atribuir classe e definir dimensões da interface
window = Tk()
window.geometry("300x200")
window.title("Temporizador")

#Função para ativar o cronômetro de contagem regressiva do python e mostrar notificações quando o cronômetro terminar
def timer(): 

    #Como usamos placeholders, verificamos se o usuário digitou um inteiro
    try:
        timer_time = int(hour_entry.get())*3600 + int(min_entry.get())*60 + int(sec_entry.get())
        
    except:
        messagebox.showerror(message="Digite um horário válido")
    #O usuário não pode ativar um timer sem tempo definido
   #Para atualizar o cronômetro a cada segundo decrescente e exibir uma notificação    
    if timer_time >0:
        hour = 0
        min = 0 
        sec = 0    
       #Se minutos for maior que 60, deve ser definido para a próxima hora
        while timer_time >= 0:
            min, sec = divmod(timer_time,60)
            if min > 60:
                hour, min = divmod(min,60) 
            #Defina as variáveis ​​declaradas com os novos valores a serem exibidos                
            hours.set(hour)
            mins.set(min)
            secs.set(sec)
            #Sleep for 1 cria um atraso de 1 segundo
            time.sleep(1)   
            #Atualiza as alterações na janela a cada segundo
            window.update()
            #Diminui o valor do timer em 1
            timer_time -= 1
       #Criar uma notificação na área de trabalho
        notification.notify(
           #Título da notificação,
            title = "TIMER ALERT",
            #Corpo da notificação
            message = "Ei, amigo!\nVocê fez o que queria? \nSe não, tente novamente com um novo timer",
            app_icon = "/home/deepika/Downloads/internship/countdown_timer/pictures/bell.ico",
            #Notificação fica por 30 segundos
            timeout  = 30,
        )
        #Esta notificação é fornecida pelo tkinter com o aplicativo criado
        messagebox.showinfo(message="Seu tempo acabou!!")         
        
#Remova os espaços reservados para cada campo de entrada com base no clique    
def h_click(event):
        hour_entry.delete(0,'end')         
def m_click(event):
        min_entry.delete(0,'end')
def s_click(event):    
        sec_entry.delete(0,'end')
        
#Label para exibir o título do aplicativo
#posição do rótulo ou widget é definida usando pack().
#pack padroniza o alinhamento centralizado na linha ax e na coordenada da coluna y
title_label_1 = Label(window, text="Temporizador/Cronômetro",font=("Gayathri", 11)).pack()
title_label_2 = Label(window, text="Coloque 0 em campos que não são de uso",font=("Gayathri", 10)).pack()
#Variáveis ​​com as quais o timer é atualizado na função
hours = IntVar()
mins = IntVar()
secs = IntVar()

#Para ler a entrada do usuário por horas, minutos e segundos
hour_entry=Entry(window,width=3,textvariable=hours,font=("Ubuntu Mono",18))
min_entry=Entry(window,width=3,textvariable=mins,font=("Ubuntu Mono",18))
sec_entry=Entry(window,width=3,textvariable=secs,font=("Ubuntu Mono",18))

#Espaço reservado para os widgets de entrada
hour_entry.insert(0,00)
min_entry.insert(0,00)
sec_entry.insert(0,00)

#Posicionando os widgets de entrada.
#place() pega uma coordenada x(da esquerda) e y(de cima)
hour_entry.place(x=80,y=40)
min_entry.place(x=130,y=40)
sec_entry.place(x=180,y=40)

#Para vincular as funções de remoção de placeholder definidas ao clicar com o mouse
hour_entry.bind("<1>", h_click)
min_entry.bind("<1>", m_click)
sec_entry.bind("<1>", s_click)

#botão para ativar a função de timer
button = Button(window,text='Activate Timer', bg = 'blue',command=timer).pack(pady=40)

#Feche a janela e saia do aplicativo
window.mainloop()



