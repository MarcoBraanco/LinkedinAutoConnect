import PySimpleGUI as sg

class tela:
    def __init__(self):
        """
        Configurações iniciais da GUI
        
        """
        sg.theme(new_theme="DarkPurple1")
        layout = [
            [sg.Text('Usuario:',),sg.Input(size=(40,1),key="user")],
            [sg.Text('Senha:',size=(6,0)),sg.Input(size=(40,1),password_char="*",key="password")],
            [sg.Text('Palavra chave:'),sg.Input(size=(20,0),key="keyword")],
            [sg.Text('Por quantas paginas o robo deve passar? '),sg.Slider(range=(1, 10),default_value=1,orientation='h',key="people_loop")],
            [sg.Button('Iniciar o robô')],
            [sg.Output(size=(65,20))]
        ]
        self.janela = sg.Window("LinkedIn Auto-connect", layout, size=(400,300), element_justification="center")

    def iniciar(self):
        """
        Inicia o programa através da GUI

        """
        while True:
            self.events, self.values = self.janela.Read()
            if self.events == sg.WIN_CLOSED:
                break
            else:
                self.bot = Linkedin_autoConnect()
                self.bot.rodar(self.values['user'], self.values['password'], self.values['keyword'], self.values['people_loop'])
                break
        sleep(5)
        self.janela.Close()

GUI = tela()
GUI.iniciar()