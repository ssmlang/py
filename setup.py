from setuptools import setup, find_packages

setup(
    name="simple_structured_markup",
    version="0.1.0",
    description="A lightweight parser for Simple Structured Markup (SSM) files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="sctech",
    author_email="gamerselimiko@gmail.com",
    url="https://github.com/ssmlang/py",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
