import os
from setuptools import setup, find_packages
version = "1.0.0"
README = os.path.join(os.path.dirname(__file__), "README.txt")
long_description = open(README).read() + "nn"
setup(name="MyPackage",
      version=version,
      description=("Example package that dows very complex mathematical operations"),
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python",
        ("Topic :: Software Development :: Libraries :: Python Modules")],
      keywords='weird math',
      author='Eduardo G. Gusmao',
      author_email='eduardo.gusmao@rwth-aachen.de',
      url='http://www.google.com',
      license='GPL',
      packages=find_packages(),
      entry_points = {
          'console_scripts': [
              'MyPackage = myMath.main:main'
          ]
      },
      install_requires=['numpy','scipy']
      )
