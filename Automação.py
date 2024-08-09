import pyautogui as sg
import PySimpleGUI as sa
from time import sleep 

sa.theme('Reddit')

layout = [
    [sa.Text('Selecione a forma de pagamento da comanda que deseja lançar')],
    [sa.Button('pix')],
    [sa.Button('dinheiro')],
    [sa.Button('débito')],
    [sa.Button('Crédito')]
]
    
def dinheiro():
    sg.click(x=970, y=167) 
    sleep(0.5)
    sg.click(x=1266,y=167) 
    sleep(1.5)
    sg.click(x=839, y=412) # Clique em "serviço"
    sleep(1)
    sg.click(x=1401, y=589) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1158, y=627) # Clique em "continuar"
    sleep(2)
    sg.click(x=1117, y=500) # Clique em "adicionar pagamento"
    sleep(2)
    sg.click(x=945, y=298)  # Clique para "selecionar pagamento"
    sleep(2)
    sg.click(x=948,y=681)  # Clique em "dinheiro"
    sleep(1)
    sg.click(x=1208, y=518) # Clique em "salvar"
    sleep(1)
    sg.click(x=1169, y=200) # Clique em "fechar"
    sleep(1)
    sg.click(x=1158, y=681) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1836,y=202) # Clique fora
    sleep(1)
    sg.click(x=1836,y=202) # Clique adicionar
    sleep(1)
    sg.click(x=911,y=180) # Clique pesquisar
   
def pix():
    sg.click(x=970, y=167) 
    sleep(0.5)
    sg.click(x=1266,y=167) 
    sleep(1.5)
    sg.click(x=839, y=412) # Clique em "serviço"
    sleep(1)
    sg.click(x=1401, y=589) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1158, y=627) # Clique em "continuar"
    sleep(2)
    sg.click(x=1117, y=500) # Clique em "adicionar pagamento"
    sleep(2)
    sg.click(x=945, y=298)  # Clique para "selecionar pagamento"
    sleep(2)
    sg.click(x=976, y=739)  # Clique em "pix"
    sleep(1)
    sg.click(x=1208, y=518) # Clique em "salvar"
    sleep(1)
    sg.click(x=1169, y=200) # Clique em "fechar"
    sleep(1)
    sg.click(x=1158, y=681) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1836,y=202) # Clique fora
    sleep(1)
    sg.click(x=1836,y=202) # Clique adicionar
    sleep(1)
    sg.click(x=911,y=180) # Clique pesquisar

def debito():

    sg.click(x=970, y=167) 
    sleep(0.5)
    sg.click(x=1266,y=167) 
    sleep(1.5)
    sg.click(x=839, y=412) # Clique em "serviço"
    sleep(1)
    sg.click(x=1401, y=589) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1158, y=627) # Clique em "continuar"
    sleep(2)
    sg.click(x=1117, y=500) # Clique em "adicionar pagamento"
    sleep(2)
    sg.click(x=945, y=298)  # Clique para "selecionar pagamento"
    sleep(2)
    sg.click(x=943,y=462)  # Clique em "débito"
    sleep(1)
    sg.click(x=938, y=598)
    sleep(1)
    sg.click(x=944, y=622)
    sleep(1)
    sg.click(x=1208, y=518) # Clique em "salvar"
    sleep(1)
    sg.click(x=1169, y=200) # Clique em "fechar"
    sleep(1)
    sg.click(x=1158, y=681) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1836,y=202) # Clique fora
    sleep(1)
    sg.click(x=1836,y=202) # Clique adicionar
    sleep(1)
    sg.click(x=911,y=180) # Clique pesquisar
   
    
    sg.click(x=970, y=167) 
    sleep(0.5)
    sg.click(x=1266,y=167) 
    sleep(1.5)
    sg.click(x=839, y=412) # Clique em "serviço"
    sleep(1)
    sg.click(x=1401, y=589) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1158, y=627) # Clique em "continuar"
    sleep(2)
    sg.click(x=1117, y=500) # Clique em "adicionar pagamento"
    sleep(2)
    sg.click(x=945, y=298)  # Clique para "selecionar pagamento"
    sleep(2)
    sg.click(x=976, y=739)  # Clique em "pix"
    sleep(1)
    sg.click(x=1208, y=518) # Clique em "salvar"
    sleep(1)
    sg.click(x=1169, y=200) # Clique em "fechar"
    sleep(1)
    sg.click(x=1158, y=681) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1836,y=202) # Clique fora
    sleep(1)
    sg.click(x=1836,y=202) # Clique adicionar
    sleep(1)
    sg.click(x=911,y=180) # Clique pesquisar
  
def crédito():
    sg.click(x=970, y=167) 
    sleep(0.5)
    sg.click(x=1266,y=167) 
    sleep(1.5)
    sg.click(x=839, y=412) # Clique em "serviço"
    sleep(1)
    sg.click(x=1401, y=589) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1158, y=627) # Clique em "continuar"
    sleep(2)
    sg.click(x=1117, y=500) # Clique em "adicionar pagamento"
    sleep(2)
    sg.click(x=945, y=298)  # Clique para "selecionar pagamento"
    sleep(2)
    sg.click(x=935, y=409)  # Clique em "crédito"
    sleep(1)
    sg.click(x=1039, y=592) 
    sleep(1)
    sg.click(x=1027, y=627) 
    sleep(1)
    sg.click(x=970, y=548)
    sleep(1)
    sg.click(x=1208, y=518) # Clique em "salvar"
    sleep(1)
    sg.click(x=1169, y=200) # Clique em "fechar"
    sleep(1)
    sg.click(x=1158, y=681) # Clique em "confirmar"
    sleep(1)
    sg.click(x=1836,y=202) # Clique fora
    sleep(1)
    sg.click(x=1836,y=202) # Clique adicionar
    sleep(1)
    sg.click(x=911,y=180) # Clique pesquisar
   
 

# Criação da janela
janela = sa.Window('Sistema brabooooo', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sa.WINDOW_CLOSED:
        break
    elif eventos == 'pix':
        pix()
    elif eventos == 'dinheiro':
        dinheiro()
    elif eventos == 'débito':
        debito()
    elif eventos == 'Crédito':
        crédito()

janela.close()
