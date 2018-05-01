import base64


def encode_password(password):
    return base64.b64encode(password)
