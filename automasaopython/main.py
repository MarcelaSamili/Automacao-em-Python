import pyautogui
from time import sleep
#fazer um beckup de um arquivo na área de trabalho
# para o google drive

#PASSOS

pyautogui.alert('Não mexa no pc durante a execurção do programa!!!')

#entrei no google drive no pc
pyautogui.PAUSE = 0.5 # O CODIGO É FEITO MUITO RÁPIDO E AS VEZES O PC PODE NAO ACOMAPNHR ENTAO É BOM COOCAR UM TEMPO ENTRE UMA FUNÇÃO E OUTRA
pyautogui.press('winleft') #esse press é somente um click, para saber os nomes das teclas é so pegar o manual do pacote pyautogui
pyautogui.write('chorome')
pyautogui.press('enter')
sleep(0.4)
pyautogui.write('http://')#aqui voce coloca o link do SEU Google Drive
pyautogui.press('enter')
sleep(1)

#entrar na area de trabalho
pyautogui.hotkey('winleft', 'd')
sleep(0.5)

#clicar no arquivo que eu quero e arrastar ele
pyautogui.moveTo(1233, 32) #para ver esas posisções, abra python console e coloque o comando pyautogui.positon() no Python Console, posicione o mouse sobre o arquivo que quer pegar e sem tirar o mouse do lugar de ok no python console e vai aparecer Point x... e y.. e é so por aqui
sleep(0.5)                 #essas coordenadas sao do meu pc as do seu é diferente voce precisa fazer isso qui de cima^ .
pyautogui.mouseDown()
sleep(0.5)

#enquanto eu estou arrastando eu vou mudar para o google drive
pyautogui.moveTo(991, 579)
sleep(0.5)
pyautogui.hotkey('alt', 'tab')
sleep(0.5)

#largei ele no google drive
pyautogui.mouseUp()

#esperar 5 segundo
sleep(2)
pyautogui.alert('CODIGO FINALIZADO COM SUCESSO!! SEU BECKUP FOI FEITO, PODE USAR SEU PC NORMALMETE!')
