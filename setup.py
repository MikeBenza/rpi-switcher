import os
from setuptools import setup

try:
    version = os.environ['VERSION']
except:
    version = "0.0.1"

setup(name='rpi-switcher',
      version=version,
      packages=['switcher']
      author='Mike Benza',
      author_email='mikebenza@gmail.com',
      install_requires=['RPIO'])
