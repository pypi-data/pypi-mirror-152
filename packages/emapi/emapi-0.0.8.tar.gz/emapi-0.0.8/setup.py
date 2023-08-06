#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   Copyright 2017 Federico Cerchiari <federicocerchiari@gmail.com>
#
#   this file is part of emapi
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import os
import sys
from shutil import rmtree
from pathlib import Path

from emapi import __version__

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "emapi"
DESCRIPTION = "Event-Models based api framework."
URL = "https://github.com/Hrabal/Emapi"
EMAIL = "federicocerchiari@gmail.com"
AUTHOR = "Federico Cerchiari"
REQUIRES_PYTHON = ">=3.3"
VERSION = __version__

REQUIRED = ["starlette", "tem-py", "tortoise-orm", "orjson", "PyYAML"]
EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))
long_description = (Path(__file__).parent / "README.md").read_text()


class UploadCommand(Command):
	"""Support setup.py upload."""

	description = "Build and publish the package."
	user_options = []

	@staticmethod
	def status(s):
		print(f"\033[1m{s}\033[0m")

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		try:
			self.status("Removing previous builds…")
			rmtree(os.path.join(here, "dist"))
		except OSError:
			pass

		self.status("Building Source and Wheel (universal) distribution…")
		os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

		self.status("Uploading the package to PyPI via Twine…")
		os.system("twine upload dist/*")

		self.status("Pushing git tags…")
		os.system(f"git tag v{__version__}")
		os.system("git push --tags")

		sys.exit()


# Where the magic happens:
setup(
	name=NAME,
	version=__version__,
	description=DESCRIPTION,
	long_description=long_description,
	long_description_content_type="text/markdown",
	author=AUTHOR,
	author_email=EMAIL,
	python_requires=REQUIRES_PYTHON,
	url=URL,
	packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
	install_requires=REQUIRED,
	extras_require=EXTRAS,
	include_package_data=True,
	license="APACHE 2.0",
	classifiers=[
		"License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: Implementation :: PyPy",
		"Topic :: Internet :: WWW/HTTP :: HTTP Servers",
		"Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
	],
	cmdclass={"upload": UploadCommand,},
)
