class Files:
    qatar = './coordinates/qatar.csv'
    western_sahara = './coordinates/western_sahara.csv'
    uruguay = './coordinates/uruguay.csv'
    djibouti = './coordinates/djibouti.csv'
    random_10_cities = './coordinates/random_10_cities.csv'
    random_30_cities = './coordinates/random_30_cities.csv'


# config
class ENConfig:
    read_file = True
    city_file = Files.random_30_cities
    city_num = 30


class SOMConfig:
    read_file = False
    city_file = Files.random_10_cities
    city_num = 30
