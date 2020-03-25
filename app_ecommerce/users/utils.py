import os
import secrets
from PIL import Image
from flask import url_for, app
from flask_mail import Message
from app_ecommerce import  mail

#Guardar en nuestra carpeta static
def save_picture(form_picture):
    #Creamos un nombre aleatorio al fichero
    random_hex = secrets.token_hex(8)
    #Sacamos la extensión de la imagen que vamos a guardar
    _, f_ext = os.path.splitext(form_picture.filename)
    #Armamos el nombre del fichero con la extensión
    picture_fname = random_hex+f_ext
    #Creamos el path donde vamos a guardar
    picture_path = os.path.join(app.root_path,'static/profile_picts',picture_fname)
    #Redimensionar la imagen
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    #Guardamos la imagen
    i.save(picture_path)
    #Devolvemos el nuevo path
    return picture_fname

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: 
    {url_for('users.reset_token', token=token,_external=True)}
    If you didnt this request, simply ignore
    '''
    mail.send(msg)