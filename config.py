class Files:
    path = "./coordinates/"
    qatar = "qatar.csv"
    western_sahara = "western_sahara.csv"
    uruguay = "uruguay.csv"
    djibouti = "djibouti.csv"
    random_10_cities = "random_10_cities.csv"
    random_20_cities = "random_20_cities.csv"
    random_30_cities = "random_30_cities.csv"


# config
class ENConfig:
    name = "elastic_nets"
    read_file = True
    file_path = Files.path
    city_file = Files.random_20_cities
    city_num = 100


class SOMConfig:
    name = "self_organizing_map"
    read_file = True
    file_path = Files.path
    city_file = Files.random_20_cities
    city_num = 30


class HNConfig:
    name = "hopfield_net"
    read_file = True
    file_path = Files.path
    city_file = Files.random_10_cities
    city_num = 30


class GifMakerConfig:
    __path = "./results/"
    __problem_set = "random_10_cities/"
    __en_path = "elastic_nets/"
    __som_path = "self_organizing_map/"
    __hn_path = "hopfield_net/"
    source_dir = __path + __problem_set + __hn_path
