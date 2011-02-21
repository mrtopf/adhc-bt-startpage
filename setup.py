from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='startpage',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "logbook",
        "werkzeug",
        "routes",
        "quantumcore.storages",
        "quantumcore.exceptions",
        "jinja2",
            
      ],
      entry_points="""
        [paste.app_factory]
        frontend = startpage.main:frontend_factory
      """,
      )
