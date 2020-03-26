import os, requests
import secrets
from PIL import Image
from app_ecommerce import app

#Guardar en nuestra carpeta static
def save_picture(form_picture,folder):
    #Creamos un nombre aleatorio al fichero
    random_hex = secrets.token_hex(8)
    #Sacamos la extensión de la imagen que vamos a guardar
    _, f_ext = os.path.splitext(form_picture.filename)
    #Armamos el nombre del fichero con la extensión
    picture_fname = random_hex+f_ext
    #Creamos el path donde vamos a guardar
    picture_path = os.path.join(app.root_path,'static/'+folder,picture_fname)
    #Redimensionar la imagen
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    #Guardamos la imagen
    i.save(picture_path)
    #Devolvemos el nuevo path
    return picture_fname

def get_quote_USD_to(change):
    url = 'http://api.currencylayer.com/live?access_key=405e0a2e943e4174df8bb5881800e101&currencies=USD,AUD,CAD,PLN,MXN&format=1'
    response = requests.get(url)
    if (response.status_code == 200):
        quote = response.json()["quotes"]['USD'+change]  # Diccionario
        return quote