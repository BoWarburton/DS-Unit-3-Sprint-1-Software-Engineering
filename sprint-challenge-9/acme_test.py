#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        # print(f'Price is {prod.price}')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight being 20"""
        prod = Product('Test Product')
        # print(f'Weight is {prod.weight}')
        self.assertEqual(prod.weight, 20)
    
    def test_default_stealability(self):
        """Test stealability works"""
        prod = Product('Test Product', 5, 1, 5.2)
        # print(f'Stealability is {prod.stealability()}')
        self.assertEqual(prod.stealability(), 'Very stealable!')
    
    def test_explode(self):
        """Test default explode is ...boom""" 
        prod = Product('Test Product')
        # print(f'Explode is {prod.explode()}')
        self.assertEqual(prod.explode(), '...boom!')

class AcmeReportTests(unittest.TestCase):
    """Making sure the test reports work correctly"""
    def test_default_num_products(self):
        """Check that it receives list of length 30"""
        product_list = generate_products()
        # print(f'How many products? {len(product_list)}')
        self.assertEqual(len(product_list), 30)
    
    def test_legal_names(self):
        """Generated names all have adjective, noun, space"""
        product_list = generate_products()
        i = 0
        while i < len(product_list):
            self.assertIn(' ', product_list[i].name)
            i += 1

if __name__ == '__main__':
    unittest.main()