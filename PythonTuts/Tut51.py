#MultiLevel Inheritance

class Dad:
    basketball=1

class Son(Dad):
    dance=1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} number of times"

class Grandson(Son):
    dance = 6
    guitar=1
    def isdance(self):
        return f"Jackson yeah!Yes I dance very awesomly {self.dance} number of times"

    def isguitar(self):
        return f"Harry plays guitar {self.guitar} number of times"

darry=Dad()
larry=Son()
harry=Grandson()

print(darry.basketball)

print(larry.isdance())
print(larry.basketball)

print(harry.isdance())
print(harry.isguitar())
print(harry.basketball)
