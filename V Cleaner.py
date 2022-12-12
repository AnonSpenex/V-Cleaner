#Developed by AnonSpenex
#E-mail address : anon.spenexploit@protonmail.com

from tkinter import *
from tkinter import messagebox
import os
import pyttsx3
import webbrowser
import wget
import time
import winsound

os.system("title V Cleaner")

logo="""
 ██╗   ██╗   █████╗ ██╗     ███████╗ █████╗ ███╗  ██╗███████╗██████╗
 ██║   ██║  ██╔══██╗██║     ██╔════╝██╔══██╗████╗ ██║██╔════╝██╔══██╗
 ╚██╗ ██╔╝  ██║  ╚═╝██║     █████╗  ███████║██╔██╗██║█████╗  ██████╔╝
  ╚████╔╝   ██║  ██╗██║     ██╔══╝  ██╔══██║██║╚████║██╔══╝  ██╔══██╗
   ╚██╔╝    ╚█████╔╝███████╗███████╗██║  ██║██║ ╚███║███████╗██║  ██║
    ╚═╝      ╚════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝\n"""

menu = """
0: Find information about the hash function of a file.
1: Find information about an IP address.
2: Find information about a port.
3: Find information about a process.
4: Find information about a DLL.
5: Display all running processes in execution.
6: Display all information about network connections.
7: Determine all Windows related corruptions.
8: Perform an advanced analysis related to Windows problems.
9: Perform automatic analysis and repair of Windows related errors.
10: Activate the firewall
""" 

contact = """
CONTACT: anon.spenexploit@protonmail.com
"""  

antivirus = """
--------------ANTIVIRUS--------------

AVAST: Perform a analysis with Avast
"""                               

fonctions = """
1: SHA-256
2: MD5
"""

ip_options = """
1: Find information about an IP address.
2: WHOIS.
"""

def options():

    try:

        print(contact.strip())
        print(menu)
        print(antivirus.strip()+"\n")

        engine.say("What is your option ?")
        engine.runAndWait()
           
        option = input("What is your option ? :")

        while option not in ["0","1","2","3","4","5","6","7","8","9","10"]:

            frequency = 870
            duration = 1500
            winsound.Beep(frequency, duration)

            engine.say("This option is invalid.")
            engine.runAndWait()

            messagebox.showwarning("V Cleaner :", """
            This option is invalid.
            Please choose an option from the program.""")

            os.system("cls")

            print(logo)
            options() 

        engine.say("Do you want to perform an analysis with an antivirus ?")
        engine.runAndWait()

        antivirus_option = input("\nDo you want to perform an analysis with an antivirus ? :")

        if antivirus_option == "y":

            engine.say("Do you want to download the Avast Premium Security license file, valid until July 5, 2026 ?")
            engine.runAndWait()

            avast = input("Do you want to download the Avast Premium Security license file, valid until July 5, 2026 ? :")

            os.system("cls")

            if avast == "y":

                engine.say("Please wait, the license file is being downloaded.")
                engine.runAndWait()

                print("Please wait, the license file is being downloaded.\n")

                avast = "https://www.mediafire.com/file/rnhd6nt7xn8ooqv/Avast_Premium_Security_05-07-2026.avastlic/file"
                wget.download(avast)

                time.sleep(5)

                os.system("cls")

            elif avast == "n":

                pass

            engine.say("What is the drive, folder or file to be analyzed ?")
            engine.runAndWait()

            avast_analyse = input("What is the drive, folder or file to be analyzed ? :")

            os.system("cls")

            while avast_analyse not in ["A:","B:","C:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"]:

                frequency = 870
                duration = 1500
                winsound.Beep(frequency, duration)

                engine.say("""
                This option is invalid.
                Please transmit the letter of your drive, as well as the access path if it concerns a folder or file.""")
                engine.runAndWait()

                messagebox.showwarning("V Cleaner :", "Please transmit the letter of your drive, as well as the access path if it concerns a folder or file.")

                engine.say("What is the drive, folder or file to be analyzed ?")
                engine.runAndWait()

                avast_analyse = input("What is the drive, folder or file to be analyzed ? :")

                os.system("cls")

            engine.say("Please wait, the analysis is in progress.")
            engine.runAndWait()

            print("Please wait, the analysis is in progress...")

            time.sleep(5)

            os.system("cls")

            time.sleep(5)

            os.chdir(r"C:\Program Files\Avast Software\Avast")

            os.system("start ashCmd.exe" + " " +str(avast_analyse))

            os.system("pause > nul")

        elif antivirus_option == "n":

            os.system("cls")
            
            pass

        if option == "0":

            engine.say("You have selected the first option.")
            engine.runAndWait()

            hash()

        elif option == "1":

                engine.say("You have selected the second option.")
                engine.runAndWait()

                ip()

        elif option == "2":

                engine.say("You have selected the third option.")
                engine.runAndWait()

                port()

        elif option == "3":

                engine.say("You have selected the fourth option.")
                engine.runAndWait()

                process()

        elif option == "4":

                engine.say("You have selected the fifth option.")
                engine.runAndWait()

                DLL()

        elif option == "5":

                engine.say("You have selected the sixth option.")
                engine.runAndWait()

                process_2()
                
        elif option == "6":

                engine.say("You have selected the seventh option.")
                engine.runAndWait()

                network()

        elif option == "7":

                engine.say("You have selected the eighth option.")
                engine.runAndWait()

                corruptions()

        elif option == "8":

                engine.say("You have selected the ninth option.")
                engine.runAndWait()

                analyse()

        elif option == "9":

                engine.say("You have selected the tenth option.")
                engine.runAndWait()

                repair()

        elif option == "10":

                engine.say("You have selected the eleventh option.")
                engine.runAndWait()

                firewall()

    except (ValueError, TypeError):

        frequency = 870
        duration = 1500
        winsound.Beep(frequency, duration)

        engine.say("This option is invalid.")
        engine.runAndWait()

        messagebox.showwarning("V Cleaner :", "This option is invalid.")

        os.system("cls")

        print(logo)
        options()

        while antivirus_option.lower() not in ["y", "n"]:

            frequency = 870
            duration = 1500
            winsound.Beep(frequency, duration)

            engine.say("""
            This option is invalid.
            Please choose between the letter: y for yes or: n for no""")
            engine.runAndWait()

            messagebox.showwarning("V Cleaner :", """
            This option is invalid.\n
            Please choose between the letter: y for yes or: n for no""")

            os.system("cls")

            print(logo)
            options()

def hash():

    engine.say("What is the hash function ?")
    engine.runAndWait()

    print(fonctions.strip())

    engine.say("S-H-A-256 hash function.")
    engine.runAndWait()
    
    engine.say("MD5 hash function.")
    engine.runAndWait()

    engine.say("Wich hash function ?")
    engine.runAndWait()

    option = input("\nWhich hash function ? :")

    os.system("cls")

    while option not in ["1","2"]:

        frequency = 870
        duration = 1500
        winsound.Beep(frequency, duration)

        engine.say("Please choose the first or secondary option.")
        engine.runAndWait()

        messagebox.showwarning("V Cleaner :", "Please choose the first or secondary option.")

        print(fonctions.strip())

        option = input("\nWhich hash function ? :")

        os.system("cls")

    if option == "1":

        engine.say("You have selected the S-H-A-256 hash function")
        engine.runAndWait()
            
        time.sleep(3)

        engine.say("Please transmit the hash function.")
        engine.runAndWait()

        hash_file = input("Please transmit the hash function :")

        os.system("cls")

        engine.say("Please wait, the search for information about the SHA-256 hash function is in progress.")
        engine.runAndWait()

        print("Please wait, the search for information about the SHA-256 hash function is in progress...")

        time.sleep(5)

        os.system("cls")

        virustotal = "https://www.virustotal.com/gui/file/"+str(hash_file)
        webbrowser.open(virustotal)

        os.system("cls")

        print(logo)
        options()

    elif option == "2":

        engine.say("You have selected the MD5 hash function")
        engine.runAndWait()

        hash_file = input("Please transmit the hash function :")

        os.system("cls")

        engine.say("Please wait, the search for information about the MD5 hash function is in progress.")
        engine.runAndWait()

        print("Please wait, the search for information about the MD5 hash function is in progress...")

        time.sleep(5)

        virustotal = "https://www.virustotal.com/gui/file/"+str(hash_file)
        webbrowser.open(virustotal)

        os.system("cls")
                
        print(logo)
        options()

def ip():

    engine.say("Find information about an IP address.")
    engine.runAndWait()

    engine.say("WHO-IS.")
    engine.runAndWait()

    engine.say("What is your option ?")
    engine.runAndWait()

    print(ip_options.strip()+"\n")

    ip_option = input("What is your option ? :")

    os.system("cls")

    while ip_option not in ["1","2"]:

        frequency = 870
        duration = 1500
        winsound.Beep(frequency, duration)

        engine.say("Please choose the first or secondary option.")
        engine.runAndWait()

        messagebox.showwarning("V Cleaner :", "Please choose the first or secondary option.")

        print(ip_options.strip())

        ip_option = input("\nWhat is your option ? :")

        os.system("cls")

    if ip_option == "1":

        engine.say("What is the IP address ?")
        engine.runAndWait()

        ip = input("What is the IP address ? :")

        os.system("cls")

        engine.say("""
        Please transmit a valid IP address.
        Otherwise, this may result in a negative result.""")
        engine.runAndWait()

        messagebox.showinfo("V Cleaner :", """
        Please transmit a valid IP address.
        Otherwise, this may result in a negative result.""")

        engine.say("Please wait, the search for the IP address :" +" " +str(ip) +" " "information is in progress.")
        engine.runAndWait()

        print("Please wait, the search for the IP address :" +" " +str(ip) +" " "information is in progress...")

        time.sleep(5)

        os.system("cls")

        Malwares = "https://www.malwares.com/report/ip?ip="+str(ip)
        WMA = "https://whatismyipaddress.com/ip/"+str(ip)
        webbrowser.open(Malwares)
        webbrowser.open(WMA)

        print(logo)
        options()

    elif ip_option == "2":

        engine.say("What is the IP address ?")
        engine.runAndWait()

        ip = input("What is the IP address ? :")

        os.system("cls")

        engine.say("""
        Please transmit a valid IP address.
        Otherwise, this may result in a negative result.""")
        engine.runAndWait()

        messagebox.showinfo("V Cleaner :", """
        Please transmit a valid IP address.
        Otherwise, this may result in a negative result.""")

        engine.say("Please wait, the WHOIS search for the IP address :" +" " +str(ip) +" " "is in progress.")
        engine.runAndWait()

        print("Please wait, the WHOIS search for the IP address :" +" " +str(ip) +" " "is in progress...")
        
        time.sleep(5)

        os.system("cls")

        WHOIS = "https://who.is/whois-ip/ip-address/"+str(ip)
        webbrowser.open(WHOIS)

        print(logo)
        options()

def port():
    
    engine.say("What is the port ?")
    engine.runAndWait()

    port = input("What is the port ? :")

    os.system("cls")

    while port not in range(65536):

        frequency = 870
        duration = 1500
        winsound.Beep(frequency, duration)

        engine.say("Please choose a port between 0 and 65536.")
        engine.runAndWait()

        messagebox.showwarning("V Cleaner :", "Please choose a port between 0 and 65536.")

        port = input("What is the port ? :")

        os.system("cls")

    engine.say("Please wait, the search for the port :" +" " +str(port) +" " "information is in progress.")
    engine.runAndWait()

    print("Please wait, the search for port :" +" " +str(port) +" " "information is in progress...")
    
    time.sleep(5)
    os.system("cls")

    speedguide = "https://www.speedguide.net/port.php?port="+str(port)
    webbrowser.open(speedguide)

    os.system("cls")
    
    print(logo)
    options()

def process():
    
    engine.say("What is the process ?")
    engine.runAndWait()

    process = input("What is the process ? :")

    os.system("cls")

    while process not in [str(".exe")]:

        frequency = 870
        duration = 1500
        winsound.Beep(frequency, duration)

        engine.say("Please transmit the name of the process and its extension: .exe")
        engine.runAndWait()

        messagebox.showwarning("V Cleaner :", "Please transmit the process name and its correct extension.")

        engine.say("What is the process ?")
        engine.runAndWait()

        process = input("What is the process ? :")

        os.system("cls")

    engine.say("Please wait, the search for process :" +" " +str(process) +" " "information is in progress.")
    engine.runAndWait()

    print("Please wait, the search for process :" +" " +str(process) +" " "information is in progress...")
    
    time.sleep(5)

    os.system("cls")

    file = "https://www.fichier.net/processus/"+str(process)
    webbrowser.open(file)
    
    os.system("cls")
    
    print(logo)
    options()

def DLL():
    
    engine.say("What is the DLL ?")
    engine.runAndWait()

    DLL = input("What is the DLL ? :")

    os.system("cls")

    while DLL not in [str(".dll")]:

        frequency = 870
        duration = 1500
        winsound.Beep(frequency, duration)

        engine.say("Please transmit the name of the DLL, as well as its correct extension : .dll")
        engine.runAndWait()

        messagebox.showwarning("V Cleaner :", "Please transmit the name of the DLL, as well as its correct extension.")

        engine.say("What is the DLL ?")
        engine.runAndWait()

        DLL = input("What is the DLL ? :")

        os.system("cls")

    engine.say("Please wait, the search for DLL :" +" " +str(DLL) +" " "information is in progress.")
    engine.runAndWait()

    print("Please wait, the search for DLL :" +" " +str(DLL) +" " "information is in progress...")
    
    time.sleep(5)

    os.system("cls")

    file = "https://www.fichier.net/processus/"+str(DLL)
    webbrowser.open(file)
    
    print(logo)
    options()

def process_2():
    
    engine.say("Please wait, the display of running processes is in progress.")
    engine.runAndWait()

    print("Please wait, the display of running processes is in progress...")

    time.sleep(5)

    os.system("cls")

    os.system("tasklist /m")
    os.system("pause > nul")
    
    os.system("cls")
    
    print(logo)
    options()
    
def network():
    
    engine.say("Please wait, displaying information about network connections is in progress.")
    engine.runAndWait()

    print("Please wait, displaying information about network connections is in progress...")
    
    time.sleep(5)

    os.system("cls")

    os.system("netstat -b")
    os.system("pause > nul")

    os.system("cls")

    os.system("netstat -ano")
    os.system("pause > nul")

    os.system("cls")

    print(logo)
    options()
    
def corruptions():
    
    engine.say("Please wait, determination of Windows-related corruption is in progress.")
    engine.runAndWait()

    print("Please wait, determination of Windows-related corruption is in progress...")
    
    time.sleep(5)

    os.system("cls")

    os.system("DISM /Online /Cleanup-Image /CheckHealth")
    os.system("pause > nul")
    
    os.system("cls")

    print(logo)
    options()

def analyse():
    
    engine.say("Please wait, an analysis of various Windows issues is in progress.")
    engine.runAndWait()

    print("Please wait, an analysis of various Windows issues is in progress...")
    
    time.sleep(5)

    os.system("cls")

    os.system("DISM /Online /Cleanup-Image /ScanHealth")
    os.system("pause > nul")

    os.system("cls")
    
    print(logo)
    options()

def repair():

    engine.say("Please wait, an analysis as well as the repair of various problems related to Windows is in progress.")
    engine.runAndWait()

    print("Please wait, an analysis as well as the repair of various problems related to Windows is in progress...")
    
    time.sleep(5)

    os.system("cls")

    os.system("DISM /Online /Cleanup-Image /RestoreHealth")
    os.system("pause > nul")

    os.system("cls")
    
    print(logo)
    options()

def firewall():
    
    engine.say("Please wait, firewall activation is in progress.")
    engine.runAndWait()

    print("Please wait, firewall activation is in progress...")
    
    time.sleep(5)

    os.system("cls")

    os.system("netsh advfirewall set allprofiles state on")
    
    time.sleep(5)

    os.system("cls")
    
    print(logo)
    options()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

messagebox.showinfo("Support me :", """
If you wish, you can make a donation on my PayPal account.\n
PayPal : https://www.paypal.com/paypalme/AnonSpenex
Thanking you for your sympathy.""")

engine.say("""
If you encounter difficulties or problems with the program, please contact me via this email address :
anon.spenexploit@protonmail.com""")

engine.runAndWait()

messagebox.showinfo("Informations :", """
If you encounter difficulties or problems with the program, please contact me via this email address :\n 
anon.spenexploit@protonmail.com""")

engine.say("In order to use this program in the best conditions, it is recommended to run it as an administrator.")
engine.runAndWait()

messagebox.showinfo("Informations :", """
In order to use this program in the best conditions, it is recommended to run it as an administrator.""")

print(logo)
options()
