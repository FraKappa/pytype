from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='pytyping',
    packages=['pytyping'],
    version='0.1',
    license='MIT',
    description='A simple Typing Speed Test right in your terminal made with Python and the curses module.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kappa',
    author_email='f.cappetti.05@gmail.com',
    url='https://github.com/FraKappa/pytype',
    download_url='https://github.com/FraKappa/pytyping/archive/refs/tags/v_01.tar.gz',
    keywords=['typing'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
  ]
)
