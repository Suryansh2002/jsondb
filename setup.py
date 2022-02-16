import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	# Here is the module name.
	name="jsonsh",

	# version of the module
	version="0.0.1",

	# Name of Author
	author="Suryansh Sharma",

	# your Email address
	author_email="suryanshwins2002@gmail.com",

	long_description=long_description,
	long_description_content_type="text/markdown",

	url="https://github.com/Suryansh2002/jsonsh",
	packages=setuptools.find_packages(),


	install_requires=[
        "orjson",
        "ujson",
        "pydantic"
    ],


	license="MIT",

	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
