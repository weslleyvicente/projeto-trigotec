import math

class Trigotec:
        
    def pitagoras(self, cateto_oposto, cateto_adjacente):
        """calcula a hipotenusa usando o teorema de pitágoras."""
        hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
        return hipotenusa

    def calcular_trigonometria(self, cateto_oposto, cateto_adjacente):
        """calcula seno, cosseno, tangente e hipotenusa de um triângulo retângulo."""
        hipotenusa = self.pitagoras(cateto_oposto, cateto_adjacente)
        seno = cateto_oposto / hipotenusa
        cosseno = cateto_adjacente / hipotenusa
        tangente = cateto_oposto / cateto_adjacente if cateto_adjacente != 0 else None
        return seno, cosseno, tangente, hipotenusa

    def calcular_hipotenusa(self, cateto_a, cateto_b):
        """calcula a hipotenusa usando os dois catetos fornecidos."""
        return self.pitagoras(cateto_a, cateto_b)

    def seno(self, angulo):
        """calcula o seno de um ângulo (em graus)."""
        return math.sin(math.radians(angulo))

    def cosseno(self, angulo):
        """calcula o cosseno de um ângulo (em graus)."""
        return math.cos(math.radians(angulo))

    def tangente(self, angulo):
        """calcula a tangente de um ângulo (em graus)."""
        return math.tan(math.radians(angulo))

# menu principal -
trigotec = Trigotec()

while True:
    print("bem-vindos a trigotec! \n(calculadora de triângulo retângulo)")
    print("\nescolha uma opção:")
    print("1. calcular a hipotenusa usando os catetos ")
    print("2. calcular seno, cosseno e tangente a partir dos catetos ")
    print("3. calcular seno de um ângulo ")
    print("4. calcular cosseno de um ângulo ")
    print("5. calcular tangente de um ângulo ")
    print("6. sair! ")

    escolha = input("digite o número da opção: ")

    if escolha == '1':
        cateto_oposto = float(input("digite o comprimento do cateto oposto: "))
        cateto_adjacente = float(input("digite o comprimento do cateto adjacente: "))
        hipotenusa = trigotec.pitagoras(cateto_oposto, cateto_adjacente)
        print(f"a hipotenusa é: {hipotenusa:.2f}")

    elif escolha == '2':
        cateto_oposto = float(input("digite o comprimento do cateto oposto: "))
        cateto_adjacente = float(input("digite o comprimento do cateto adjacente: "))
        seno, cosseno, tangente, hipotenusa = trigotec.calcular_trigonometria(cateto_oposto, cateto_adjacente)
        print(f"\nresultados:")
        print(f"hipotenusa: {hipotenusa:.2f}")
        print(f"seno: {seno:.2f}")
        print(f"cosseno: {cosseno:.2f}")
        print(f"tangente: {tangente:.2f}" if tangente is not None else "tangente: indefinido.")

    elif escolha == '3':
        angle = float(input("digite o ângulo em graus: "))
        seno = trigotec.seno(angle)
        print(f"o seno de {angle}° é: {seno:.2f}")

    elif escolha == '4':
        angle = float(input("digite o ângulo em graus: "))
        cosseno = trigotec.cosseno(angle)
        print(f"o cosseno de {angle}° é: {cosseno:.2f}")

    elif escolha == '5':
        angle = float(input("digite o ângulo em graus: "))
        tangente = trigotec.tangente(angle)
        print(f"a tangente de {angle}° é: {tangente:.2f}")

    elif escolha == '6':
        print("saindo da trigotec. até logo!")
        break

    else:
        print("opção inválida. tente novamente :/ ")