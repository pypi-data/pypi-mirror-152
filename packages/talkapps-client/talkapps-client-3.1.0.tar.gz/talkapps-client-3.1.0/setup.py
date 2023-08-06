import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="talkapps-client",
    version="3.1.0",
    author="NKDuy",
    author_email="kn145660@gmail.com",
    description="A client for the Talk stickers API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/talkapps/talkapps-client",
    packages=setuptools.find_packages(),
    install_requires=[
        'anyio>=2.0.2,<3.0.0',
        'httpx>=0.16.1,<0.17.0',
        'cryptography>=3.1.1,<4.0.0',
        'protobuf>=3.13.0,<4.0.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Chat"
    ],
    python_requires='>=3.6',
    package_data={
        'talkapps_client': ['utils/ca/cacert.pem']
    }
)
