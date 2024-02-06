import unittest
from ascenseur import Ascenseur
from porte import Porte
from usager import Usager
from io import StringIO
import sys

class TestAscenseur(unittest.TestCase):
    def setUp(self):
        self.porte = Porte(0)
        self.ascenseur = Ascenseur()
        self.u1 = Usager('Jean',2, 5)
        self.u2 = Usager('Jacque',2, 6)
        self.u3 = Usager('Michel',0, 1)
        self.u4 = Usager('Guylenne',5, 1)
        self.u5 = Usager('Julien',3, 6)
        self.u6 = Usager('Juliette',0, 5)

    def test_initialisation(self):
        self.assertEqual(self.ascenseur.etage, 0)
        self.assertIsNone(self.ascenseur.direction)
        self.assertEqual(self.ascenseur.destinations, [])
        self.assertEqual(self.ascenseur.appels, [])
        self.assertEqual(self.porte.etage, 0)
        self.assertEqual(self.u1.getEtage(), 2)
        self.assertEqual(self.u1.destination, 5)
        self.assertEqual(self.u2.getEtage(), 2)
        self.assertEqual(self.u2.destination, 6)
        self.assertEqual(self.u3.getEtage(), 0)
        self.assertEqual(self.u3.destination, 1)
        self.assertEqual(self.u4.getEtage(), 5)
        self.assertEqual(self.u4.destination, 1)
        self.assertEqual(self.u5.getEtage(), 3)
        self.assertEqual(self.u5.destination, 6)

    def test_appel_ascenseur(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2])
        self.u3.appelerAscenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2, 0])

    def test_multiple_appel_ascenseur(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.u3.appelerAscenseur(self.ascenseur)
        self.u1.appelerAscenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2, 0])

    def test_entrer_ascenseur(self):
        if self.u1.entrerAscenseur(self.ascenseur):# si l'usager est rentrer dans l'ascenseur
            self.assertEqual(self.ascenseur.destinations, [5])
        else:
            self.assertEqual(self.ascenseur.destinations, [])

    def test_meme_destination(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.u2.appelerAscenseur(self.ascenseur)
        self.u3.appelerAscenseur(self.ascenseur)
        self.u4.appelerAscenseur(self.ascenseur)
        self.u5.appelerAscenseur(self.ascenseur)

        self.u1.entrerAscenseur(self.ascenseur)
        self.u2.entrerAscenseur(self.ascenseur)
        self.u3.entrerAscenseur(self.ascenseur)
        self.u4.entrerAscenseur(self.ascenseur)
        self.u5.entrerAscenseur(self.ascenseur)

        self.assertEqual(self.ascenseur.destinations, [5, 1, 6])


    def test_choisir_direction(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.u3.appelerAscenseur(self.ascenseur)
        self.u1.entrerAscenseur(self.ascenseur)
        self.u3.entrerAscenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.direction, "haut")

    def test_monter_descendre(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.u3.appelerAscenseur(self.ascenseur)
        self.u1.entrerAscenseur(self.ascenseur)
        self.u2.entrerAscenseur(self.ascenseur)
        self.u3.entrerAscenseur(self.ascenseur)
        self.u4.entrerAscenseur(self.ascenseur)
        self.u5.entrerAscenseur(self.ascenseur)

        # Récupération du print d'information d'ascenseur deja complet
        captured_output = StringIO()
        sys.stdout = captured_output
        self.u6.entrerAscenseur(self.ascenseur)
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        
        # Test du print d'information d'ascenseur deja complet
        self.assertEqual(output.strip(), f"Ascenseur plein,{self.u6.nom} doit attendre quelque minutes")


        self.ascenseur.monter_descendre()
        self.assertEqual(self.ascenseur.etage, 2)
        self.assertEqual(self.ascenseur.destinations, [5])
        self.assertEqual(self.ascenseur.appels, [])
        self.assertEqual(self.ascenseur.direction, "haut")

if __name__ == '__main__':
    unittest.main()