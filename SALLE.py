import pyfiglet
import os
import getpass

font = pyfiglet.Figlet(font='cosmic')
logo_text = "S A L L E"
figlet_logo = font.renderText(logo_text)

os.system("clear")
print(figlet_logo)


def anmeldung_pruefen():
    benutzername = input("Benutzername: ")
    passwort = getpass.getpass("Passwort: ")

    with open("anmeldedaten.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(":")
            if benutzername == stored_user and passwort == stored_pass:
                print("Anmeldung erfolgreich!")
                return True

    print("Ungültige Anmeldeinformationen.")
    return False

if anmeldung_pruefen() == True:

	os.system("clear")
	print(figlet_logo)


	print("1 Beef 			2 Port Scanner")
	print("3 Exploit-Frameworks	4 Password Cracker")
	print("5 Packet Sniffer  	6 Social Engeneering Tools")
	print("7 Forensik-Tools  	8 Keylogger")


userinput = input()

if userinput == "1":
	os.system("sudo beef-xss")
if userinput == "2":
	os.system("sudo zenmap-kbx")
if userinput == "3":
	os.system("sudo msfconsole")
if userinput == "4":
	print("in arbeit")
if userinput == "5":
	os.system("sudo wireshark")
if userinput == "6":
	print("in arbeit")
if userinput == "7":
	os.system("sudo autopsy")
if userinput == "8":
	print("in arbeit")
if userinput > "8" or userinput < "0":
	print("Ungültige Eingabe")
