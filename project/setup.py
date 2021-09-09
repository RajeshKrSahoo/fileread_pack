

from setuptools import setup, find_packages

setup(
    name="file reader",
    version="0.1",
    packages=find_packages(),
    # zip_safe=True,
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['pytest','jsonlib','PyYAML'],#requirements
    # extras_require={
    #     'PDF':  ["ReportLab>=1.2", "RXP"],
    #     'reST': ["docutils>=0.3"],
    # }
    # entry_points={
    #     'console_scripts': [
    #         'snek = snek:main',
    #     ],
    # }

    author="Rajesh Sahoo",
    author_email="rajesh2012acs@gmail.com",
    description="this package is to read those files",
    keywords="file reader",

   
)