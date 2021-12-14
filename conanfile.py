import os
from conans import ConanFile, tools

class LinuxAarch32Toolchain(ConanFile):
    name = "linux_aarch32_toolchain"
    version = "10.2"
    settings = "os", "arch"

    def build(self):
         tools.get("https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-a/10.2-2020.11/binrel/gcc-arm-10.2-2020.11-x86_64-arm-none-linux-gnueabihf.tar.xz", destination="toolchain")

    def package(self):
        self.copy("*", dst="", src="toolchain/gcc-arm-10.2-2020.11-x86_64-arm-none-linux-gnueabihf")

    def package_info(self):
        bin_folder = os.path.join(self.package_folder, "bin")
        self.env_info.CC = os.path.join(bin_folder, "arm-none-linux-gnueabihf-gcc")
        self.env_info.CXX = os.path.join(bin_folder, "arm-none-linux-gnueabihf-g++")
        self.env_info.SYSROOT = self.package_folder