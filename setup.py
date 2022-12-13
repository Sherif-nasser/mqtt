from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mqtt/__init__.py
from mqtt import __version__ as version

setup(
	name="mqtt",
	version=version,
	description="na",
	author="na",
	author_email="na",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
