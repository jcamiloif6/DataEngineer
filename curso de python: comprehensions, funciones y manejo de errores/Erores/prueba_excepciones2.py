def divide():

  try:

    op1 = (float(input("Ingrese el primer número: ")))
  
    op2 = (float(input("Ingrese el segundo número: ")))
  
    print("La división es: " + str(op1/op2))
    
  except ValueError:
    print("El valor introducido es erróneo")

  except ZeroDivisionError:
    print("No se puede dividir entre 0")

  finally: 
    print("Cálculo finalizado")

divide()