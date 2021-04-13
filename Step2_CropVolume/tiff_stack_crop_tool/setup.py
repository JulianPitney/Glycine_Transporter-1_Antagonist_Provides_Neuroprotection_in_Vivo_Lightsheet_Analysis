#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'opencv-python==3.2.0.6',
    'tiffile',
    'imagecodecs',
    'numpy==1.19.2',
    'pywin32',
]


setup(
    author="Julian Pitney",
    author_email='julianpitney@Gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Utility for cropping tiff stacks in 3D.",
    entry_points={
        'console_scripts': [
            'tiff_stack_crop_tool=tiff_stack_crop_tool.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tiff_stack_crop_tool',
    name='tiff_stack_crop_tool',
    packages=find_packages(include=['tiff_stack_crop_tool', 'tiff_stack_crop_tool.*']),
    url='https://github.com/JulianPitney/tiff_stack_crop_tool',
    version='0.6',
    zip_safe=False,
)
