from setuptools import setup, find_packages

entry_points = """\
[console_scripts]
hw1=binf690.hw1:main
"""

setup(
    name='binf690',
    version='0',
    author='Alexander Smith',
    author_email='asmitl@gmu.edu',
    url='https://github.com/ajsmith',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points=entry_points,
    install_requires=[
        'matplotlib',
        'numpy',
    ],
)
