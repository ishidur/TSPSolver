# TSPSolver
Neural Network approaches for the Traveling Salesman Problem.
- Hopfield Network  
![Hopfield net](https://github.com/ishidur/TSPSolver/blob/develop/results/random_10_cities/hopfield_net/animation.gif)
- Elastic Nets  
![Elastic nets](https://github.com/ishidur/TSPSolver/blob/develop/results/djibouti/elastic_nets/animation.gif)
- Self-organizing map  
![Self-organizing map](https://github.com/ishidur/TSPSolver/blob/develop/results/djibouti/self_organizing_map/animation.gif)

# Environment
|package|version|
|:--|:--:|
|python|3.7|
|matplotlib|3.1.1|
|numpy|1.17.0|
|pandas|0.25.0|
|imagemagick (optional)|7.0.7|
  
## Install with [Pipenv](https://docs.pipenv.org)  
This project is using Pipenv, popular package manager in Pyhton.
In the project directory, run the following commands:  
```
pip install pipenv
pipenv install
```  
If you are contributer, please install with `--dev` flag
```
pipenv install --dev
```

## (Optional) Install [imagemagick](https://www.imagemagick.org/script/index.php)  
If you want to save result as gif, imagemagick is required.  
### Install with [Homebrew](https://brew.sh/index.html) (for macOS)  
Run the following command: 
```
brew install imagemagick
```
### Install with [Chocolatey](https://chocolatey.org/about) (for Windows)  
Run the following command: 
```
choco install imagemagick
```
### Install from source and binary distributions    
Check this out  
[source](https://www.imagemagick.org/script/install-source.php)  
[binary distributions](https://www.imagemagick.org/script/download.php)
