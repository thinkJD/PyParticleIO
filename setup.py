import codecs
import os


from setuptools import setup, find_packages

__version__ = "0.0.8"
__title__ = "PyParticleIO"
__description__ = "Python module with a class to interface with the ParticleIO cloud"
__uri__ = "https://github.com/youngsoul/PyParticleIO"
__author__ = "Patrick Ryan"
__email__ = "pat_ryan_99@yahoo.com"
__license__ = "Public Domain"
__copyright__ = "Copyright (c) 2016 Patrick Ryan"

###############################################################################

NAME = __title__
PACKAGES = find_packages(where=".")
KEYWORDS = ["ParticleIO", "Photon", "Electron"]
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: Public Domain",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = [
    'requests >= 2.8.1',
    'sseclient >= 0.0.11',
    'hammock >= 0.2.4'
]

###############################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()

if __name__ == "__main__":
    setup(
        name=NAME,
        description=__description__,
        license=__license__,
        url=__uri__,
        version=__version__,
        author=__author__,
        author_email=__email__,
        maintainer=__author__,
        maintainer_email=__email__,
        keywords=KEYWORDS,
        long_description=read("README.rst"),
        packages=PACKAGES,
        package_dir={"": "."},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        scripts=[]
    )