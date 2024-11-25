from setuptools import find_packages,setup


setup(

    name='mymcq',
    version='0.0.1',
    author='goutam',
    author_email="goutamkumar.sharmq@gmail.com",
    install_requires=["openai",
"langchain",
"streamlit",
"python-dotenv",
"PyPDF2"],
packages=find_packages()
)