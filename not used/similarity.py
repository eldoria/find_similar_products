from config import *
import time


def return_similarity(p1, p2):
    return nlp(p1).similarity(nlp(p2))


def print_similarity(p1, p2):
    print(f"{p1} <-> {p2}: {return_similarity(p1, p2)}")


def loop_over_data(list_data_1, list_data_2, cap):
    for data_1 in list_data_1: # sous-tableau du tab 1
        for data_2 in list_data_2: # sous tableau du tab 2
            for product_1 in data_1['product_name']: # produits Uber Eats
                for product_2 in data_2['product_name']: # produits Franprix
                    similarity = return_similarity(product_1, product_2)
                    if similarity > cap:
                        print(f"{product_1} <-> {product_2}: {similarity}")


def loop_over_arrays(data_1, data_2):
    print("Début fonction")
    i = 0
    start = time.time()
    nb_instructions = 10000
    for d1 in data_1['product_name']:
        for d2 in data_2['product_name']:
            similarity = return_similarity(d1, d2)
            i += 1
            if i > nb_instructions:
                print(f"Time take for {nb_instructions} instructions: {time.time() - start}")
                exit()
