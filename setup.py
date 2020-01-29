import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_custom_email_user",
    version="0.1",
    author="Gary Burgmann",
    author_email="garyburgmann@gmail.com",
    description="Modify Django default User to use email as unique identifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garyburgmann/django-custom-email-user",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
