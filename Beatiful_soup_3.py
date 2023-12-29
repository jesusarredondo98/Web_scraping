# Importar librerías
from bs4 import BeautifulSoup
import requests
import os

#Para varias paginas

#Creamos la variable raiz que nos servira para concatenarlo a los links de las peliculas
root = "https://subslikescript.com"

#Definimos la pagina web
web_site = f"{root}/movies_letter-A"

#Enviamos una solicitud a la pagina
result = requests.get(web_site) #respuesta a la solicitud efectuada
content = result.text #obtenemos solo el texto

#Sirve para localizar elementos en una pagina web
soup = BeautifulSoup(content,"lxml") #Se cita el contenido y el parser

###----------------------Pagination----------------------------###
#Ubicacion de las distintas paginas de navegación
pagination = soup.find('ul',class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text #Tomamos el penultimo elemento dado que el último elemento es un flecha

###-------------------------------------------------------------###

for page in range(1,int(last_page)+1)[:2]:
    #guia pagina https://subslikescript.com/movies_letter-A?page=1
    result = requests.get(f"{root}/movies_letter-A?page={page}") #respuesta a la solicitud efectuada
    content = result.text #obtenemos solo el texto
    soup = BeautifulSoup(content,"lxml") #Se cita el contenido y el parser


    #Cuadro con los links de las peliculas
    box = soup.find('article',class_="main-article")
    links = [link["href"] for link in box.find_all('a',href = True)]

    for link in links:
        try:
            print("----------------------")
            print(link)


            result = requests.get(f"{root}/{link}") #respuesta a la solicitud efectuada
            content = result.text #obtenemos solo el texto
            soup = BeautifulSoup(content,"lxml") #Se cita el contenido y el parser
            box = soup.find('article',class_="main-article")

            title = box.find("h1").get_text() #No tiene clase solo el tag

            #Para obtener el transcript, tiene tag div
            #Con strip eliminamos espacios en blanco al principio y al final de cada oración
            #seperator va a cambiar el salto de linea por un espacio en blanco
            transcript = box.find("div", class_="full-script").get_text(strip = True, separator = " ")
            os.makedirs(os.path.dirname(f"pruebas/{page}/Beatiful_soup3_{title}.txt"), exist_ok=True)
            with open(f"pruebas/{page}/Beatiful_soup3_{title}.txt",'w') as archivo:
                archivo.write(transcript)
            print(f"Archivo Beatiful_soup3_{title}.txt esta grabado")
            print("------------------------------------")
        except:
            print("-----------------------")
            print(f"Link {link} is not working !!!")
            print("---------------------------------------")

