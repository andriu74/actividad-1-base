try:
    a = int (input("digite un numero: "))
    b = int (input("digite uno mas: "))
    c = int (input("digite un ultimo numero: "))
    if (a > b and b > c ):
        print("" ,a,"-" ,b, "-" ,c)
    elif(b > a and a > c) :
        print("" ,b, "-" ,a, "-" ,c)
    elif (c > a and a > b) :
        print("" ,c, "-" ,a, "-" ,b)
    elif (c > b and b > a): 
        print("" ,c, "-" ,b, "-" ,a)
    elif(a > c and c > b) :
        print("" ,a, "-" ,c, "-" ,b)
    elif (b > c and c > a) :
        print("" ,b, "-" ,c, "-" ,a)

    else:
        print("se ingrsaron numeros iguales")
except:
    print("señor usuario usted debe ingresar solo numeros")


   

