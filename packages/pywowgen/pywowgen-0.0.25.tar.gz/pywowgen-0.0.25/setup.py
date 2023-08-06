from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pywowgen',
    version='0.0.25',
    packages=['pywowgen'],
    install_requires=[
        'Pillow',
        'requests',
        'flask',
        'GitPython'],
    url='https://git.cccwi.de/2dwt/wowgen',
    author='tigabeatz',
    author_email='tigabeatz@cccwi.de',
    description='Generate and configure Workadventure worlds, maps and resources',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    entry_points={
        'console_scripts': [
            'pywowgen=pywowgen.cli:main'
        ]
    },
)
