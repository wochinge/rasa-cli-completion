from distutils.core import setup

setup(
    name="rasa-cli-completion",
    version="0.1",
    license="Apache 2.0",
    long_description=open("README.md").read(),
    install_requires=["rasa~=1.3"],
    tests_require=["pytest~=4.5"],
)
