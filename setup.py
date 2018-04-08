from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Flask Mail Bundle',
    version='0.2.0',
    description='Adds email sending support to Flask Unchained',
    long_description=long_description,
    url='https://github.com/briancappello/flask-mail-bundle',
    author='Brian Cappello',
    license='MIT',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    py_modules=['flask_mail'],
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'blinker>=1.4',
        'beautifulsoup4>=4.6.0',
        'flask-unchained>=0.2.0',
        'lxml>=4.2.1',
    ],
    extras_require={
        'test': ['mock', 'pytest', 'pytest-flask', 'speaklater'],
    },
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'pytest11': [
            'flask_mail_bundle = flask_mail_bundle.pytest',
        ],
    },
)
