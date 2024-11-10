from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(), 
    include_package_data=True,
    license="Apache License 2.0",
    description="A simple math quiz package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vindu",
    url="https://github.com/Vindu1022/dsss_homework_2",
    install_requires=[],  # Add package dependencies here if any
    entry_points={
        "console_scripts": [
            "math_quiz = math_quiz.math_quiz:main",  
        ],
    },
)