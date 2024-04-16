from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Use this to interact with Google Chat easily.'
LONG_DESCRIPTION = 'This wrapper module allows you to easily interact with Google Chat, allowing you to build Google Chat applications that run in Python, so you don't need to learn Javascript or Apps Script.'

# Setting up
setup(
    name="Webhook Interface", 
    version=VERSION,
    author="SquchyBear",
    author_email="<squchybot@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["httplib2", "google-api-python-client", "google-auth"],
    
    keywords=['python', 'first package', 'google', 'wrapper'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
