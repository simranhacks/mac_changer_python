import subprocess

interface = input("Enter the name of the interface: ")
new_mac = input("Enter the new MAC address: ")


subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.run(["ifconfig", interface, "up"])
subprocess.run("ifconfig")

print("Your MAC is spoofed")
