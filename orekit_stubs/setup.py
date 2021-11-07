from setuptools import setup

ALL_PYI = [('*/' * depth) + '*.pyi' for depth in range(0, 15)]

setup(
    name='orekit_stubs',
    version='0.1',
    packages= [ 'org-stubs'],
    package_dir = { 'org-stubs':'org-stubs'},
    package_data={ 'org-stubs':ALL_PYI},
    include_package_data=True,
    license='apache',
    author='Petrus Hyvonen',
    author_email='petrus.hyvonen@gmail.com',
    description='None',
    zip_safe = False
)
