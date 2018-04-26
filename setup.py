import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

from docma import __version__


class PyTestCommand(TestCommand):
    """ Command to run unit py.test unit tests
    """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest
        rcode = pytest.main(self.test_args)
        sys.exit(rcode)


setup(
    name='docma',
    version=__version__,
    author='Neil Joshi',
    author_email='',
    description='Describe schemas in docstrings',
    license='MIT',
    keywords='python schema docstring',
    url='http://github.com/pydocma/docma',
    py_modules=['docma'],
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Schema',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=[
            'pytest',
        ],
    cmdclass={
            'test': PyTestCommand,
        }
)