from setuptools import setup,find_packages
setup(name='dfcbenchmarker',
      version='1.0',
      description='dfcbenchmarker is a package that compares different dynamic functoinal connectivity methods against eachother.',
      packages = ['dfcbenchmarker'],
      package_data={'':['./dfcbenchmarker/data/']},
      include_package_data = True,
      author='William Hedley Thompson',
      url='https://www.github.com/wiheto/dfcbenchmarker',
      )
