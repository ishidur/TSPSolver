class Files:
    path = './coordinates/'
    qatar = 'qatar.csv'
    western_sahara = 'western_sahara.csv'
    uruguay = 'uruguay.csv'
    djibouti = 'djibouti.csv'
    random_10_cities = 'random_10_cities.csv'
    random_20_cities = 'random_20_cities.csv'
    random_30_cities = 'random_30_cities.csv'


# config
class ENConfig:
    read_file = True
    file_path = Files.path
    city_file = Files.random_20_cities
    city_num = 100


class SOMConfig:
    read_file = True
    file_path = Files.path
    city_file = Files.random_20_cities
    city_num = 30


class HNConfig:
    read_file = True
    file_path = Files.path
    city_file = Files.random_10_cities
    city_num = 30


class GifMakerConfig:
    __path = './results/'
    __problem_set = 'random_30_cities/'
    __en_path = 'elastic_nets/'
    __som_path = 'self_organizing_map/'
    source_dir = __path + __problem_set + __en_path
