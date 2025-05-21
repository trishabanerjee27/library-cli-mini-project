from setuptools import setup, find_packages

setup(
    name="library-cli",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "library-cli=main:main"
        ]
    },
    install_requires=[],
    author="Your Name",
    description="CLI Library Management System",
)