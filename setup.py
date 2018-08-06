from codecs import open as codecs_open
from setuptools import setup, find_packages


# Parse the version from the fiona module.
with open('aligncheck/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip().strip('"\'')
            break

# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='rio-aligncheck',
      version=version,
      description=u"Rasterio CLI plugin for checking raster alignment",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Neil Freeman",
      author_email='contact@fakeisthenewreal.org',
      url='https://github.com/fitnr/rio-aligncheck',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'rasterio'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [rasterio.rio_commands]
      aligncheck=aligncheck.scripts.cli:aligncheck
      """)
