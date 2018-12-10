# Installation
1. Follow instructions to install gdx-pandas and its dependencies: https://github.com/NREL/gdx-pandas#install
1. Install this package from your command line: `pip install git+https://github.com/mmowers/valuestreams.git@master`
    * If you are doing development, consider using this instead: `pip install -e git+https://github.com/mmowers/valuestreams.git@master#egg=valuestreams`

# Use
1. Import the module in python: `import valuestreams`
1. Call the function `get_value_streams` (with an optional variable list to filter results to only certain variables): `df = valuestreams.get_value_streams('path_to_gdx_file.gdx', 'path_to_mps_file', optional_var_list)`

# Upgrade package to latest
1. `pip install --upgrade valuestreams`

# Uninstall package
1. `pip uninstall valuestreams`
