niveaux = {
    "0":[False,1,False,False],
    "1":[False,False,2,1],
    "2":[1,3,4,False],
}


niveaux["3"]=[False,False,False,False]


niveaux["3"][1]=5




niveaux_all = {
    "0":{
        "passerelles":[False,1,False,False],
        "blocs":[1,23,345,234,567,2345,456],
        "vie":[3,5],
    }

}

print(niveaux_all["0"]["passerelles"][0])