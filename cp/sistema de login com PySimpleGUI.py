import PySimpleGUI as sg

layout = [
    [sg.Text('usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='Senha')],
    [sg.Button('Login')],
    [sg.Text('', key = 'mensagem')],
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        usuarioCorreto = 'teste'
        senhaCorreta = '1'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senhaCorreta and usuario == usuarioCorreto:
            window['mensagem'].update('login efetuado com sucesso')
        else:
            window['mensagem'].update('falha de login')