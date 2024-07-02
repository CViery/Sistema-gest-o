import hashlib



class Login:
    def __init__(self):
        pass
    

    def autenticar(self, user, password):
        try:
            usuario = user.upper()
            senha = password
            senha_hash = hashlib.sha1((senha).encode('utf-8')).hexdigest()
            banco = [
                        {
                            'usuario':'CRISTIAN',
                            'password':'7110eda4d09e062aa5e4a390b0a572ac0d2c0220'
                        },
                        {
                            'usuario':'MATHEUS',
                            'password':'2abd55e001c524cb2cf6300a89ca6366848a77d5'
                        }
                    ]
            for person in banco:
                if usuario == person['usuario'] and senha_hash == person['password']:
                    return True
            return False
        except Exception as e:
            print(e)
