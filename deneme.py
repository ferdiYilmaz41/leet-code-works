class Arac:
    def __init__(self,marka,model):
        self.marka=marka
        self.__model=model
    def get_model(self):
        return self.__model
    def bilgileri_goster(self):
        print(f"Marka:{self.marka} Model:{self.__model} ")
    def __str__(self):
        return f"{self.marka} {self.__model}"
    
class Araba(Arac):
    def __init__(self,marka,model,yil):
        super().__init__(marka,model)
        self.__yil=yil
    def __len__(self):
        return int(self.__yil)

arac1=Arac("Fiat","Doblo")
araba1=Araba("Hyundai","Tucson",2010)

#print(arac1.get_model())
#print(arac1)
#arac1.bilgileri_goster()
#araba1.bilgileri_goster()
print(araba1)
