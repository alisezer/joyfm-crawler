from setuptools import setup, find_packages

setup(
    name='joycrawler',
    version='0.1.0',

    description='Joy Crawler',

    # The project's main homepage.
    url='https://github.com/alisezer/joyfm_crawler',

    # Author details
    author='Ali Sezer',
    author_email='ali@sezeruk.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
    ],
    keywords='joy, radio, crawl',
    packages=find_packages(),

    install_requires=[
        'pandas',
        'beautifulsoup4',
        'lxml',
        'click',
        'requests'
    ],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'joycrawler = manage:manage',
        ],
    },
)