# Importar librerías
from bs4 import BeautifulSoup
import requests

#Definimos la pagina web
web_site = "https://subslikescript.com/movie/Titanic-120338"

#Enviamos una solicitud a la pagina
result = requests.get(web_site) #respuesta a la solicitud efectuada
content = result.text #obtenemos solo el texto

#Sirve para localizar elementos en una pagina web
soup = BeautifulSoup(content,"lxml") #Se cita el contenido y el parser

#Imprimimos el codigo html con un mjoer formato

#print(soup.prettify())

#Buscamos solo el elemento de main_article, primero va el tipo de tag y luego el nombre de la clase
#Lo guardamos en una variable
box = soup.find('article',class_='main-article')

#Para obtener el elemnto en el tag h1

title = box.find("h1").get_text() #No tiene clase solo el tag

#Imprimos el titulo
#print(title)

#Para obtener el transcript, tiene tag div
#Con strip eliminamos espacios en blanco al principio y al final de cada oración
#seperator va a cambiar el salto de linea por un espacio en blanco
transcript = box.find("div", class_="full-script").get_text(strip = True, separator = " ")

#Imprimimos el transcript
#print(transcript)

#Exportamos a un archivo txt

with open(f"Beatiful_soup1_{title}.txt",'w') as archivo:
    archivo.write(transcript)