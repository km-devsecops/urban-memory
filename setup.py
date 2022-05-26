import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="app",
    version="1.0.0",
    url="https://github.com/km-devsecops/urban-memory.git",
    license="BSD",
    maintainer="Cloud SRE",
    maintainer_email="cloud.sre@demo.com",
    description="Python application.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)