# Own The Recon.

***Tools and scripts setting up guide.***

This repository contains all the tools which are listed on my recent blog post "Recon Like you own it!" amd i personally use.
here is my blog post https://medium.com/cyberverse/recon-like-you-owns-it-190175c81c42


## Required dependencis

```
$ sudo apt-get upgrade
$ sudo apt-get update
$ sudo apt-get install git      //install git
$ apt install curl              //install curl
$ apt-get install ruby-full     //install ruby
$ apt install python-pip        //install pip
$ apt install python3-pip	      //for python 3
```

### Go language installation.
```
$ curl -O https://go.dev/dl/go1.21.0.linux-amd64.tar.gz
$ tar xvf go1.21.0.linux-amd64.tar.gz
$ sudo chown -R root:root ./go
$ sudo mv go /usr/local
$ rm -rf go1.21.0.linux-amd64.tar.gz
$ vi ~/.profile
```
### and add the following lines in `.profile`
```
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```
source ~/.profile

## Downloading the tools

### Subfinder
```
$ go get github.com/subfinder/subfinder
```

### Amass
```
$ go get -u github.com/OWASP/Amass/...
```

### Knockpy
```
$ git clone https://github.com/guelfoweb/knock.git
$ cd knock
$ sudo apt-get install python-dnspython
$ Setup your VirusTotal_api key: nano knockpy/config.json
$ sudo python setup.py install
```

### Findomain
```
$ git clone https://github.com/Edu4rdSHL/findomain.git
$ cd findomain
$ sudo apt-get install cargo      //install cargo
$ cargo build --release  
$ sudo cp target/release/findomain /usr/bin/
$ findomain
```

### Assetfinder
```
$ go get -u github.com/tomnomnom/assetfinder
```

### Dirsearch
```
$ git clone https://github.com/maurosoria/dirsearch.git
$ cd dirsearch
$ python3 dirsearch.py -u <URL> -e <EXTENSION>
```

### Gobuster
```
$ go get github.com/OJ/gobuster
```

### AltDNS
```
$ pip install py-altdns
```

### Aquatone
```
$ go get github.com/michenriksen/aquatone
```

### WebScreenshot
```
$ pip install webscreenshot
```

### Httprobe
```
$ go get -u github.com/tomnomnom/httprobe
```

### Waybackurl
```
$ go get github.com/tomnomnom/waybackurls
```

### LazyS3
```
$ git clone https://github.com/nahamsec/lazys3.git
$ cd lazys3
$ ruby lazys3.rb <COMPANY>
```

## Elite Bug Bounty Tier

The following toolkit reflects the modern, professional-grade recon stack used at the **elite bounty tier**. These tools complement the basics above and are essential for serious bug hunters chasing critical bounties.

### Subdomain Enumeration (Advanced)

#### Shuffledns
```
$ go install github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest
$ shuffledns -d <DOMAIN> -w wordlist.txt -r resolvers.txt
```

#### Puredns
```
$ go install github.com/d3mondev/puredns/v2@latest
$ puredns bruteforce wordlist.txt <DOMAIN> -r resolvers.txt
```

#### DNSx
```
$ go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
$ dnsx -l subdomains.txt -resp -a -aaaa -cname -mx -ns -txt
```

#### GitHub-Subdomains
```
$ go install github.com/gwen001/github-subdomains@latest
$ github-subdomains -d <DOMAIN> -t <GITHUB_TOKEN>
```

### HTTP Probing & Tech Fingerprinting

#### Httpx
```
$ go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
$ httpx -l subdomains.txt -title -tech-detect -status-code -follow-redirects
```

### Port Scanning

#### Naabu
```
$ go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
$ naabu -list hosts.txt -top-ports 1000 -rate 1000
```

#### Masscan
```
$ sudo apt-get install masscan
$ masscan -p1-65535 <CIDR> --rate=10000
```

### Web Crawling & URL Discovery

#### Katana
```
$ go install github.com/projectdiscovery/katana/cmd/katana@latest
$ katana -u https://<TARGET> -d 5 -jc -kf all
```

#### Gau (GetAllUrls)
```
$ go install github.com/lc/gau/v2/cmd/gau@latest
$ gau <DOMAIN> --threads 50 --providers wayback,commoncrawl,otx,urlscan
```

#### Hakrawler
```
$ go install github.com/hakluke/hakrawler@latest
$ echo https://<TARGET> | hakrawler -d 3
```

### Vulnerability Scanning

#### Nuclei
```
$ go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
$ nuclei -update-templates
$ nuclei -l urls.txt -t cves/ -severity critical,high
```

### JavaScript & Endpoint Analysis

#### SubJS
```
$ go install github.com/lc/subjs@latest
$ cat hosts.txt | subjs
```

#### LinkFinder
```
$ git clone https://github.com/GerbenJavado/LinkFinder.git
$ cd LinkFinder
$ pip3 install -r requirements.txt
$ python3 linkfinder.py -i https://<TARGET>/script.js -o cli
```

### Parameter Discovery

#### Arjun
```
$ pip3 install arjun
$ arjun -u https://<TARGET>/endpoint -oT params.txt
```

#### ParamSpider
```
$ git clone https://github.com/devanshbatham/ParamSpider.git
$ cd ParamSpider
$ pip3 install -r requirements.txt
$ python3 paramspider.py -d <DOMAIN>
```

### Cloud Asset Enumeration

#### Cloud_Enum
```
$ git clone https://github.com/initstring/cloud_enum.git
$ cd cloud_enum
$ pip3 install -r requirements.txt
$ python3 cloud_enum.py -k <KEYWORD>
```

### Recon Frameworks

#### ReconFTW
```
$ git clone https://github.com/six2dez/reconftw.git
$ cd reconftw
$ ./install.sh
$ ./reconftw.sh -d <DOMAIN> -r
```

#### Project Discovery Tool Manager (PDTM)
```
$ go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest
$ pdtm -install-all
```


> Note: All credit goes to the original developers of the tools in this repository. I've just listed them in this repository.



[![Twitter Follow](https://img.shields.io/twitter/follow/hetroublemakr?color=RED&style=flat-square)](https://twitter.com/hetroublemakr)

