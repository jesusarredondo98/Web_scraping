# Importar librerías
from bs4 import BeautifulSoup
import requests

#Para varias paginas

#Creamos la variable raiz que nos servira para concatenarlo a los links de las peliculas
root = "https://subslikescript.com"

#Definimos la pagina web
web_site = f"{root}/movies"

#Enviamos una solicitud a la pagina
result = requests.get(web_site) #respuesta a la solicitud efectuada
content = result.text #obtenemos solo el texto

#Sirve para localizar elementos en una pagina web
soup = BeautifulSoup(content,"lxml") #Se cita el contenido y el parser

#Cuadro con los links de las peliculas
box = soup.find('article',class_="main-article")

#Obtenemos los link
#Activamos el atributo h_ref que contiene los links necesarios
#Obtenemos el link

links = [link["href"] for link in box.find_all('a',href = True)]

for link in links:

    web_site = f"{root}/{link}"

    result = requests.get(web_site) #respuesta a la solicitud efectuada
    content = result.text #obtenemos solo el texto
    soup = BeautifulSoup(content,"lxml") #Se cita el contenido y el parser
    box = soup.find('article',class_="main-article")

    title = box.find("h1").get_text() #No tiene clase solo el tag

    #Para obtener el transcript, tiene tag div
    #Con strip eliminamos espacios en blanco al principio y al final de cada oración
    #seperator va a cambiar el salto de linea por un espacio en blanco
    transcript = box.find("div", class_="full-script").get_text(strip = True, separator = " ")

    #Exportamos a un archivo txt

    with open(f"Beatiful_soup2_{title}.txt",'w') as archivo:
        archivo.write(transcript)