#Creating Class
class Genomics():
    number_genes= 200000
    number_chormosome= 23

    def __init__(self,n,ch,ge):
        self.name=str(n)
        self.choromosomal_abnormalities=str(ch)
        self.gene_chnages=str(ge)
        
    def getX(self):
        return self.name
    def getY(self):
        return self.choromosomal_abnormalities
    def getZ(self):
        return self.gene_chnages
    
    def __str__(self,number):
        if number is >23:
            return"The{} has either{} or {} ?.The answer is the Chromosome.".format(self.name, self.choromosomal_abnormalities,self.gene_chnages)
        else:   
            return"The{} has either{} or {} ?.The answer is the Gene.".format(self.name, self.choromosomal_abnormalities,self.gene_chnages)
    
#Subclass 1
class Single_Gene(Genomics):
    number_genes= 200000
    def Dominant(self):
        return "The change is dominat"
    def Recessive(self):
        return "The change is recessive"
    def Xlinked(self):
        return "The change is Xlinked"

#Subclass 2
class Chromosome(Genomics):
    number_chormosome= 23
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
    

