from UI import *
from description_city import *
from description_build import *
from description_event import *
user_choice = ""
inhabitant = [{"name": "Ivan", "surname": "Ivanov", "age": 23, "occupation": "smithy", "religion": "christian", "family": "Yes"},
              {"name": "Ivan", "surname": "Petrov", "age": 27, "occupation": "builder", "religion": "christian", "family": "No"},
              {"name": "Oleg", "surname": "Ivanov", "age": 10, "religion": "christian", "family": "Yes"},
              {"name": "Mariya", "surname": "Ivanova", "age": 21, "occupation": "cook", "religion": "christian", "family": "Yes"},
              {"name": "Achmed", "surname": "Muradov", "age": 33, "occupation": "doctor", "religion": "muslim", "family": "Yes"},
              {"name": "Rustam", "surname": "Muradov", "age": 3, "occupation": "doctor", "religion": "muslim", "family": "No"},
              {"name": "Sergey", "surname": "Sokolov", "age": 71, "occupation": "teacher", "religion": "christian", "family": "No"}
              ]
buildings = [{"name": "storage", "type": "storehouse", "year": 450},
             {"name": "Ai_Bolit", "type": "hospital", "year": 473},
             {"name": "my_home", "type": "house", "year": 499},
             {"name": "Kyznya", "type": "smithy", "year": 479},
             {"name": "in_god_we_trust", "type": "temple", "year": 300}]
event = [{"name": "city_day", "date": 22.08},
         {"name": "day_of_light", "date": 13.10},
         {"name": "knights tournament", "date": 02.03},
         {"name": "new_harvest_day", "date": 29.09},
         {"name": "execution", "date": 11.01}]
while user_choice != 000:
    menu()
    user_choice = input()
    if user_choice == "1":
        new_resident = {}
        print(adding_resident(inhabitant, new_resident))
        #набросок! нет решения"
    if user_choice == "2":
        print(elder(inhabitant))
    if user_choice == "3":
        age = int(input("Ввести возраст "))
        print(if_child(inhabitant, age))
    if user_choice == "4":
        occupation = input("Введите профессию ")
        print(get_count_occupation(inhabitant, occupation))
    if user_choice == "5":
        religion = input("Введите религию ")
        print(count_religion(inhabitant, religion))
    if user_choice == "7":
        type = str(input("Ввести тип здания "))#как привести к разному регистру строку, чтобы можно было вводить и строчные, и прописные буквы
        print(get_count(buildings, type))
    if user_choice == "8":
        wish_year = int(input("Введите год "))
        print(get_old_buildings(buildings, wish_year))
    if user_choice == "9":
        data = int(input("Введите дату в формате мм "))
        print(get_next_event(data, event))


