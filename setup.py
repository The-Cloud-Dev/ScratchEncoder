import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ScratchEncoder", 
    url="https://github.com/The-Cloud-Dev/ScratchEncoder",                    
    version="0.0.2",                        
    author="TheCloudDev",
    license="MIT",        
    description="Scratch Encoder",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',                 
)
