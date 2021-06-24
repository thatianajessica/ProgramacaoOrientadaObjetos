class Pessoa:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    def __repr__(self):
        return 'Pessoa({0},{1})'.format(self._nome, self._email)
