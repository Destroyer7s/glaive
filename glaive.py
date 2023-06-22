import subprocess
import time
import os

sources = [
    'anubis', 'baidu', 'bevigil', 'binaryedge', 'bing', 'bingapi', 'bufferoverun',
    'brave', 'censys', 'certspotter', 'criminalip', 'crtsh', 'dnsdumpster',
    'duckduckgo', 'fullhunt', 'github-code', 'hackertarget', 'hunter', 'hunterhow',
    'intelx', 'otx', 'pentesttools', 'projectdiscovery', 'rapiddns', 'rocketreach',
    'securityTrails', 'sitedossier', 'subdomainfinderc99', 'threatminer', 'urlscan',
    'virustotal', 'yahoo', 'zoomeye'
]

domain = input("Enter the domain: ")

save_to_file = input("Do you want to save the results to a file? (y/n): ")

if save_to_file.lower() == 'y':
    log_file = input("Enter the filename to save the results to: ")
    if not os.path.splitext(log_file)[1]:
        log_file += ".txt"
else:
    log_file = None


def remove_text_block(input_file, output_file):
    start_marker = '*******************************************************************'
    end_marker = '*******************************************************************'

    input_path = os.path.join(os.getcwd(), input_file)

    with open(input_path, 'r') as file:
        lines = file.readlines()

    output_lines = []
    skip = False

    for line in lines:
        if start_marker in line:
            skip = not skip
        elif end_marker in line:
            skip = not skip
        elif not skip:
            output_lines.append(line)

    with open(output_file, 'w') as file:
        file.writelines(output_lines)

    print(f"The block of text has been removed from {input_file} and saved to {output_file}.")


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

try:
    output = ""
    for source in sources:
        print(f"Testing source: {source}")
        command = f"theHarvester -d {domain} -l 500 -b {source}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"An error occurred while executing theHarvester for {source}.")
            continue  # Move to the next source
        if "not recognized" in result.stdout:
            print(f"theHarvester for {source} is not recognized.")
            continue  # Move to the next source
        output += result.stdout

    if log_file:
        with open(log_file, 'w') as f:
            f.write(output)
        # Remove specified lines from the output file
        with open(log_file, 'r') as f:
            lines = f.readlines()
        with open(log_file, 'w') as f:
            skip_next = 0
            for line in lines:
                if skip_next > 0:
                    skip_next -= 1
                    continue
                if line.strip() == '*' * 65:  # Check if the line matches the pattern
                    skip_next = 13  # Skip the next 13 lines
                    continue
                f.write(line)

        print(f"\ntheHarvester completed. Check {log_file} for results.")
        # Call remove_text_block function after theHarvester completes
        remove_text_block(log_file, log_file)

    else:
        # Remove specified lines from the console output
        skip_next = 0
        for line in output.splitlines():
            if skip_next > 0:
                skip_next -= 1
                continue
            if line.strip() == '*' * 65:  # Check if the line matches the pattern
                skip_next = 13  # Skip the next 13 lines
                continue
            print(line)

        print("\ntheHarvester completed. Results are printed on the screen.")

        # Call remove_text_block function after theHarvester completes
        if log_file:
            remove_text_block(log_file, 'output.txt')

except Exception as e:
    print(f"An error occurred: {str(e)}. Check the output file or screen, depending on your choice.")
