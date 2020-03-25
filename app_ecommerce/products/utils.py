import os
import secrets
from PIL import Image
from app_ecommerce import  app

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