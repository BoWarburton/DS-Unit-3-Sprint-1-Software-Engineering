#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

# print(ADJECTIVES)
# print(NOUNS)

def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        new_name = ''
        new_name += sample(ADJECTIVES, 1)[0]
        new_name += ' '
        new_name += sample(NOUNS, 1)[0]
        new_product = Product(new_name, randint(5, 101), randint(5, 101), uniform(0.0, 2.5))
        products.append(new_product)
    return products

def inventory_report(products):
    """Loop over products to calculate # of unique product names and mean price, weight, flammability"""
    unique_names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0
    num_products = len(products)
    for i in range(num_products):
        if products[i].name not in unique_names:
            unique_names.append(products[i].name) 
        total_price += products[i].price
        total_weight += products[i].weight
        total_flammability += products[i].flammability
    mean_price = total_price / num_products
    mean_weight = total_weight / num_products
    mean_flammability = total_flammability / num_products
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(unique_names)}')
    print(f'Average price: {mean_price}')
    print(f'Average weight {mean_weight}')
    print(f'Average flammabilitiy {mean_flammability}')
    return unique_names, mean_price, mean_weight, mean_flammability

if __name__ == '__main__':
    inventory_report(generate_products())