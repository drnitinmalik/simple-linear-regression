import io
import os
import sys
from shutil import rmtree
from typing import Tuple, List

from setuptools import Command, setup

# Package meta-data
name = "simple-linear-regression_python"
description = "Simple Linear Regression in Python"
url = "https://github.com/drnitinmalik/simple-linear-regression"
email = "nitinmalik77@gmail.com"
author = "Nitin Malik"
requires_python = ">=3.0.0"
current_dir = "os.path.abspath(os.path.dirname(__file__))"

def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        return f.read()

class UploadCommand(Command):
    description = "Build and publish the package"
    user_options: List[Tuple] = []

    @staticmethod
    def status(s):
        """Print things in bold."""
        print(s)

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(current_dir, "dist"))
        except OSError:
            pass

        self.status("Building distribution...")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        self.status("Pushing git tags...")
        os.system("git tag v{}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()
