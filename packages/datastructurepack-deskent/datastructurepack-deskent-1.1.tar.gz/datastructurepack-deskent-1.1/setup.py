import setuptools

setuptools.setup(
    name="datastructurepack-deskent",
    version="1.1",
    author="Deskent",
    description="Datastorage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
