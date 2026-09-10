telenovelas = {
    'colombianas': {
     'amor': 'gata salvaje',
     'suspenso': 'el monchi',
     'terror': ['septima puerta', 'los sepultureros'],
     'coo_actores': ('carlos', 'cesar', 'jairo'),

     },
    'mexicanas': {

       'amor': 'teresa',
       'suspeso': 'el rey de los cielos',
       'terror': 'despues del ultimo no hay nadie ',

    }
    
}

print(type(telenovelas))
print(telenovelas)

print(telenovelas.keys())
print(telenovelas.values())
print(telenovelas.items())

print(telenovelas)
telenovelas["suspenso"] = "la saga"
print(telenovelas)

