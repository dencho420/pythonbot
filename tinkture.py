def calculate_ingredients(volume, tincture_choice):
    # Примерные расчеты ингредиентов для трех видов настоек
    base_ingredients = {
        'Лимка': {
            'водка': 550,  # грамм на литр
            'сахар': 200,  # грамм на литр
            'цедра': 100,  # грамм на литр
            'вода' : 200,
            'фрэш' : 200,
            'сливочная аромка' : 0.1
        },
        'Тайга': {
            'джин': 500,
            'сахар': 250,
            'смородина': 300,
            'вода' : 250,
            'лимонная кислота' : 15,
            'ментол' : 0.1
        },
        'Нутелла': {
            'водка': 300,
            'нутелла': 250,
            'аромка': 0.1,
            'молоко' : 300,
            'сливки' : 300
        }
    }

    selected_ingredients = base_ingredients.get(tincture_choice, {})
    ingredients = {ingredient: amount * volume for ingredient, amount in selected_ingredients.items()}
    return ingredients
