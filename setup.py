from setuptools import setup

def parse_requirements(filename:str) -> list:
    """Reads the requirements.txt file and returns a list of packages."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

setup(
    name='excel_column_extractor',
    version='0.1',
    packages=['column_utils'],
    license='unlincense',
    description='Extracts data from a specific column in an Excel file and stores it in a list.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Fernando Fontes',
    author_email='nandofontes30@gmail.com',
    url='https://github.com/fernandoluiz2003/CreateDirectory',
    install_requires=parse_requirements('requirements.txt')
)