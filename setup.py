from setuptools import setup, find_packages

setup(
    name='genotools', 
    version='1.0.0', 
    packages=find_packages(),
    author='Dan Vitale',
    author_email='d.vitale199@gmail.com',
    description='A collection of tools for genotype quality control and analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dvitale199/GenoTools',
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    extras_require={
        'dev': [
            'pytest>=3.7',
            'twine>=1.11.0'
        ]
    },
    entry_points={
        'console_scripts': [
            'genotools=genotools.__main__:handle_main',
            'genotools-download=genotools.download_refs:handle_download',
        ]
    },
    install_requires = [
        'dash_bio==1.0.2',
        'joblib==1.3.0',
        'matplotlib==3.6.2',
        'numba==0.57.1',
        'numpy==1.23.5',
        'pandas==2.0.3',
        'Pillow==9.3.0',
        'plotly==5.11.0',
        'requests==2.28.1',
        'scikit_learn==1.3.0',
        'scipy==1.9.3',
        'seaborn==0.12.1',
        'setuptools==65.6.3',
        'statsmodels==0.13.5',
        'streamlit==1.15.2',
        'umap_learn==0.5.3',
        'xgboost==1.7.6',
        'google-cloud-aiplatform',
        'google-cloud-storage'
    ],
    package_data={
      'genotools': ['container/*.pkl','container/*.txt','container/Dockerfile']
   }
)