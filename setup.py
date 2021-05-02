from setuptools import find_packages, setup

setup(name="microservices",
      version = "0.1",
      author = "MSD",
      description = "Movie House",
      platforms = ["any"],
      packages = find_packages(),
      install_requires = ["Flask==0.10.1", "requests==2.20.0", "wsgiref==0.1.2" ],
      )
