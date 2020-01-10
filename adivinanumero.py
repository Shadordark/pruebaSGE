import random
print ("Como te llamas?")
nombre = input()
numero = 0
numeroaleatorio = random.randrange(20)
print ("Hola "+nombre+", voy a pensar en un numero del 1 al 20\n")
i = 0
while i < 6:
  if numero == numeroaleatorio:
    print("Has acertado, enhorabuena!")
  else:
    print("Llevas ",i," intento, tienes un máximo de 5 para acertar")
    print ("Dime un numero a ver si aciertas")
    try:
      numero = int(input())
    except:
      print("No has introducido un numero!")
  
  if numero < numeroaleatorio:
    print("El numero es mayor del que has puesto...")

  if numero > numeroaleatorio:
    print("El numero es menor del que has puesto...")

  i += 1

if numero != numeroaleatorio:
  print("Has fallado "+nombre+", el numero era ",numeroaleatorio)