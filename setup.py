from setuptools import setup, find_namespace_packages


setup(
    name='projectX',
    version='1.0',
    packages=find_namespace_packages(),
    install_requires=[
        'customtkinter',  # Example dependency
    ],
    entry_points={
        'console_scripts': ['start-project = project.gui:main',],
    },
)
