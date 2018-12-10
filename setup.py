from setuptools import setup

setup(name='valuestreams',
      version='0.1',
      description='Create pandas dataframe of value streams from cplex MPS file and GAMS gdx solution file of variable levels and marginals',
      url='http://github.com/mmowers/valuestreams',
      author='Matt Mowers',
      license='MIT',
      packages=['valuestreams'],
      zip_safe=False)