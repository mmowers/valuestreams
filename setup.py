from setuptools import setup

setup(name='valuestreams',
      version='0.5',
      description='Create pandas dataframe of value streams from cplex MPS file and GAMS gdx file of variable levels and marginals from solution',
      url='http://github.com/mmowers/valuestreams',
      author='Matt Mowers',
      license='MIT',
      packages=['valuestreams'],
      install_requires=[
          'pandas',
          'gdxpds',
          'datetime',
      ],
      zip_safe=False)