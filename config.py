class Files:
    path = './coordinates/'
    qatar = 'qatar.csv'
    western_sahara = 'western_sahara.csv'
    uruguay = 'uruguay.csv'
    djibouti = 'djibouti.csv'
    random_10_cities = 'random_10_cities.csv'
    random_30_cities = 'random_30_cities.csv'


# config
class ENConfig:
    read_file = True
    file_path = Files.path
    city_file = Files.random_30_cities
    city_num = 30


class SOMConfig:
    read_file = True
    file_path = Files.path
    city_file = Files.random_10_cities
    city_num = 30


class GifMakerConfig:
    __path = './results/random_10_cities/'
    __en_path = 'elastic_nets/'
    __som_path = 'self_organizing_map/'
    source_dir = __path + __en_path
