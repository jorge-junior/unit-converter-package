from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="minimal_unit_converter",
    version="0.0.2",
    author="Jorge Junior",
    author_email="juniorjorge0375@gmail.com",
    description="Meu primeiro pacote em python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorge-junior/unit-converter-package",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.8',
    keywords=['python', 'first package']
)