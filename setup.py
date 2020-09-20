import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonToExcel", # Replace with your own username
    version="0.0.1",
    author="Akriti Anand",
    author_email="anand.akriti@gmail.com",
    description="Package to convert complex, nested json objects to excel.",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
