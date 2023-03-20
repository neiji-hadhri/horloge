import time
class Horloge:
    def __init__(self, h, m, s) -> None:
        self.heure = h 
        self.minute = m
        self.seconde = s
    
    def temps(self):
    
        while True :
            time.sleep(1)
            self.seconde+=1
            print("{0:02}:{1:02}:{2:02}".format(self.heure, self.minute, self.seconde), end="\r")
            
            if self.heure == self.heure_alarme and self.minute == self.minute_alarme and self.seconde == self.seconde_alarme:
                print("\nRéveille toi!!!!!!!!!!")
                break
            if self.seconde == 60: 
                self.minute+=1 
                self.seconde = 0
            if self.minute == 60:
                self.heure+=1
                self.minute=0
            if self.heure == 24:
                self.heure = 0
                self.minute = 0
                self.seconde = 0
            
            
    def modifHeure(self, h):
        self.heure = h 
            
    def modifMinute(self, m):
        self.minute = m
            
    def modifSeconde(self, s):
        self.seconde = s
            
    def afficher_heure(self,h , m, s):
        self.heure = h 
        self.minute = m
        self.seconde = s  

    def regler_alarme(self, heures, minutes, secondes):
        self.heure_alarme = heures
        self.minute_alarme = minutes
        self.seconde_alarme = secondes
        
        print("L'alarme s'active, à {}:{}:{}".format(heures, minutes, secondes)) 
            
        
            


                
T1 = Horloge(23, 59, 56)
#T1.modifHeure(12)
#T1.modifMinute(23)
#T1.modifSeconde(34)
T1.afficher_heure(12,23,34)
T1.regler_alarme(12, 23, 40)
T1.temps()



#def afficher_heure(h, m, s):
    #print("{}:{}:{}".format(h, m, s))
    #time.sleep(1.0)
#heure(12,15,56)