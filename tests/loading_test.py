'''
test to se if we can load the data at least

'''


import unittest
from repoNoData import image_operations as im
from utils import test_utils as tu



class LoadingTest(unittest.TestCase):
    def test_load_relativity(self):
        out = im.LinearOperations(
            tu.get_test_data_path("220px-Escher's_Relativity.jpg"))
        self.assertEqual(out.get_image().shape,(209,220))

    def test_load_day_and_night(self):
        out = im.LinearOperations(
            tu.get_test_data_path("day_and_night.jpg"))
        self.assertEqual(out.get_image().shape,(902,1566))

    def test_load_pencil_sketch(self):
        out = im.LinearOperations(
            tu.get_test_data_path("escher_pencil_sketch_by_psion005.jpg"))
        self.assertEqual(out.get_image().shape,(768,1024))
        
    def test_load_artwork(self):
        out = im.LinearOperations(
            tu.get_test_data_path("M-C-font-b-Escher-b-font-Optical-illusion"
                                  "-artworks-geometry-animals-chameleon-"
                                  "poster-60x60CM-Print.jpg"))
        self.assertEqual(out.get_image().shape,(600,600))
        
    def test_load_swans(self):
        out = im.LinearOperations(tu.get_test_data_path("swans.jpg"))
        self.assertEqual(out.get_image().shape,(600,600))

if __name__ == "__main__":
    unittest.main()
