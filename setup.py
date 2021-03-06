import io
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    readme = f.read()

with io.open("fileNameTranslation/__version__.py", "r") as f:
    version = re.search(r"^__version__\s*=\s*[\"']([^\"']*)[\"']$", f.read(), re.MULTILINE).group(1)

with io.open(os.path.join(here, 'CHANGELOG.rst'), encoding='utf-8') as f:
    changelog = f.read()

setup(
        name="fileNameTranslation",
        version=version,
        description="This package will allow you to translate your file names to you desire language",
        long_description=readme + "\n\n" + changelog,
        url="https://github.com/aviadlevy/fileNameTranslation/",
        classifiers=["Development Status :: 2 - Pre-Alpha",
                     "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                     "Operating System :: OS Independent",
                     "Intended Audience :: End Users/Desktop",
                     "Programming Language :: Python :: 2.7",
                     "Topic :: Desktop Environment :: File Managers",
                     ],
        author="Aviad Levy",
        author_email="aviadlevy1@gmail.com",
        license="LGPLv3",
        packages=["fileNameTranslation"],
        install_requires=[
              "googletrans"
        ],
        entry_points={
            "console_scripts": [
                "fileNameTranslation = fileNameTranslation.__main__:main"
            ],
        },
        zip_safe=True)
