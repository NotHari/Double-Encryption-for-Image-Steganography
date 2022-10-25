
# Implementation of Cryptographic Algorithms for Steganography

Image Steganography can be used to communicate secretly by hiding data within images, audio files and other media. However, it is easy for a cybercriminal to decrypt these media files and extract the data which poses a severe threat to integrity.

To combat the above stated problem, techniques that combine the advantages of cryptography with those of steganography are needed. 



## Table of Contents
- [About the Project](#about-the-project)
- [Library Used](#library-used)
- [Installation](#installation)

## About the Project

Image Steganography is the process of embedding hidden data to a media file like image, audio or video files. The secret information is hidden in a way that it isn't visible to the human eyes.

However, a more secure system can be implemented that uses cryptographic algorithms along with steganographic techniques.

Our project involves the use of several independent layers of encryption, enabled to protect against the compromises of any one layer of encryption in a process known as **Double Encryption**.

Our system makes use of three independent layers of encryption which are as follows:-
- **Layer 1**: RSA with 1024-bit private key.
- **Layer 2**: AES with 128-bit private key.
- **Layer 3**: Triple DES with 168-bit private key.


## Library Used

Our project makes use of the pycryptodome library which is a python library that consists of cryptographic primitives.

The documentation to the library can be found [here](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html).

## Installation

_The following steps can be followed to setup the proposed system in your system:-_

1. Install python version greater than 3.6 from [python.org](https://www.python.org/).
2. Setup a virtual python environment. Go to your terminal and do the following to set it up.
```
pip install virtualenv
virtualenv [name of your new virtual environment]
cd [name of your new virtual environment]
source Scripts/activate
cd [name of parent directory]
```
3. Clone the repository by running the following in the terminal.
```
git clone https://github.com/NotHari/Double-Encryption.git
```
4. To install the dependencies to run the code execute the following after activating your python virtual environment.
```
pip install pycryptodome
```
5. Run code to see the output on your terminal.


Made with ❤ by [Harikrishnan Nair](https://github.com/NotHari) &  [Tanvi Johari](https://github.com/TJ202)
