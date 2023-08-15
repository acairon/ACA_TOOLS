import bcrypt
import jwt

# Ejemplo de autenticación utilizando contraseñas con bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password)

# Ejemplo de generación y verificación de tokens JWT
def generate_jwt_token(payload, secret_key):
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def verify_jwt_token(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token expirado"
    except jwt.InvalidTokenError:
        return "Token inválido"
