salario = float(input('qual é o salario do funcionario?'))
novo = salario + (salario * 15/100)
print ('um funcionario que ganhava {:.2f} , com o aumento de 15% passa a ganhar {:.2f}'.format(salario,novo))