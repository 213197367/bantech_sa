from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bantech_sa/__init__.py
from bantech_sa import __version__ as version

setup(
	name="bantech_sa",
	version=version,
	description="bantech.sa",
	author="bandar",
	author_email="bandaralmutiri.10@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
