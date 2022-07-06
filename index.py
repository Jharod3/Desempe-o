
nombre = input("Nombre: ")
nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))
definitiva = (nota1 + nota2 + nota3) / 3

if(definitiva < 2):
    print("perdió, no puede habilitar")
elif(definitiva < 3):
    print("perdió, pero puede recuperar")
elif(definitiva < 4):
    print("Ganó")
elif(definitiva < 4.5):
    print("Sobresaliente")
elif(definitiva <= 5):
    print("Excelente")
else: 
    print("verifique las notas")    
