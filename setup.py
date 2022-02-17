import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	# Here is the module name.
	name="jsonsh",

	version="0.1.1",

	author="Suryansh Sharma",

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
