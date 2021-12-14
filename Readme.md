# Linux AArch32 GNU toolchain conan package

This conan toolchain package is intended to cross-compile other conan packages for Linux based AArch32 systems of the Cortex-A Family. Sample conan profiles to cross-compile from Linux based x86 build system to Linux based AArch32 systems are provided.

## Use Case

This package can be used to build for

 - Raspberry Pi greater 2 B
 - Raspberry Pi Zero 2 W

If you want to check compatibility of your Raspberry Pi use command

```
$ uname -m
```
to get the soc archtiecture. 
If output is equal to `armv7l` you can use this package. If it is `armv8` you should consider to use an AArch64 Toolchain since the plattform should support 64 Bit software aswell (might be added to this repo in the future). 

## Supported OS

Currently, only GNU Toolchain 10.2 was packaged. If you want to know if your Linux based host system is compatible with this version checkout if your GLIB matches version 2.31:

```
$ ldd --version
```

Running this command on Raspberry Pi 3 B with latest Raspberry Pi OS (Debian Bullseye) produces following output:

```
ldd (Debian GLIBC 2.31-13+rpt2+rpi1+deb11u2) 2.31
```

which is compatible with GNU Toolchain 10.2. 


## Usage

### Create the package

Clone the repository and run 

```
$ conan create . 
```

in the repository root to create the toolchain package.

### Use the package

Running a Linux based x86_64 build system you can add the sample-profiles to conan profiles directory and try to cross compile OpenCV using conan center package

```
$ conan install opencv/4.5.3@ -pr:b=linux-x86-debug -pr:h=linux-aarch32-debug --build=missing
```

## Versioning

The version of the package is equivalent to the used [GNU toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-a/downloads). 

## Contribution

Feel free to update other GNU toolchain versions by creating pull requests to main branch. They will be taged with the corresponding versions afterwards.