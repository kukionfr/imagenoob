import setuptools

with open("README.md", encoding="utf8") as fh:
    readme = fh.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name="imagenoob",
    version="0.0.1",
    author="Kyu Sang Han",
    author_email="khan21@jhu.edu",
    description="VAMPIRE Image Analysis Package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kukionfr/VAMPIRE_open",
    license=license,
    packages=setuptools.find_packages(include=['vampireanalysis', 'vampireanalysis.*']),
    install_requires=[
        'scipy==1.3.3',
        'pandas==0.25.3',
        'numpy==1.17.4',
        'pillow==6.2.1',
        'matplotlib==3.1.2',
        'scikit-learn==0.22',
        'scikit-image==0.16.2',
        'opencv-python==4.1.2.30',
        'dask==2.9.0'
    ],
    # scripts=['bin/vampire.py'],
    entry_points={
        'console_scripts': ['vampire=vampireanalysis.vampire:vampire']
        },
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        'Operating System :: Microsoft :: Windows',
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires='>=3'
)