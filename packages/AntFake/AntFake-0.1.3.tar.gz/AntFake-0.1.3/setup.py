from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r") as req_file:
    req = req_file.read()

setup(
    name='AntFake',
    version='0.1.3',
    license='MIT',
    author="Inkviz96",
    author_email='b-semen-b@mail.ru',
    packages=find_packages(),
    url='https://github.com/inkviz96/antFake',
    keywords='fake test web3 eth',
    description="Ant is library for generation random string, float, eth address and pk, etc",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=req,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)