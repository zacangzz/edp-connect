from setuptools import setup, find_packages

setup(
    name="edp_connect",  # The name of your package
    version="1.0",
    packages=find_packages(),  # Automatically discovers all packages/modules
    install_requires=[
        "pyodbc",
        "python-dotenv",
        "sqlalchemy"
    ],
)
