from setuptools import setup, find_packages
import re


with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


with open("ytb_up/__init__.py") as f:
    version = re.search(
        r"""^__version__\s*=\s*['"]([^\'"]*)['"]""", f.read(), re.MULTILINE
    ).group(1)


setup(
    name="ytb-up",
    version=version,
    author="wanghaisheng",
    author_email="edwin.uestc@gmail.com",
    description="auto video machine,Upload videos to YouTube using geckodriver, Firefox profiles and Selenium/playwright.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/wanghaisheng/youtube-auto-upload",
    download_url="https://github.com/wanghaisheng/youtube-auto-upload/tarball/v" + version,
    packages=["ytb_up"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["playwright"],
    python_requires=">=3.6",
)
