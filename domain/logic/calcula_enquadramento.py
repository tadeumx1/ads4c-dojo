from domain.logic import calculo_salario_base

def calcula_enquadramento(salario_bruto, numero_dependentes):
  base_de_calculo = calculo_salario_base(salario_bruto, numero_dependentes)
    if base_de_calculo <= 1903.98:
      base_de_calculo_texto = 'Até 1.903,98'
      aliquota = 0.0
    elif base_de_calculo <= 2826.65:
      base_de_calculo_texto = 'De 1.903,99 até 2.826,65'
      aliquota = 7.5
    elif base_de_calculo <= 3751.05:
      base_de_calculo_texto = 'De 2.826,66 até 3.751,05'
      aliquota = 15
    elif base_de_calculo <= 4664.68:
      base_de_calculo_texto = 'De 3.751,06 até 4.664,68'
      aliquota = 22.5
    else:
      base_de_calculo_texto = 'Acima de 4.664,68'
      aliquota = 27.5

  return { 'base_de_calculo': base_de_calculo_texto, 'aliquota': aliquota }