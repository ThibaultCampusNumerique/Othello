class Case:
    def __init__(self, label):
        self.label = label

    def contient_pion(self, Pion):
        if 


















































    def se_deplacer(self):
        pass

    def get_poids(self):
        return self.__poids

    def get_taille(self):
        return self.__taille

    def set_poids(self, poids):
        if poids > 0:
            self.__poids = poids
        else:
            print("ValueError")

    def set_taille(self, taille):
        if taille <= 0:
            print("ValueError")
        else:
            self.__taille = taille