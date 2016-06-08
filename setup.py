from setuptools import find_packages, setup


setup(
    name='kagiso_image',
    version='1.1.0',
    author='Kagiso Media',
    author_email='development@kagiso.io',
    description='Kagiso Image with Attribution',
    url='https://github.com/Kagiso-Future-Media/kagiso_image',
    packages=find_packages(),
    install_requires=[
        'wagtail>=1.4.3',
        'fake-factory>=0.5.7',
    ]
)
