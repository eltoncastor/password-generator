import random
import PySimpleGUI as sg
import os

class PassGen:
    # Layout
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Site/Software',size=(12,1)),sg.Input(key='site',size=(16,1))],
            [sg.Text('E-mail/Usuário',size=(12,1)),sg.Input(key='usuario',size=(16,1))],
            [sg.Text('Quantidade de caracteres'),sg.Combo(values=list(range(30)),key='total_chars',default_value=1,size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar senha'), sg.Button('Sair')]
        ]
        # Declarar Janela
        self.janela = sg.Window('Password Generator', layout)
    
    
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            
            if evento == sg.WIN_CLOSED or evento == 'Sair':
                break
            
            if evento == 'Gerar senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
                
    
    def gerar_senha(self, valores):
        char_list = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    
    
    
    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"Site/Software: {valores['site']}\nUsuario/E-mail: {valores['usuario']}\nSenha Gerada: {nova_senha}\n\n")
        
        print('\nDados salvos no arquivo "senhas.txt"')
        
        
gen = PassGen()
gen.Iniciar()
        