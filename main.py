from classes import Category


def main():
    food_category = Category("Food", 1000)
    clothing_category = Category("Clothing", 500)
    car_category = Category("Car Expenses", 600)

    print(food_category.deposit(250))

    print(food_category.category_balance())

    print(food_category.check_balance(200))

    print(food_category.withdraw(200))

    print(car_category.category_balance())

    print(food_category.category_balance())

    print(clothing_category.category_balance())

    food_category.transfer(500, clothing_category)

    print(food_category.category_balance())
    
    print(clothing_category.category_balance())


if __name__ == "__main__":
    main()
