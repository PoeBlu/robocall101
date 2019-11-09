from setuptools import setup


setup(
    name="robocall101",
    version="1.1",
    packages=["robocall101"],
    url="https://github.com/rootVIII/robocall101",
    license="MIT",
    author="rootVIII",
    description="Robocall on the fly with Python and Twilio ",
    entry_points={
        "console_scripts": [
            "robocall101=robocall101.robocall101:main"
        ]
    },
)
