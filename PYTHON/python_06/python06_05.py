def phare_rdc_week(x,y):
    h_phare= x * y / 100
    trajet_jour= h_phare *5 * 2
    trajet_semaine = trajet_jour * 7
    resultat = print("Pour " , x ," marches de ", y , "cm, le gardien parcourt ", trajet_semaine , " m.")
    return resultat 
phare_rdc_week(10,20)