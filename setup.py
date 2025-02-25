from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="whatsapp-bot",
    version="0.1.0",
    author="M4A1SD",
    description="A WhatsApp bot with FastAPI integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M4A1SD/whatsapp-bot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "fastapi",
        "uvicorn",
        "pywa",
        "python-dotenv",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "whatsapp-bot=whatsappModule.main:app",
        ],
    },
) 