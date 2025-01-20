from validador_de_triangulo import perimetro 

a = int(input("Insira o lado A"))
b = int(input("Insira o lado B"))
c = int(input("Insira o lado C"))

resultado = perimetro(a,b,c)
print("O perímetro é igual ", + resultado)