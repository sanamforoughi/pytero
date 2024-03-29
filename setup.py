import setuptools

requirements = [
    'requests>=2.22.0'
]
with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='pytero',
    version='0.1.0',
    scripts=[],
    author='Brave Hager',
    author_email='bravehager7@gmail.com',
    description='A requests wrapper for the Natero API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bravehager/pytero',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
    ],
)
