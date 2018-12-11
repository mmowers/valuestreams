## Install package
1. Follow instructions to install gdx-pandas and its dependencies: https://github.com/NREL/gdx-pandas#install
1. Install this package from your command line: `pip install git+https://github.com/mmowers/valuestreams.git@master`
    * If you are doing development, consider using this instead: `pip install -e git+https://github.com/mmowers/valuestreams.git@master#egg=valuestreams`

## Use
1. Import the module in python: `import valuestreams`
1. Call the function `get_value_streams` (with an optional variable list and constraint list to filter results, using *lowercased* variable and constraint names): `df = valuestreams.get_value_streams('path_to_gdx_file.gdx', 'path_to_mps_file', optional_var_list, optional_con_list)`
    * For more information on inputs and outputs of `get_value_streams()`, see the docstring comment section at the top of this function in `__init__.py`

## Upgrade package to latest
1. `pip install --upgrade git+https://github.com/mmowers/valuestreams.git@master`
    * This command won't work if you installed using `pip install -e...`. Instead, find the location of the valuestreams package with the `pip list` command at the command line, and then simply navigate to this git repo and pull the latest from git.

## Uninstall package
1. `pip uninstall valuestreams`
