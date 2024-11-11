num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar (+,-,*,/): ")

if operacao == '+':
    print(abs(num1 + num2))
    
elif operacao == '-':
    print(num1 - num2)

elif operacao == '*':
    print(num1 * num2)

elif operacao == '/':
    print(num1 / num2)

   
    



else: print("Operação invalida")