from setuptools import setup, find_namespace_packages


setup(
    name='goit_project',
    version='1.0',
    packages=find_namespace_packages(),
    install_requires=[
        'prompt_toolkit','rich',
    ],
    entry_points={
        'console_scripts': ['startproject = goit_project.main:main',],
    },
)
