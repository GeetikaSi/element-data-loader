#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import urllib.request

pkg_name = next(p for p in find_packages() if '.' not in p)
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

with urllib.request.urlopen('https://raw.githubusercontent.com/flatironinstitute/CaImAn/master/requirements.txt') as f:
   caiman_requirements = f.read().decode('UTF-8').split('\n')
caiman_requirements.remove('')

with open(path.join(here, pkg_name, 'version.py')) as f:
    exec(f.read())

setup(
    name=pkg_name.replace('_', '-'),
    version=__version__,
    description="Loaders of neurophysiological data into the DataJoint Elements",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='DataJoint',
    author_email='info@datajoint.com',
    license='MIT',
    url=f'https://github.com/datajoint/{pkg_name.replace("_", "-")}',
    keywords='neuroscience calcium-imaging science datajoint',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    scripts=[],
    install_requires=requirements,
    extras_require={
        'scanreader': ['scanreader@git+https://github.com/atlab/scanreader.git'],
        'sbxreader': ['sbxreader==0.1.6.post1'],
        'suite2p': ['suite2p@git+https://github.com/MouseLand/suite2p.git'],
        'caiman_requirements': caiman_requirements,
        'caiman': ['h5py==3.3.0',
                   'scipy==1.7.0',
                   'caiman@git+https://github.com/flatironinstitute/CaImAn.git@v1.8.9'],
    }
    # TODO suite2p - issue with current pypi version, github version works, change to pypi once issue is resolved and version lock
)
