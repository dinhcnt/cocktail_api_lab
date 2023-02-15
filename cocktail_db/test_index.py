
from index import (drinks_by_name, drink_by_id, extract_api_drink,
 extract_ingredients, extract_ingredients_and_amounts, coerce_ingredients_amounts)
from data import strawberry_margarita
def test_drinks_by_name_returns_matching_drinks():
    returned_drinks = drinks_by_name('old fashioned')
    assert len(returned_drinks['drinks']) == 1

def test_drinks_by_id_returns_specified_drink():
    returned_drink = drink_by_id(12322)
    assert returned_drink['drinks'][0]['idDrink'] == '12322'

def test_extract_api_drink():
    drink_summary = extract_api_drink(strawberry_margarita)
    assert drink_summary == {'id': '12322', 'name': 'Strawberry Margarita', 'instructions': 'Rub rim of cocktail glass with lemon juice and dip rim in salt. Shake schnapps, tequila, triple sec, lemon juice, and strawberries with ice, strain into the salt-rimmed glass, and serve.', 'main_ingredient': 'Strawberry schnapps'}

def test_extract_ingredients():
    assert extract_ingredients(strawberry_margarita) == {'name': 'Strawberry Margarita', 
    'ingredients': ['Strawberry schnapps', 'Tequila', 'Triple sec', 'Lemon juice', 'Strawberries', 'Salt']}

def test_extract_ingredients_and_amounts():
    ingredients_amounts = extract_ingredients_and_amounts(strawberry_margarita) 
    assert ingredients_amounts == {'name': 'Strawberry Margarita', 
    'ingredients_amounts': [('Strawberry schnapps', '1/2 oz '), ('Tequila', '1 oz '),
     ('Triple sec', '1/2 oz '), ('Lemon juice', '1 oz '), ('Strawberries', '1 oz ')]}

def test_numeric_amounts():
    ingredients_amounts = [('Strawberry schnapps', '1 oz '), ('Tequila', '1 oz '), ('Triple sec', '2 oz '),
     ('Lemon juice', '1 oz '), ('Strawberries', '1 oz ')]
    coerced_amounts = coerce_ingredients_amounts(ingredients_amounts)
    assert coerced_amounts == [('Strawberry schnapps', 1), ('Tequila', 1), ('Triple sec', 2), ('Lemon juice', 1), ('Strawberries', 1)]


