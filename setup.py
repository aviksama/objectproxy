import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


setup(name='object-proxy',
      version='0.1a',
      description='A minimalistic yet powerful object proxying utility',
      long_description=README + '\n',
      classifiers=[
          "Programming Language :: Python",
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      author='Avik Samaddar',
      author_email='eml2avik@gmail.com',
      url='https://github.com/aviksama/objectproxy',
      keywords='python objectproxy',
      packages=['objectproxy'],
      include_package_data=True,
      zip_safe=True,
      )
