# Installation
1. Follow instructions to install gdx-pandas and its dependencies: https://github.com/NREL/gdx-pandas#install
1. Install this package from your command line: `pip install git+https://github.com/mmowers/.git@newbranch`
  * Consider using the `-e` option to automatically use the latest version on the `master` branch when the module is imported: `pip install -e git+https://github.com/mmowers/valuestreams.git@master`

# Use
1. Import the module in python: `import valuestreams`
1. Call the function `get_value_streams` with optional var_list to filter results to only certain variables: `df = valuestreams.get_value_streams(solution_file, mps_file, var_list)`

# Upgrade package to latest
1. `pip install --upgrade git+https://github.com/mmowers/valuestreams.git@master`

# Uninstall package
1. `pip uninstall valuestreams`
