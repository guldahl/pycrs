


print "hello"



class pet():
    def __init__(self, species):
        self.species = species

    def print_species(self):
        print self.species


dog = pet("dog")

dog.print_species()

cat = pet("cat")

cat.print_species()