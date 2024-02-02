from porte import Porte
from ascenseur import Ascenseur
from usager import Usager

# Simulation
porte = Porte(0)
ascenseur = Ascenseur()
usager = [Usager('Andréa',2, 5),Usager('Christelle',0, 5),Usager('Eva',4, 1),Usager('Adriano',4, 1)]

for i in range(len(usager)):
    usager[i].appeler_ascenseur(ascenseur)


# Simulation de choix de direction et déplacement de l'ascenseur
while ascenseur.appels_existants() or ascenseur.destinations_existants():
    ascenseur.fermer_porte()
    ascenseur.choisir_direction()
    ascenseur.monter_descendre(usager)

