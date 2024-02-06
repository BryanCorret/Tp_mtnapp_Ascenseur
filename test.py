import unittest
from ascenseur import Ascenseur
from porte import Porte
from usager import Usager

class TestAscenseur(unittest.TestCase):
    def setUp(self):
        self.porte = Porte(0)
        self.ascenseur = Ascenseur()
        self.u1 = Usager(2, 5)
        self.u2 = Usager(2, 6)
        self.u3 = Usager(0, 1)
        self.u4 = Usager(5, 1)
        self.u5 = Usager(3, 6)

    def test_initialisation(self):
        self.assertEqual(self.ascenseur.etage, 0)
        self.assertIsNone(self.ascenseur.direction)
        self.assertEqual(self.ascenseur.destinations, [])
        self.assertEqual(self.ascenseur.appels, [])
        self.assertEqual(self.porte.etage, 0)
        self.assertEqual(self.u1.etage, 2)
        self.assertEqual(self.u1.destination, 5)
        self.assertEqual(self.u2.etage, 2)
        self.assertEqual(self.u2.destination, 6)
        self.assertEqual(self.u3.etage, 0)
        self.assertEqual(self.u3.destination, 1)
        self.assertEqual(self.u4.etage, 5)
        self.assertEqual(self.u4.destination, 1)
        self.assertEqual(self.u5.etage, 3)
        self.assertEqual(self.u5.destination, 6)

    def test_appel_ascenseur(self):
        self.u1.appeler_ascenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2])
        self.u3.appeler_ascenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2, 0])

    def test_multiple_appel_ascenseur(self):
        self.u1.appeler_ascenseur(self.ascenseur)
        self.u3.appeler_ascenseur(self.ascenseur)
        self.u1.appeler_ascenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2, 0])

    def test_entrer_ascenseur(self):
        if self.u1.entrer_ascenseur(self.ascenseur):# si l'usager est rentrer dans l'ascenseur
            self.assertEqual(self.ascenseur.destinations, [5])
        else:
            self.assertEqual(self.ascenseur.destinations, [])

    def test_meme_destination(self):
        self.u1.appeler_ascenseur(self.ascenseur)
        self.u2.appeler_ascenseur(self.ascenseur)
        self.u3.appeler_ascenseur(self.ascenseur)
        self.u4.appeler_ascenseur(self.ascenseur)
        self.u5.appeler_ascenseur(self.ascenseur)

        self.u1.entrer_ascenseur(self.ascenseur)
        self.u2.entrer_ascenseur(self.ascenseur)
        self.u3.entrer_ascenseur(self.ascenseur)
        self.u4.entrer_ascenseur(self.ascenseur)
        self.u5.entrer_ascenseur(self.ascenseur)

        self.assertEqual(self.ascenseur.destinations, [5, 1, 6])


    def test_choisir_direction(self):
        self.u1.appeler_ascenseur(self.ascenseur)
        self.u3.appeler_ascenseur(self.ascenseur)
        self.u1.entrer_ascenseur(self.ascenseur)
        self.u3.entrer_ascenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.direction, "haut")

    def test_mise_en_marche_asenceur(self):
        self.u1.appeler_ascenseur(self.ascenseur)
        self.u3.appeler_ascenseur(self.ascenseur)
        self.u1.entrer_ascenseur(self.ascenseur)
        self.u3.entrer_ascenseur(self.ascenseur)
        self.ascenseur.mise_en_marche_asenceur()
        self.assertEqual(self.ascenseur.etage, 2)
        self.assertEqual(self.ascenseur.destinations, [5])
        self.assertEqual(self.ascenseur.appels, [])
        self.assertEqual(self.ascenseur.direction, "haut")
    


    

        
    
        
        

if __name__ == '__main__':
    unittest.main()