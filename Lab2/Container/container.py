class Container:
    _user = str()
    _storage = set()

    def __init__(self, user):
        self._user = user

    def add(self, elem):
        self._storage.add(elem)

    def remove(self, elem):
        self._storage.remove(elem)

    def find(self, elem):
        return elem in self._storage

    def list(self):
        return [self._storage]

    def grep(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def switch(self):
        pass
