def tower_builder(n_floors):
    # build here
    n=n_floors-1
    tower = []
    for j in range(n_floors):
        tower.append((n-j) * " " + j * "*" + "*" + j * "*" + (n-j) * " ")
    
    return tower
    
    
        