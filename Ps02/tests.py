import unittest

from rail_fence import *
from matrix_shift import *
from caesar import *
from vigenere import *


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(railfence_encode("CRYPTOGRAPHY", 3), "CTARPORPYYGH")
        self.assertEqual(railfence_decode("CTARPORPYYGH", 3), "CRYPTOGRAPHY")
        self.assertEqual(railfence_encode("ALAMAKOTAMMM", 3), "AAALMKTMMAOM")
        self.assertEqual(railfence_decode("AAALMKTMMAOM", 3), "ALAMAKOTAMMM")

    def test_2a(self):
        self.assertEqual(encode_2a("CRYPTOGRAPHY", "3-4-1-5-2"), "YPCTRRAOPGHY")
        self.assertEqual(decode_2a("YPCTRRAOPGHY", "3-4-1-5-2"), "CRYPTOGRAPHY")
        self.assertEqual(encode_2a("CRYPTOGRAPHYOSA", "3-1-4-2"), "YCPRGTROHAYPAOS")
        self.assertEqual(decode_2a("YCPRGTROHAYPAOS", "3-1-4-2"), "CRYPTOGRAPHYOSA")
        self.assertEqual(encode_2a("ALAMAKOTAMMM", "3-1-4-2"), "AAMLOATKMAMM")
        self.assertEqual(decode_2a("AAMLOATKMAMM", "3-1-4-2"), "ALAMAKOTAMMM")

    def test_2b(self):
        self.assertEqual(encode_2b("HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION", "CONVENIENCE"), "HECRNCEYIISEPSGDIRNTOAAESRMPNSSROEEBTETIAEEHS")
        self.assertEqual(decode_2b("HECRNCEYIISEPSGDIRNTOAAESRMPNSSROEEBTETIAEEHS", "CONVENIENCE"), "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION")
        self.assertEqual(encode_2b("ALAMAKOTAMMM", "CONVENIENCEMMM"), "AMATMOMAKALM")
        self.assertEqual(decode_2b("AMATMOMAKALM", "CONVENIENCEMMM"), "ALAMAKOTAMMM")

    def test_2c(self):
        self.assertEqual(encode_2c("HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION", "CONVENIENCE"), "HEESPNIRRSSEESEIYASCBTEMGEPNANDICTRTAHSOIEERO")
        self.assertEqual(decode_2c("HEESPNIRRSSEESEIYASCBTEMGEPNANDICTRTAHSOIEERO", "CONVENIENCE"), "HEREISASECRETMESSAGEENCIPHEREDBYTRANSPOSITION")
        self.assertEqual(encode_2c("ALAMAKOTAMMM", "CONVENIENCEMMM"), "ALMMKATMOMAA")
        self.assertEqual(decode_2c("ALMMKATMOMAA", "CONVENIENCEMMM"), "ALAMAKOTAMMM")
    
    def test_3b(self):
        self.assertEqual(caesar_encode("CRYPTOGRAPHY", 5, 7), "TURGIZVUFGCR")
        self.assertEqual(caesar_decode("TURGIZVUFGCR", 5, 7), "CRYPTOGRAPHY")
        self.assertEqual(caesar_encode("ALAMAKOTAMMM", 5, 7), "FEFLFXZIFLLL")
        self.assertEqual(caesar_decode("FEFLFXZIFLLL", 5, 7), "ALAMAKOTAMMM")
    
    def test_4(self):
        self.assertEqual(vigenere_encode("CRYPTOGRAPHY", "BREAK"), "DICPDPXVAZIP")
        self.assertEqual(vigenere_decode("DICPDPXVAZIP", "BREAK"), "CRYPTOGRAPHY")
        self.assertEqual(vigenere_encode("ALAMAKOTAMMM", "BREAK"), "BCEMKLFXAWND")
        self.assertEqual(vigenere_decode("BCEMKLFXAWND", "BREAK"), "ALAMAKOTAMMM")


if __name__ == "__main__":
    unittest.main()