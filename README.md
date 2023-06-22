# glaive



![Image Description](assets/main.png)



## Introduction

glaive is a tool used for gathering information about a specific domain. It queries various sources and collects data such as email addresses, subdomains, and more all through the power of  [theHarvestor ]( https://github.com/laramies/theHarvester) tool

-->  Now allows saving condensed output to a file 🇦🇨  <--


## Usage

1. Clone the repository:

```bash
git clone https://github.com/Destroyer7s/glaive.git
```

<!-- ignore 

2. Install the dependencies:

pip install -r requirements.txt

 -->

2. Run glaive:

```bash
python3 glaive.py
```

3. Enter the domain when prompted.

4. Wait for theHarvester to gather information from different sources.

5. Check the HarvesterLog.txt for the results.


# Sources

The following sources are used by theHarvester to collect data:

- anubis
- baidu
- bevigil
- binaryedge
- bing
- bingapi
- bufferoverun
- brave
- censys
- certspotter
- criminalip
- crtsh
- dnsdumpster
- duckduckgo
- fullhunt
- github-code
- hackertarget
- hunter
- hunterhow
- intelx
- otx
- pentesttools
- projectdiscovery
- rapiddns
- rocketreach
- securityTrails
- sitedossier
- subdomainfinderc99
- threatminer
- urlscan
- virustotal
- yahoo
- zoomeye

## Output

glaive uses theHarvestor tool to collect data and stores it in the HarvesterLog.txt file. Each source's results are listed separately.

## Disclaimer

Please use theHarvester responsibly and respect the privacy and security of others. Usage of this tool for malicious purposes is strictly prohibited.
