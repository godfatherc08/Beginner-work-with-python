
class Password:
    def __init__(self, website, encryption, n):
        self.n = n
        self.website = website
        self.encryption = encryption
    def __add__(self, other):
        pass