#Creating Class
from random import randrange

class Genomics():
    number_genes= 100
    number_chormosome= 10
    increament= 1
    hungry=7
    visionproblem=5
    a=
    b=
    c=
    d=
    

    def __init__(self,n,ch,ge):
        self.name=str(n)
        self.choromosomal_abnormalities=str(ch)
        self.gene_chnages=str(ge)
        self.public="Public"
        self._protected="Protected"
        self.increament=randrange(self.increament)
        self.hungry=randrange(self.hungry)
        self.visionproblem=randrange(self.visionproblem)
        self.visionproblem=randrange(self.visionproblem)
    
    #Property
    def getX(self):
        return self.name
    def getY(self):
        return self.choromosomal_abnormalities
    def getZ(self):
        return self.gene_chnages
    
    def __str__(self,number):
        if number is >10:
            return"The{} has either{} or {} ?.The answer is the Chromosome.".format(self.name, self.choromosomal_abnormalities,self.gene_chnages)
        else:   
            return"The{} has either{} or {} ?.The answer is the Gene.".format(self.name, self.choromosomal_abnormalities,self.gene_chnages)
    
    #Name Setter
    def getX(self,namegiven):
        alphabet=["abcdefghijklmnopqrstuvwxyz"]
        if namegiven in alphabet:
            self.name=str(namegiven)
        else:
            return "No information available"
    
    def forward(self):
        self.increament+=1
        
    def report (self):
        return"Your report is good"
    
    def mood(self):
        if self.hungry >5:
            return " not good mood"
        else:
            return " good mood"
     
#Subclass 1
class Single_Gene(Genomics):
    number_genes= 100
    def Dominant(self):
        return "The change is dominat"
    def Recessive(self):
        return "The change is recessive"
    def Xlinked(self):
        return "The change is Xlinked"

#Subclass 2
class Chromosome(Genomics):
    number_chormosome= 10
    def Deletion(self):
        return "The change is deletion"
    def Inversion(self):
        return "The change is inversion"
    def Translocation(self):
        return "The change is translocation"
    def Mosaicism(self):
        return "The change is mosaicism"
    def Ring(self):
        return "The change is ring"
    def Aneuploidy(self):
        return "The change is Aneuploidy"
    
#Subclass 3
# in super function is takes the n from the main class
class Other(Genomics):
    def __init__(self,n,other):
        super().__init__(n)
        self.otherchanges=other
    
#Sublcass of subclass
class Cancer(Single_Gene):
    def weight_loss(self):
        if self.hungry >5:
            return "You should test for Cancer"
class Alzeimer(Single_Gene):
    def vision(self):
        if self.visionproblem >5:
            return "You should tets for Alzeimer"
    
        
        
    
