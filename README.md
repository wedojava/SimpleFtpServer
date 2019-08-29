# SimpleFtpServer
Implement by Python3.7

A very simple and crude FTP server. where it is ,where the folder was shared by ftp!

By default, username is `user`, password is `123456`, port is `21`

You can change it while running.

## Preparation

You need to install the package below:

    pip install pyftpdlib

### Optional

If you wanna package it into one exe file, if your option system is win10, you maybe need this [Q&A from stackoverflow](https://stackoverflow.com/questions/47155474/create-an-exe-compatible-with-all-versions-of-windows-64-bit-and-32-bit-even-if) and [Universal CRT not found](https://github.com/pyinstaller/pyinstaller/issues/1566)
also, you can get it by download a portable zip and set it in your pyinstaller `.spec` file like this:

```
...
a = Analysis(['ftp_server.py'],
             pathex=['<your ucrt root path>\\ucrt\\DLLs\\x86'],
             binaries=[],
             ...
```


## Passed test platform

- Windows XP SP3
- Windows 7
- Windows 10

## Usage

Oh no descritions, just run it is ok.