
import re
from setuptools import Extension, setup

extensions = [
    Extension("oscar", sources=["oscar.pyx"], libraries=["tokyocabinet"]),
]

head = open('oscar.pyx').read(2048)
pattern = r"""__%s__\s*=\s*['"]([^'"]*)['"]"""
kwargs = {keyword: re.search(pattern % keyword, head).group(1)
          for keyword in ('version', 'author', 'license')}

requirements = [
    line.strip()
    for line in open('requirements.txt')
    if line.strip() and not line.strip().startswith('#')]

# options reference: https://docs.python.org/2/distutils/
# see also: https://packaging.python.org/tutorials/distributing-packages/
setup(
    name="oscar",
    description="A Python interface to OSCAR data",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[  # full list: https://pypi.org/classifiers/
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Cython',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering'
    ],
    # since setuptools  18.0 it is possible to pass Cython sources to extensions
    # without `cythonize`
    # https://stackoverflow.com/questions/37471313
    setup_requires=['setuptools>=18.0', 'cython'],
    python_requires='>=3.4',
    ext_modules=extensions,
    author_email=kwargs['author'],
    url='https://github.com/ssc-oscar/oscar.py',
    install_requires=requirements,
    test_suite='test.TestStatus',
    **kwargs
)
