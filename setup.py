# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


install_requires = [
    'urwid',
]

setup(name='astlog',
      version='0.5',
      description='astlog',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Tvrtko Sokolovski',
      author_email='tvrtko.sokolovski@gmail.com',
      url='https://github.com/slsolucije/astlog',
      keywords='asterisk sip log',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      cmdclass={},
      install_requires=install_requires,
      entry_points="""\
        [console_scripts]
        astlog=astlog.app:main
      """)
