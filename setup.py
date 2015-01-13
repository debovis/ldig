from setuptools import setup, find_packages
import sys, os

version = '1.0.0'

setup(name='ldig',
      version=version,
      description="ldig",
      long_description=""" """,
      classifiers=[], 
      keywords='language detection',
      author='Author',
      author_email='author@author.com',
      url='https://github.com/debovis/ldig',
      license='BSD',
      packages=find_packages(exclude=[]),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'numpy',
      ],
      entry_points= {},
      )