import json
import os
import re


class Container:
    _user = str()
    _storage: set[str] = set()
    _file = str()

    def __init__(self, user):
        self._user = user
        self._file = f'./users/{user}.json'
        self.load()

    def add(self, elem):
        self._storage.add(elem)

    def remove(self, elem):
        self._storage.remove(elem)

    def find(self, elem):
        if elem in self._storage:
            return elem

    def list(self):
        return list(self._storage)

    def grep(self, regex):
        return list(filter(lambda elem: re.match(regex, elem), self._storage))

    def save(self):
        os.makedirs(os.path.dirname(self._file), exist_ok=True)
        with open(self._file, 'w') as f:
            json.dump(list(self._storage), f)

    def load(self):
        if os.path.exists(self._file):
            with open(self._file, 'r') as f:
                self._storage = set(json.load(f))

    def switch(self, user):
        self._user = user
        self._file = f'./users/{user}.json'
        self.load()
