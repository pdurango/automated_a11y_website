from setuptools import setup, find_packages

setup(name='automated_a11y',
      version='2.0',
      description='Crawls websites and accessibility checks each page',
      url='https://github.com/pdurango/AutomatedA11y',
      author='Lucas Silvestri',
      author_email='SilveslaCreates@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      install_requires=['Naked']
      )
