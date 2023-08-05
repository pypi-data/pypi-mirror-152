from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


setup(
    name="pyrootutils",
    version="1.0.1",
    license="MIT",
    description="Simple package for setting up the root of the project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashleve/pyrootutils",
    author="ashleve",
    author_email="ashlevegalaxy@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7.0",
    include_package_data=True,
    install_requires=["python-dotenv"],
    tests_require=["pytest"],
)
