import numpy as np

city_num = 15
file_path = './coordinates/'
output_file = 'random_' + str(city_num) + '_cities.csv'

if __name__ == "__main__":
    # “continuous uniform” distribution random
    np_cities = np.random.random((city_num, 2))
    np.savetxt(file_path + output_file, np_cities, delimiter=',')
