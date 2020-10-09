import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AnagramSolver",
    version="0.1.4",
    author="James Butcher",
    author_email="jamesbutcher167@gmail.com",
    description="Solves Your Anagrams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ForbiddenKJ/AnagramSolver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
