#MultiLevel Inheritance

class Electronicdevice:
    charge=1

class PocketGadgets(Electronicdevice):
    keep_in_pockets=1
    charge = 2

    def incharge(self):
        return f"Gadgets charge {self.charge} times"

class Phone(PocketGadgets):
    Music=10
    charge=3

    def incharge(self):
        return f"{self.charge} times charge"

    def palymusuc(self):
        return f"Music plays {self.Music} times"

ed=Electronicdevice()
pg=PocketGadgets()
ph=Phone()

print(ed.charge)

print(pg.charge)
print(pg.incharge())

print(ph.palymusuc())
print(ph.incharge())