from setuptools import setup, find_packages

setup(
    name="terraform_validate",
    version="3.0.1",
    author="Edmund Dipple",
    author_email="elmundio1987@gmail.com",
    description="A library that provides asserts for testing Terraform configuration",
    url="https://github.com/foursquare/terraform_validate",
    download_url = 'https://github.com/foursquare/terraform_validate/tarball/3.0.1',
    keywords = ['terraform', 'assert', 'testing'],
    packages = find_packages(),
    install_requires=[
        "pyhcl"
    ],
)
