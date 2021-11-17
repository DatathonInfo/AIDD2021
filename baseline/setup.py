#nsml: pytorch/pytorch:1.5-cuda10.1-cudnn7-runtime

from distutils.core import setup

setup(
    name='nia dm hackathon example',
    version='1.0',
    install_requires=[
        'pandas',
        'joblib',
        'sklearn',
        'lightgbm'
    ]
)