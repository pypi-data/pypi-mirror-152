import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ton",
    version="0.16",
    author="psylopunk",
    author_email="psylopunk@protonmail.com",
    description="Python client for The Open Network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/psylopunk/ton",
    packages=setuptools.find_packages(),
    install_requires=[
        'crc16==0.1.1',
        'poetry==1.1.13',
        'ujson==5.2.0',
        'ed25519==1.5',
        'requests==2.27.1'
    ],
    package_data={
        'ton': [
            'distlib/linux/*',
        ]
    },
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
