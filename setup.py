from setuptools import setup, find_namespace_packages


setup(
    name='projectX',
    version='2.0',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': ['start = project.gui:main',],
    },
)
