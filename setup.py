import os

from setuptools import setup, find_packages

setup(
    name="RealESRGAN",
    py_modules=["RealESRGAN"],
    version="1.0",
    description="",
    author="Sberbank AI, Xintao Wang",
    url='https://github.com/ai-forever/Real-ESRGAN',
    packages=find_packages(include=['RealESRGAN']),
    install_requires=[
        line.strip()
        for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        if line.strip() and not line.startswith("#")
    ],
)
