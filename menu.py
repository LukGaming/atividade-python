from aluno import *
menu = {}
menu['1'] = "Add Student"
menu['2'] = "Delete Student"
menu['3'] = "Find Student"
menu['4'] = "Exit"
print('--------Bem vindo------------')
print('--------Seleciona Uma Opção------------')
for x, y in menu.items():
  print(x,'---------', y)

print('--------Seleciona Uma Opção------------')
option = str(input())
print('Opção de ', menu[option], 'selecionada')
if(option == '1'):
  aluno = str(input())
  adicionarAluno(aluno)
  mostrarAlunos()
