
from setuptools import setup, find_packages
setup(
    name="isbn_service",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'isbn_server= isbn.__main__:main'
        ]
    },
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['requests', 'falcon'],

    # metadata for upload to PyPI
    author="Carlos",
    author_email="carlosvin@gmail.com",
    description="ISBN service",
    license="PSF",
    keywords="isbn server",
    url="https://github.com/carlosvin/isbn_service",
    # could also include long_description, download_url, classifiers, etc.
)