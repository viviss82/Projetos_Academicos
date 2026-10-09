## Trabalho Lógica de Programação e Algorítimos

## MENSAGEM DE BOAS VINDAS
print("-" * 70)
print("-" * 70)
print("Bem Vindo ao Sistema de Planos de Saúde")
print("Desenvolvido por: Vivian Oliveira dos Santos")
print("-" * 70)
print("-" * 70)

## VARIÁVEIS DA CALCULADORA

Valor_Base = float(input("Valor Base do Plano:"))
Idade = int(input("Idade:"))

print()

## ESTRUTURAS CONDICIONAIS 
if Idade >= 0 and Idade < 19: 
    Percentual = (100 / 100)
elif Idade > 19 and Idade < 29:
    Percentual = (150 / 100)
elif Idade >= 29 and Idade < 39: 
    Percentual = (225 / 100)
elif Idade >= 39 and Idade < 49:
    Percentual = (240 /100)
elif Idade >= 49 and Idade < 59:
    Percentual = (350/ 100)
## elif Idade > 59:
##  Percentual = (600 / 100)
else:
    Percentual = (600 / 100)
## CALCULO VALOR MENSAL

Valor_Mensal = Valor_Base * Percentual

## SAÍDA DA CAUCULADORA

print("-" * 70)
print("-" * 70)
print(f"Valor Base: R$ {Valor_Base:6.2f}")
print(f"Idade: {Idade} anos")
print(f"Percentual: {Percentual*100:6.2f}%")
print(f"Valor do Plano: R${Valor_Mensal:6.2f}")
print("-" * 70)
print("-" * 70)



