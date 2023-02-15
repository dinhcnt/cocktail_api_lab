import requests

def drinks_by_name(name):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
    response = requests.get(url)
    return response.json()

def drink_by_id(drink_id):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    response = requests.get(url)
    return response.json()

def extract_api_drink(drink_response):
    drink = drink_response['drinks'][0]
    id = drink['idDrink']
    name = drink['strDrink']
    instructions = drink['strInstructions']
    main_ingredient = drink['strIngredient1']
    return {'id': id, 'name': name, 'instructions': instructions, 'main_ingredient': main_ingredient}

def extract_ingredients(drink_response):
    drink = drink_response['drinks'][0]
    ingredients = [drink[f'strIngredient{ingredient_num + 1}'] for ingredient_num in range(15) if drink[f'strIngredient{ingredient_num + 1}']]
    return {'name': drink['strDrink'], 'ingredients': ingredients}
    
def extract_ingredients_and_amounts(drink_response):
    drink = drink_response['drinks'][0]
    ingredients = [drink[f'strIngredient{ingredient_num + 1}'] for ingredient_num in range(15) if drink[f'strIngredient{ingredient_num + 1}']]
    
    amounts = [drink[f'strMeasure{ingredient_num + 1}'] for ingredient_num in range(15) if drink[f'strMeasure{ingredient_num + 1}']]
    ingredient_pairs = list(zip(ingredients, amounts))
    return {'name': drink['strDrink'], 'ingredients_amounts': ingredient_pairs}

def coerce_ingredients_amounts(ingredients_amounts):
    return [(ingredient, int(amount.split(' ')[0]))for ingredient, amount in ingredients_amounts]
