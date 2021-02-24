### Creating and Activating a New Environment
`conda create --name ENVNAME`

`conda activate ENVNAME`

`conda install PKGNAME`

#### Notes

1. Remember to install jupyter and jupyter lab.
2. Installing pandas will install numpy and matplotlib as dependencies.
3. Search install instructions if there are errors.

### Installing New Packages to Environment
Open a new terminal tab.

`conda activate ENVNAME`

`conda install PKGNAME`

#### Exporting EVN
`conda env export --name ENVNAME > envname.yml`

#### Creating Enviroment From YAML File
`conda env create --file envname.yml`





