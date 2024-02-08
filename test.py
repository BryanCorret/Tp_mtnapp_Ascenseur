import unittest
from ascenseur import Ascenseur
from porte import Porte
from usager import Usager
from io import StringIO
import sys
class TestPorte(unittest.TestCase):
    def setUp(self):
        self.porte = Porte(0)
        self.ascenseur = Ascenseur()

    def test_initialisation(self):
        self.assertEqual(self.porte.etage, 0)


    def test_porte(self):        
        etage = self.porte.getEtage()

        captured_output = StringIO()
        sys.stdout = captured_output
        self.porte.ouvrir()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        # Test du print d'ouverture de porte
        self.assertEqual(output.strip(), f"La porte s'ouvre à l'étage {etage}")

        captured_output = StringIO()
        sys.stdout = captured_output
        self.porte.fermer()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        # Test du print de fermeture de la porte
        self.assertEqual(output.strip(), f"La porte se ferme à l'étage {etage}")

        captured_output = StringIO()
        sys.stdout = captured_output
        self.porte.signaler_redemarrage()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        # Test du print de redemarrage de la porte
        self.assertEqual(output.strip(), "Signaler à l'ascenseur qu'il peut redémarrer")


class TestUsager(unittest.TestCase):
    def setUp(self):
        self.porte = Porte(0)
        self.ascenseur = Ascenseur()
        self.u1 = Usager('Jean',2, 5)
        self.u2 = Usager('Jacque',2, 6)
        self.u3 = Usager('Michel',0, 1)
        self.u4 = Usager('Guylenne',5, 1)
        self.u5 = Usager('Julien',3, 6)
        self.u6 = Usager('Juliette',0, 2)

    def test_initialisation(self):
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

    def test_multiple_appel_ascenseur(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.u3.appelerAscenseur(self.ascenseur)
        self.u1.appelerAscenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2, 0])

    def test_attendre_porte_ouverte(self):
        # Récupération du print d'information d'ascenseur deja complet
        captured_output = StringIO()
        sys.stdout = captured_output
        self.u1.attendre_porte_ouverte()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        # Test du print d'information d'ascenseur deja complet
        self.assertEqual(output.strip(), f"Attendre que la porte de l'ascenseur s'ouvre.")

    def test_sortirAscenseur(self):
        self.ascenseur.addPersonne()
        # Récupération du print d'information d'ascenseur deja complet
        captured_output = StringIO()
        sys.stdout = captured_output
        self.u1.sortirAscenseur(self.ascenseur)
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        # Test du print d'information d'ascenseur deja complet
        self.assertEqual(output.strip(), f"{self.u1.nom} sort de l'ascenseur")


    def test_getDestination(self):
        self.assertEqual(self.u1.getDestination(), 5)








class TestAscenseur(unittest.TestCase):
    def setUp(self):
        self.porte = Porte(0)
        self.ascenseur = Ascenseur()
        self.u1 = Usager('Jean',2, 5)
        self.u2 = Usager('Jacque',2, 6)
        self.u3 = Usager('Michel',0, 1)
        self.u4 = Usager('Guylenne',5, 1)
        self.u5 = Usager('Julien',3, 6)
        self.u6 = Usager('Juliette',0, 2)

    def test_initialisation(self):
        self.assertEqual(self.ascenseur.etage, 0)
        self.assertIsNone(self.ascenseur.direction)
        self.assertEqual(self.ascenseur.destinations, [])
        self.assertEqual(self.ascenseur.appels, [])

    def test_appels_existants(self):
        # Test when appels is not empty
        self.ascenseur.appels = [2, 3]
        self.assertTrue(self.ascenseur.appels_existants())

        # Test when appels is empty
        self.ascenseur.appels = []
        self.assertFalse(self.ascenseur.appels_existants())

    def test_destinations_existants(self):
        # Test when destinations is not empty
        self.ascenseur.destinations = [5, 6]
        self.assertTrue(self.ascenseur.destinations_existants())

        # Test when destinations is empty
        self.ascenseur.destinations = []
        self.assertFalse(self.ascenseur.destinations_existants())

    def test_appel_ou_destination_existe(self):
        # Test when etage is in appels
        self.ascenseur.appels = [2, 3]
        self.ascenseur.destinations = [5, 6]
        self.assertTrue(self.ascenseur.appel_ou_destination_existe(2, "haut"))

        # Test when etage is in destinations
        self.assertTrue(self.ascenseur.appel_ou_destination_existe(5, "bas"))

        # Test when etage is not in appels or destinations
        self.assertFalse(self.ascenseur.appel_ou_destination_existe(1, "haut"))

    def test_signaler_ouvrir_porte(self):
        ...
    def test_ouvrir_porte(self):
        ...
    def test_fermer_porte(self):
        ...
        
    def test_supprimer_appel(self):
        # Test when etage exists in appels
        self.ascenseur.appels = [2, 3, 4]
        self.ascenseur.supprimer_appel(3)
        self.assertEqual(self.ascenseur.appels, [2, 4])

        # Test when etage does not exist in appels
        self.ascenseur.supprimer_appel(1)
        self.assertEqual(self.ascenseur.appels, [2, 4])

    def test_getDestination(self):
        # Test when destinations is not empty
        self.ascenseur.destinations = [5, 6]
        self.assertEqual(self.ascenseur.getDestination(), [5, 6])

        # Test when destinations is empty
        self.ascenseur.destinations = []
        self.assertEqual(self.ascenseur.getDestination(), [])

    def test_getAppel(self):
        # Test when appels is not empty
        self.ascenseur.appels = [2, 3]
        self.assertEqual(self.ascenseur.getAppel(), [2, 3])

        # Test when appels is empty
        self.ascenseur.appels = []
        self.assertEqual(self.ascenseur.getAppel(), [])

    def test_choisir_direction(self):
        # Cas où la direction est initialement None, et il y a des appels
        self.ascenseur.direction = None
        self.ascenseur.etage = 0
        self.ascenseur.appels = [2]
        self.ascenseur.choisir_direction()
        self.assertEqual(self.ascenseur.direction, 'haut')

        # Cas où la direction est initialement None, mais il y a des destinations
        self.ascenseur.direction = None  # Réinitialisation de la direction
        self.ascenseur.etage = 2
        self.ascenseur.appels = [1]
        self.ascenseur.choisir_direction()
        self.assertEqual(self.ascenseur.direction, 'bas')

        # Cas où la direction est initialement None, et les deux listes sont vides
        self.ascenseur.direction = None  # Réinitialisation de la direction
        self.ascenseur.choisir_direction()
        self.assertIsNone(self.ascenseur.direction)

        # Cas où la direction est initialement None, et il y a des appels
        self.ascenseur.direction = None
        self.ascenseur.etage = 0
        self.ascenseur.destinations = [2]
        self.ascenseur.choisir_direction()
        self.assertEqual(self.ascenseur.direction, 'haut')

        # Cas où la direction est initialement None, mais il y a des destinations
        self.ascenseur.direction = None  # Réinitialisation de la direction
        self.ascenseur.etage = 2
        self.ascenseur.destinations = [1]
        self.ascenseur.choisir_direction()
        self.assertEqual(self.ascenseur.direction, 'bas')

       
        
    def test_appel_ascenseur(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2])
        self.u3.appelerAscenseur(self.ascenseur)
        self.assertEqual(self.ascenseur.appels, [2, 0])
    
    def testEntrerAscenseur(self):
        self.u1.entrerAscenseur(self.ascenseur,testMax=True)
        self.u2.entrerAscenseur(self.ascenseur,testMax=True)
        self.u3.entrerAscenseur(self.ascenseur,testMax=True)
        self.u4.entrerAscenseur(self.ascenseur,testMax=True)
        self.u5.entrerAscenseur(self.ascenseur,testMax=True)

        # Récupération du print d'information d'ascenseur deja complet
        captured_output = StringIO()
        sys.stdout = captured_output
        self.u6.entrerAscenseur(self.ascenseur,testMax=True)
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        # Test du print d'information d'ascenseur deja complet
        self.assertEqual(output.strip(), f"Ascenseur plein,{self.u6.nom} doit attendre quelque minutes")

    def test_entrer_ascenseur(self):
        self.u1.entrerAscenseur(self.ascenseur,testMax=True)
        self.assertEqual(self.ascenseur.destinations, [5])
        
        self.u1.entrerAscenseur(self.ascenseur,testMax=False)
        self.assertEqual(self.ascenseur.destinations, [])

    def test_meme_destination(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.u2.appelerAscenseur(self.ascenseur)
        self.u3.appelerAscenseur(self.ascenseur)
        self.u4.appelerAscenseur(self.ascenseur)
        self.u5.appelerAscenseur(self.ascenseur)

        self.u1.entrerAscenseur(self.ascenseur,testMax=True)
        self.u2.entrerAscenseur(self.ascenseur,testMax=True)
        self.u3.entrerAscenseur(self.ascenseur,testMax=True)
        self.u4.entrerAscenseur(self.ascenseur,testMax=True)
        self.u5.entrerAscenseur(self.ascenseur,testMax=True)

        self.assertEqual(self.ascenseur.destinations, [5, 6, 1])


    def test_choisir_direction(self):
        self.u1.appelerAscenseur(self.ascenseur)
        self.u1.entrerAscenseur(self.ascenseur,testMax=True)
        self.ascenseur.choisir_direction()
        self.assertEqual(self.ascenseur.direction, "haut")

    def test_monter_descendre(self):
        
        self.ascenseur.monter_descendre()
        self.assertEqual(self.ascenseur.etage, 1)
        self.ascenseur.monter_descendre()
        self.assertEqual(self.ascenseur.etage, 2)

        self.assertEqual(self.ascenseur.destinations, [5,6])
        self.assertEqual(self.ascenseur.appels, [])
        self.assertEqual(self.ascenseur.direction, "haut")


if __name__ == '__main__':
    unittest.main()