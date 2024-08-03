# Third Party Library
from setuptools import find_packages, setup

setup(
    name="pdf_generator",
    version="0.1.0",
    description="PDF generator app",
    author="Praful Patekar",
    author_email="prafulpatekar23@gmail.com",
    keywords="pdf_generator",
    license="MIT",
    url="https://github.com/Prafulpatekar/pdf_generator",
    python_requires="~=3.9",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    install_requires=[
        "supervisor==4.1.0",
        "fastapi==0.68.0",
        "fastapi-auth0==0.2.1",
        "PyJWT==1.7.1",
        "Pillow==9.0.0",
        "python-jose==3.3.0",
        "python-json-logger==2.0.2",
        "uvicorn==0.11.3",
        "python-multipart==0.0.5",
        "aiofiles",
        "pydantic[email]"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
