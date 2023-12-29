import pandas as pd

#Guardar información en un archivo de texto
with open ('pruebas/prueba1.txt','w') as archivo:
    archivo.write('Data extraida correctamente!')

paises = ["MEXICO","COLOMBIA","PERU","ARGENTINA"]
poblacion = [1000,2000,50,30]
dict_poblacion = {'PAISES':paises, 'POBLACION':poblacion}

df = pd.DataFrame(dict_poblacion)

df.to_csv("prueba_2.csv",index=False,encoding="utf-8")

#Uso de excepciones

new_list = [2,4,6,"MEXICO"]

for e in new_list:
    try:
        print(e/2)
    except:
        print(f"El elemento {e} no es un número")

#While se mantiene mientras sea true, break se corta el bucle
#cuando se cumpla una condicion
n=4
while n>0:
    print(n)
    n = n-1
    if n == 2:
        break
print("Bucle terminado")