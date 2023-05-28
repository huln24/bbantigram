from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bbantigram',
    version='0.0.0',
    description='Rule out Red Blood Cell Antibody from Antibody Panels/Antigrams for Blood Bank laboratory',
    long_description=readme,
    author='Khulan Ulziibat',
    author_email='khulan.ulz@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

