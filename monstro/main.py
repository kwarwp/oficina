# oficina.monstro.main.py
from _spy.vitollino.main import Jogo, STYLE
STYLE.update(width=900, height="600px")

CENARIO = "https://i.imgur.com/aisVckn.jpg"
UM_MONSTRO = "https://i.imgur.com/MRmfpAv.png"
OU_MONSTRO = "https://i.imgur.com/XFVLtJE.png"
EI_MONSTRO = "https://i.imgur.com/RfLJEhs.png"

class Monstro:
    def __init__(self):
        self.jogo = Jogo()
        self.cenario = self.jogo.c(CENARIO)
        self.monstro = self.jogo.a(UM_MONSTRO, x=700, y=400, cena = self.cenario)
        self.monstro = self.jogo.a(OU_MONSTRO, x=780, y=300, cena = self.cenario)
        self.monstro = self.jogo.a(EI_MONSTRO, x=550, y=450, cena = self.cenario)
        
    def vai(self):
        self.cenario.vai()
        
if __name__ == "__main__":
    monstro = Monstro()
    monstro.vai()