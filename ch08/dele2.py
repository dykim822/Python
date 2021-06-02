class Dele:
    def __init__(self, st):
        self.st = st
    def __getattr__(self, item):
        print(f"위임 : {item}", end=" ")
        return getattr(self.st, item)
#     0123456789012345678901
st = "Good Morning My Friend"
dl = Dele(st)
print(dl.count('n'))
print(dl.find('d'))
print(dl.rfind('d'))