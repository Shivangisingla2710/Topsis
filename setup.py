from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Topsis-Shivangi-101903122",
    version="1.0.0",
    description="A Python package for topsis analysis.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/manaskhatri/Topsis",
    author="Shivangi Singla",
    author_email="ssingla_be19@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["TOPSIS-Shivangi-101903122"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "TOPSIS_101703317=TOPSIS_101703317.Topsis:main",
        ]
    },
)