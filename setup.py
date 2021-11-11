from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in installer_scoring/__init__.py
from installer_scoring import __version__ as version

setup(
	name="installer_scoring",
	version=version,
	description="It Works For Installer Scoring",
	author="mani.v@gmail.com",
	author_email="mani.v@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
