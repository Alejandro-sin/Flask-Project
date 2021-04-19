import os


class Config(object):
    # Usada para la seguridad de formularios esta palabra se pega a una cookie para la seguirdad.
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_password_string" 
    