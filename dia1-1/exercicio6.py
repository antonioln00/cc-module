def triangle(a, b, c):
    if a + b + c == 180:
        if a == b == c:
            print("É um triângulo equilátero")
        elif a != b != c: 
            print("É um triângulo escaleno")
        else:
            print("É um triângulo isóceles")
            
    else:
        print("Não é um triângulo")

triangle(30, 30, 20) 