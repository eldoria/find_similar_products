from return_data import delete_null_values
import pandas as pd
import unidecode
import re


data = pd.read_csv('data/brute/produits_franprix.csv', usecols=['ean', 'product_name', 'brand', 'mesure'], sep=';')
data = delete_null_values(data, 'product_name')
# eviter d'avoir des NaN
data['brand'] = data['brand'].fillna('')
data['mesure'] = data['mesure'].fillna('')

data['product_name_final'] = data['product_name'] + ' ' + data['brand'] + ' ' + data['mesure']

# enlever les espaces, accents et majuscules
for libelle_idx, libelle_value in enumerate(data['product_name_final']):
    # libelle_value = re.sub(r"([0-9]+(\.[0-9]+)?)", r" \1 ", libelle_value).strip()
    libelle_value = ''.join(libelle_value.split())
    libelle_value = unidecode.unidecode(libelle_value).lower()
    data['product_name_final'].iloc[libelle_idx] = libelle_value
data.to_csv(path_or_buf='data/cleaned/produits_franprix_cleaned.csv', sep=';', index=False)
