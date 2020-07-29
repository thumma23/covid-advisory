import setuptools

REQUIREMENTS = [
    "flask",
    "flask_jwt",
    "Cython",
    "flask_restful",
    "requests",
    "datetime",
    "numpy",
    "mysql-connector" 
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covid-advisory", # Replace with your own username
    version="0.0.4",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires = REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)