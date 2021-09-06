import pandas as pd
import os


def read_csv(path, cols):
    return pd.read_csv(path, delimiter=';', usecols=cols)


def read_excel(path, cols):
    return pd.read_excel(path, usecols=cols)


def return_data(path, cols=None):
    name, extension = os.path.splitext(path)
    if extension == '.csv':
        return read_csv(path, cols)
    elif extension == '.xlsx':
        return read_excel(path, cols)
    else:
        raise Exception("Format de fichier non reconnu")


def delete_duplicates(data, col_reference):
    return data.drop_duplicates(subset=col_reference)


def delete_null_values(data, col):
    return data[data[col] != ' ']


def sort_values(data, col):
    return data.sort_values(by=col)


# Problème dans la répartition
# plus utilisé
def return_classes_price(data_1, data_2):
    '''
    0-1 0-2
    1-2 1-4
    2-4 2-8
    4-6 4-12
    6-10 6-20
    10-+inf 10-+inf
    '''
    repartition_1 = [0, 2, 4, 6, 8, 12, 20, 9999999999]
    repartition_2 = [0, 1, 2, 3, 4, 6, 10, 99999999999]

    result_1 = []
    result_2 = []

    for i, j in zip(repartition_1, repartition_2):
        print(f'i: {i}, j: {j}')
        result_1.append(data_1.loc[(data_1['price'] > i) & (data_1['price'] < i+1)])
        result_2.append(data_2.loc[(data_2['product_price_fp'] > j) & (data_2['product_price_fp'] < j+1)])

    return result_1, result_2


def return_classes_quantity(data, name_col):
    pass
