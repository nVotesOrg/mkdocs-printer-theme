from setuptools import setup, find_packages

VERSION = '0.1.0'


setup(
    name="mkdocs-printer-theme",
    version=VERSION,
    url='http://www.nvotes.com',
    license='AGPL',
    description='Printer theme for MkDocs',
    author='nVotes',
    author_email='edulix@nvotes.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'printer = mkdocs_printer_theme',
        ]
    },
    zip_safe=False
)
