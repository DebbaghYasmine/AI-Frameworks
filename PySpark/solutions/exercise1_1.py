protocols = csv_data.map(lambda x: x[1]).distinct()
services = csv_data.map(lambda x: x[2]).distinct()
combinations = protocols.cartesian(services).collect()
n_combination = len(combinations)
print("Il y a %d combinaisons de protocol X service"% n_combination)