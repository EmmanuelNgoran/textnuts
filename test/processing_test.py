from unittest import TestCase
from textnuts.processing import RegexRuler
from textnuts.processing.matches import MatchesType

class TestRegexProcessing(TestCase):
    
    def test_init(self):
        self.assertEqual(10,int("10"))
        
    def test_regex_transform(self):
        test_str = "My address is emmanuel@ngoran.com"
        reg_type = MatchesType.EMAIL
        reg_ruler = RegexRuler("matcher",[reg_type])
        res_transform = reg_ruler.transform(test_str)
        self.assertEqual("My address is ",res_transform)

