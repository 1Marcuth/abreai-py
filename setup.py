from setuptools import setup

with open("README.md", "r") as file:
    readme_content = file.read()

setup(
    name="abreai",
    version="1.0.1",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="abreai wrapper api",
    description=f"A Wrapper to communicate with the https://abre.ai API",
    packages=["abreai", "abreai/models"],
    install_requires=["httpx", "pydantic", "rich"],
)