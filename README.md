
# Double Encryption for Image Steganography
![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/cover1.jpg)

Image Steganography can be used to communicate secretly by hiding data within images, audio files and other media. However, it is easy for a cybercriminal to decrypt these media files and extract the data which poses a severe threat to integrity.

To combat the above stated problem, we look at the double encryption of plaintext before embedding the data in a cover image. The message is encrypted using Rivest-Shamir-Adleman (RSA), Advanced Encryption Standard (AES) and lastly by Triple Data Encryption Standard (3DES).

The double encrypted data is compressed with LZMA technique to reduce the capacity of the data to be embedded in the steganographic image. To increase the robustness, the Sieve of Eratosthenes algorithm is used for insertion using the Least Significant Bit steganography.



## Table of Contents
- [About the Project](#about-the-project)
- [Library Used](#library-used)
- [Installation](#installation)
- [Results](#results)

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

Additionally, the LZMA library is used to compress and decompress the data.

The documentation to the LZMA library can be found [here](https://docs.python.org/3/library/lzma.html)

## Installation

_The following steps can be followed to setup the proposed system in your system:-_

1. Install python version greater than 3.6 from [python.org](https://www.python.org/).
2. Setup a virtual python environment. Go to your terminal and do the following to set it up.
```
pip install virtualenv
virtualenv [name of your new virtual environment]
cd [name of your new virtual environment]
source Scripts/activate
```
3. Clone the repository by running the following in the terminal.
```
git clone https://github.com/NotHari/Double-Encryption.git
```
4. To install the dependencies to run the code execute the following after activating your python virtual environment.
```
pip install -r requirements.txt
```
5. Run code to see the output on your terminal.

## Results

_The following screenshot shows the terminal output upon running the code:-_
![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/ss.png)


_The following figures show the results of three images after going through our proposed method of image steganography:-_
| S.no. | Cover Image | Steganographic Image |
|-------|-------------|----------------------|
| 1     | ![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/1.png)  | ![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/1.png)           |
| 2     | ![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/2.png)  | ![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/2.png)           |
| 3     | ![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/3.png)  | ![image](https://github.com/NotHari/Double-Encryption-for-Image-Steganography/blob/main/assets/3.png)           |

_The following figure shows the PSNR of the same three images:-_
| Cover Image   | Size of Image in KB | Secret Message in Bytes | Proposed Method PSNR |
|---------------|---------------------|-------------------------|----------------------|
| Cover Image 1 | 120                 | 25                      | 79.7239              |
| Cover Image 2 | 123                 | 25                      | 73.7692              |
| Cover Image 3 | 135                 | 25                      | 77.6347              |

