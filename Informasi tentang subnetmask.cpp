#include <iostream>
#include <sstream>
#include <bitset>
#include <vector>

// Fungsi untuk mengonversi subnet mask ke notasi biner
std::string subnetToBinary(const std::string& subnet) {
    std::istringstream iss(subnet);
    std::string octet;
    std::bitset<8> binary;

    std::string result;
    while (std::getline(iss, octet, '.')) {
        binary = std::bitset<8>(std::stoi(octet));
        result += binary.to_string();
    }

    return result;
}

// Fungsi untuk menghitung informasi CIDR, total IP address, dan total IP address yang bisa dipakai
void calculateCIDRInfo(const std::string& subnet) {
    // Mengonversi subnet mask ke notasi biner
    std::string binarySubnet = subnetToBinary(subnet);

    // Menghitung jumlah bit yang diatur ke 1 dalam notasi biner subnet mask
    size_t cidr = binarySubnet.find('0');

    // Menghitung total IP address
    unsigned long long totalIPs = static_cast<unsigned long long>(1) << (32 - cidr);

    // Menghitung total IP address yang bisa dipakai
    unsigned long long usableIPs = totalIPs - 2;

    // Menampilkan hasil
    std::cout << "CIDR: /" << cidr << std::endl;
    std::cout << "Total IP Address: " << totalIPs << std::endl;
    std::cout << "Total Usable IP Address: " << usableIPs << std::endl;
}

int main() {
    std::string subnet;
    
    // Meminta pengguna untuk memasukkan subnet mask
    std::cout << "Masukkan subnet mask (contoh: 255.255.255.0): ";
    std::cin >> subnet;

    // Menghitung informasi CIDR, total IP address, dan total IP address yang bisa dipakai
    calculateCIDRInfo(subnet);

    return 0;
}