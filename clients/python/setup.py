import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pentools", 
    version="0.0.1",
    author="Artur Saradzhyan",
    author_email="sartur.ruk@gmail.com",
    description="CLI for Pen Tools API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarartur/pentools/tree/master/clients/python",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'pentools = pentools.__main__:main',                  
        ], 
        'pentools.registered_commands': [
            'list = pentools.commands.list:main',
            'script = pentools.commands.script:main'
        ]         
    },
    install_requires=['requests'],
    setup_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)