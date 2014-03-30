from setuptools import setup, find_packages

setup(name='opennlp',
      version='0.1',
      description='Python wrapper for Apache OpenNLP tools',
      keywords='opennlp nlp',
      author='Aron Curzon',
      author_email='curzona@gmail.com',
      url='http://pypi.python.org/pypi/opennlp-python',
      packages=['opennlp'],
      zip_safe=True,
      install_requires=[
          'setuptools',
          'pexpect',
      ],
      tests_require=[
          'nose',
      ],
)
