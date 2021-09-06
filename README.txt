Au début j'étais parti sur une approche(similarity.py) ou je calculais un pourcentage de ressemblance et gardais le pourcentage max.
Le problème de cette méthode est qu'elle prend énormément de temps à calculer.
En effet 10 000 tests prenaient 92 secondes, sachant qu'il faut looper sur 2 csv de plus de 10 000 lignes chacun ...
Ainsi j'avais ensuite prévue de looper sur des fractions de csv pour gagner du temps. En utilisant autoML pour séparer
les produits en département, mais ça aurait pris un temps énorme également.

La solution actuelle(similiraty_2.py) vient d'un constat que les produits uber eats sont en fait un concaténation du nom du produit
avec le nom de la marque puis le grammage. La concaténation se fait en exécutant le fichier create_new_libelle.py
À noter que j'ajoute un espace entre la quantité du grammage et son unité car cela est souvent le cas dans uber eats.
Exemple: on a souvent '280g' dans franprix et '280 g' dans uber eats
Par contre des fois ce n'est pas le cas, ainsi créer également une colonne libéllé pour uber eats ou on met un espace
après à chaque fois ou pas du tout serait mieux niveau performances.

J'ai remarqué des erreurs dans l'ortographe de certains mots dans le fichier franprix, une distance de levenshtein
pourrait régler ce soucis. Par contre cela rallongerait énormément le temps de calcul.

La comparaison des strings en mode lower a permis de multiplier par presque 2 le nombres de correspondances, mais aussi
le temps de calcul(voire bien plus). Pour gagner en temps de calcul il serait intéréssant de créer un colonne avec les
libéllés déjà en minuscule(et non faire un .lower() dans une double boucle).

comparaison sans traitement -> 3577 eans trouvés                                            14.81%
comparaison avec les libéllés en minuscules -> 7932 eans trouvés                            32.84%
comparaisons avec les libéllés sans accent (et en minusucle) -> 11610 eans trouvés          48.07 %
comparaisons des libélles en supprimant tous les espaces -> 11670 eans trouvés              48.32 %
comparaisons en utilisant la distance de levenshtein taille 1 -> 12644 eans trouvés         52.35 %
                                                     taille 2 -> 13743 eans trouvés         56.90 %
                                                     taille 3 -> 15180 eans trouvés         62.85 %
                                                     taille 4 -> 15693 eans trouvés         64.97 %
                                                     taille 5 -> 17027 eans trouvés         70.50 %
                                                     taille 6 -> 18045 eans trouvés         74.71 %
                                                     taille 7 -> 19032 eans trouvés         78.80 %
                                                     taille 8 -> 20252 eans trouvés         83.85 %
                                                     taille 9 -> 21308 eans trouvés         88.22 %
                                                    taille 10 -> 22056 eans trouvés         91.32 %
                                                    taille 11 -> 22626 eans trouvés         93.68 %
                                                    taille 12 -> 22948 eans trouvés         95.01 %
                                                    taille 13 -> 23284 eans trouvés         96.41 %
                                                    taille 14 ->

à noter qu'une distance de levenshtein trop grande dégrade l'accuracy

Levenshtein.distance('poire', 'pomme') -> 2
'jus de poire' et 'jus de pomme' seraient problématiques pour une distance de 2 ou plus
