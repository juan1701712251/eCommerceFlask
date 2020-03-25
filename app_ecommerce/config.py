import os
class Config:
    SECRET_KEY = 'c95f4dffa6f7528d72de8e94ffa16e2e'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # Para correos GMAIL
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # Cambiar esto en las variables de entorno
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')