
password = '123'
i=1
while(i <= 3):
    userpassword = (input("Digite la contraseña: "))
    if(userpassword == password):
        print("Usuario correcto")
        break
    else: 
        print(f"Error. Intentos {i} de 3")
        i=i+1

