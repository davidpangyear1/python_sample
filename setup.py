from setuptools import setup

setup(name='python_sample',
      version='1.0',
      description='A sample standalone python program with some good practices.',
      url='https://github.com/davidpangyear1/python_sample',
      # author='',
      # author_email='',
      # license='MIT',
      packages=['python_sample'],
      data_files=[ ('', ['__main__.py', ]),],
      zip_safe=False)
