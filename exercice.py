#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    big_list = []
    if values is None:
        # TODO: demander les valeurs ici
        while len(big_list) < 10:
            based = input("écrire les valeurs ici: ")
            big_list.append(based)

    list_nombres = [float(i) for i in big_list if i.isdigit()]
    list_lettres = [j for j in big_list if not j.isdigit()]
    sorted_list = sorted(list_nombres) + sorted(list_lettres)
    return sorted_list


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = [input("Écrit le mot icite stp: ") for i in range(2)]

    return len(words[0]) == len(words[1])



def contains_doubles(items: list) -> bool:
    for item in items:
        if items.count(item) > 1:
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        average = sum(value)/len(value)

        if len(best_student) == 0 or list(best_student.values())[0] < average:
            best_student = {key: average}
    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    sentence = sentence.lower()
    dictionnaire_de_lettre = dict()
    for letter in sentence:
        if letter not in dictionnaire_de_lettre:
            dictionnaire_de_lettre[letter] = 1
        else:
            dictionnaire_de_lettre[letter] += 1

    dict_trier = sorted(dictionnaire_de_lettre.items(), key=(lambda x: x[1]), reverse=True)
    for caracter in dict_trier:
        if caracter[1] > 5:
            print(f"Le caractère {caracter[0]} revient {caracter[1]} fois.")
        else:
            return dictionnaire_de_lettre
    #       Retourner le tableau de lettres
    return dictionnaire_de_lettre


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom_recette = input("Ecrire le nom de la recette: ")
    ingredients = input("Ecrire les ingredients (separe par ,): ").split(",")
    return {nom_recette: ingredients}

def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom_recette = ""
    while True:
        if nom_recette in ingredients:
            break
        else:
            print("Cette recette nest pas dans le livre.")
            nom_recette = input("Ecrire un nom de recette: ")
    print(ingredients[nom_recette])

def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
