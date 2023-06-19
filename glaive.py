import subprocess
import time

sources = [
    'anubis', 'baidu', 'bevigil', 'binaryedge', 'bing', 'bingapi', 'bufferoverun',
    'brave', 'censys', 'certspotter', 'criminalip', 'crtsh', 'dnsdumpster',
    'duckduckgo', 'fullhunt', 'github-code', 'hackertarget', 'hunter', 'hunterhow',
    'intelx', 'otx', 'pentesttools', 'projectdiscovery', 'rapiddns', 'rocketreach',
    'securityTrails', 'sitedossier', 'subdomainfinderc99', 'threatminer', 'urlscan',
    'virustotal', 'yahoo', 'zoomeye'
]

log_file = 'HarvesterLog.txt'

domain = input("Enter the domain: ")

# Animated splash screens
splash1 = """

  ▄████  ██▓     ▄▄▄       ██▓ ██▒   █▓▓█████
 ██▒ ▀█▒▓██▒    ▒████▄    ▓██▒▓██░   █▒▓█   ▀
▒██░▄▄▄░▒██░    ▒██  ▀█▄  ▒██▒ ▓██  █▒░▒███
░▓█  ██▓▒██░    ░██▄▄▄▄██ ░██░  ▒██ █░░▒▓█  ▄
░▒▓███▀▒░██████▒ ▓█   ▓██▒░██░   ▒▀█░  ░▒████▒
 ░▒   ▒ ░ ▒░▓  ░ ▒▒   ▓▒█░░▓     ░ ▐░  ░░ ▒░ ░
  ░   ░ ░ ░ ▒  ░  ▒   ▒▒ ░ ▒ ░   ░ ░░   ░ ░  ░
░ ░   ░   ░ ░     ░   ▒    ▒ ░     ░░     ░
      ░     ░  ░      ░  ░ ░        ░     ░  ░
                                   ░
\n\n
"""

splash2 = """




  ▄████  ██▓    ▄▄▄       ██▓ ██▒   █▓▓█████
 ██▒ ▀█▒▓██▒   ▒████▄    ▓██▒▓██░   █▒▓█   ▀
▒██░▄▄▄░▒██░   ▒██  ▀█▄  ▒██▒ ▓██  █▒░▒███
░▓█  ██▓▒██░   ░██▄▄▄▄██ ░██░  ▒██ █░░▒▓█  ▄
░▒▓███▀▒░██████▒▓█   ▓██▒░██░   ▒▀█░  ░▒████▒
 ░▒   ▒ ░ ▒░▓  ░▒▒   ▓▒█░░▓     ░ ▐░  ░░ ▒░ ░
  ░   ░ ░ ░ ▒  ░ ▒   ▒▒ ░ ▒ ░   ░ ░░   ░ ░  ░
░ ░   ░   ░ ░    ░   ▒    ▒ ░     ░░     ░
      ░     ░  ░     ░  ░ ░        ░     ░  ░
                                  ░

\n\n
"""

splash3 = """
  ▄████ ██▓   ▄▄▄      ██▓██▒   █▓█████
 ██▒ ▀█▓██▒  ▒████▄   ▓██▓██░   █▓█   ▀
▒██░▄▄▄▒██░  ▒██  ▀█▄ ▒██▒▓██  █▒▒███
░▓█  ██▒██░  ░██▄▄▄▄██░██░ ▒██ █░▒▓█  ▄
░▒▓███▀░██████▓█   ▓██░██░  ▒▀█░ ░▒████▒
 ░▒   ▒░ ▒░▓  ▒▒   ▓▒█░▓    ░ ▐░ ░░ ▒░ ░
  ░   ░░ ░ ▒  ░▒   ▒▒ ░▒ ░  ░ ░░  ░ ░  ░
░ ░   ░  ░ ░   ░   ▒   ▒ ░    ░░    ░
      ░    ░  ░    ░  ░░       ░    ░  ░
                              ░
\n\n
"""


splash4 = """


  ▄████  ██▓     ▄▄▄       ██▓ ██▒   █▓▓█████
 ██▒ ▀█▒▓██▒    ▒████▄    ▓██▒▓██░   █▒▓█   ▀
▒██░▄▄▄░▒██░    ▒██  ▀█▄  ▒██▒ ▓██  █▒░▒███
░▓█  ██▓▒██░    ░██▄▄▄▄██ ░██░  ▒██ █░░▒▓█  ▄
░▒▓███▀▒░██████▒ ▓█   ▓██▒░██░   ▒▀█░  ░▒████▒
 ░▒   ▒ ░ ▒░▓  ░ ▒▒   ▓▒█░░▓     ░ ▐░  ░░ ▒░ ░
  ░   ░ ░ ░ ▒  ░  ▒   ▒▒ ░ ▒ ░   ░ ░░   ░ ░  ░
░ ░   ░   ░ ░     ░   ▒    ▒ ░     ░░     ░
      ░     ░  ░      ░  ░ ░        ░     ░  ░
                                   ░

Running theHarvestor...

\n
"""


splash_screens = [splash1, splash2, splash3]

print("\033c")  # Clear the console

for splash in splash_screens:
    print(splash)
    time.sleep(0.1)  # Delay between flashes
    print("\033c")  # Clear the console
    time.sleep(0.05)  # Delay before next flash


print(splash4)

with open(log_file, 'w') as f:
    for source in sources:

        print(f"Testing source: {source}")
        command = f"theHarvester -d {domain} -l 500 -b {source}"
        subprocess.run(command, shell=True, stdout=f, stderr=f)
        f.write('\n')  # Add a line break after each command's output

print("\ntheHarvester completed. Check theHarvesterLog.txt for results.")