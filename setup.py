from setuptools import setup, find_packages

setup(
    name="mongo-helper-kit",
    version="0.1.0",
    author="Abhishek Prakash",
    author_email="abhishekprakash47@gmail.com",
    description="A simple MongoDB helper kit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abhishekprakash256/mongo-helper-kit",
    packages=find_packages(),
    install_requires=[
        "pymongo>=3.6,<4.0",
        "mongomock>=3.19",  # If you're using it for testing
        "pytest>=8.3.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
