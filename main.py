# from similarity import *
from similarity_2 import *
# from composition import *
from return_data import return_data, sort_values

data_uber_eats = return_data('data/cleaned/produits_uber_eats_cleaned.csv')
data_franprix = return_data('data/cleaned/produits_franprix_cleaned.csv', ['ean', 'product_name_final'])

add_ean_v3(data_franprix=data_franprix, data_uber_eats=data_uber_eats, dist_levenshtein=14)
exit()

sort_values(data_uber_eats, 'price')
sort_values(data_franprix, 'product_price_fp')

