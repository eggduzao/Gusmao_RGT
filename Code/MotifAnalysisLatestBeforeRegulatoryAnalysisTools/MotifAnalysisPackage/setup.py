import os
from setuptools import setup, find_packages
version = "0.0.1"
README = os.path.join(os.path.dirname(__file__), "README.txt")
long_description = open(README).read() + "nn"
setup(name="MotifAnalysisPackage",
      version=version,
      description=("Motif analysis package under construction"),
      long_description=long_description,
      #classifiers=[
      #    'Topic :: Scientific/Engineering :: Bio-Informatic',
      #    'Topic :: Scientific/Engineering :: Artificial Intelligence'
      #    ],
      keywords='tfbs',
      author='Eduardo G. Gusmao',
      author_email='eduardo.gusmao@rwth-aachen.de',
      license='GPL',
      packages=find_packages(),
      entry_points = {
          'console_scripts': [
              'motifStatistics = motifStatistics.motifStatistics:main'
          ]
      },
      install_requires=['numpy','scipy','Biopython','pandas','fisher','statsmodels','HTML','matplotlib']
      )
