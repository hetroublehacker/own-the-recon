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

### Subdomain Takeover

#### Subjack
```
$ go install github.com/haccer/subjack@latest
$ subjack -w subdomains.txt -t 100 -timeout 30 -ssl -c fingerprints.json -v
```

#### Subzy
```
$ go install -v github.com/lukasikic/subzy@latest
$ subzy run --targets subdomains.txt --concurrency 100 --hide_fails --verify_ssl
```

#### Nuclei (takeover templates)
```
$ nuclei -l subdomains.txt -t http/takeovers/
```

### Content Discovery & Fuzzing

#### FFUF
```
$ go install github.com/ffuf/ffuf/v2@latest
$ ffuf -u https://<TARGET>/FUZZ -w wordlist.txt -mc 200,301,302,403
```

#### Feroxbuster
```
$ curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/master/install-nix.sh | bash
$ feroxbuster -u https://<TARGET> -w wordlist.txt -x php,html,js
```

#### Wfuzz
```
$ pip3 install wfuzz
$ wfuzz -c -z file,wordlist.txt --hc 404 https://<TARGET>/FUZZ
```

#### Kiterunner
```
$ go install github.com/assetnote/kiterunner/cmd/kr@latest
$ kr scan hosts.txt -w routes.kite -x 10
```

### Secret & Credential Discovery

#### Trufflehog
```
$ curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin
$ trufflehog git https://github.com/<ORG>/<REPO> --only-verified
```

#### Gitleaks
```
$ go install github.com/zricethezav/gitleaks/v8@latest
$ gitleaks detect --source . --verbose
```

#### GitDorker
```
$ git clone https://github.com/obheda12/GitDorker.git
$ cd GitDorker
$ pip3 install -r requirements.txt
$ python3 GitDorker.py -tf tokens.txt -q <DOMAIN> -d Dorks/medium_dorks.txt
```

### XSS & Injection Testing

#### Dalfox
```
$ go install github.com/hahwul/dalfox/v2@latest
$ cat urls.txt | dalfox pipe --silence
```

#### XSStrike
```
$ git clone https://github.com/s0md3v/XSStrike.git
$ cd XSStrike
$ pip3 install -r requirements.txt
$ python3 xsstrike.py -u "https://<TARGET>/?q=test"
```

#### SQLMap
```
$ git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
$ cd sqlmap
$ python3 sqlmap.py -u "https://<TARGET>/?id=1" --batch --random-agent
```

### CORS & Misconfiguration

#### Corsy
```
$ git clone https://github.com/s0md3v/Corsy.git
$ cd Corsy
$ pip3 install -r requirements.txt
$ python3 corsy.py -i urls.txt
```

#### CRLFuzz
```
$ go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest
$ crlfuzz -l urls.txt
```

### HTTP Smuggling & Advanced Web

#### Smuggler
```
$ git clone https://github.com/defparam/smuggler.git
$ cd smuggler
$ python3 smuggler.py -u https://<TARGET>
```

### Screenshots & Visual Recon

#### Gowitness
```
$ go install github.com/sensepost/gowitness@latest
$ gowitness file -f urls.txt --threads 10
```

#### EyeWitness
```
$ git clone https://github.com/RedSiege/EyeWitness.git
$ cd EyeWitness/Python/setup
$ ./setup.sh
$ python3 ../EyeWitness.py -f urls.txt --web
```

### Wordlists

#### SecLists
```
$ git clone https://github.com/danielmiessler/SecLists.git /opt/SecLists
```

#### Assetnote Wordlists
```
$ wget -r --no-parent -nH --cut-dirs=1 https://wordlists-cdn.assetnote.io/data/
```

#### Commonspeak2
```
$ go install github.com/assetnote/commonspeak2@latest
$ commonspeak2 subdomains -p bigquery-project
```

### Out-of-Band & OSINT

#### Interactsh
```
$ go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
$ interactsh-client
```

#### Notify
```
$ go install -v github.com/projectdiscovery/notify/cmd/notify@latest
$ cat alerts.txt | notify -provider-config provider.yaml
```

#### Uncover
```
$ go install -v github.com/projectdiscovery/uncover/cmd/uncover@latest
$ uncover -q "ssl:<DOMAIN>" -e shodan,censys,fofa
```

#### Shosubgo
```
$ go install github.com/incogbyte/shosubgo@latest
$ shosubgo -d <DOMAIN> -s <SHODAN_API_KEY>
```

### Network & ASN

#### Asnmap
```
$ go install github.com/projectdiscovery/asnmap/cmd/asnmap@latest
$ asnmap -d <DOMAIN> -silent
```

#### Mapcidr
```
$ go install -v github.com/projectdiscovery/mapcidr/cmd/mapcidr@latest
$ echo "192.168.0.0/16" | mapcidr -silent
```

#### Cdncheck
```
$ go install -v github.com/projectdiscovery/cdncheck/cmd/cdncheck@latest
$ cat ips.txt | cdncheck
```

#### Tlsx
```
$ go install github.com/projectdiscovery/tlsx/cmd/tlsx@latest
$ tlsx -l hosts.txt -san -cn -resp-only
```

### Subdomain Permutation & DNS

#### Dnsgen
```
$ pip3 install dnsgen
$ cat subdomains.txt | dnsgen -
```

#### Gotator
```
$ go install github.com/Josue87/gotator@latest
$ gotator -sub subdomains.txt -perm permutations.txt -depth 1 -numbers 10 -mindup
```

#### MassDNS
```
$ git clone https://github.com/blechschmidt/massdns.git
$ cd massdns && make
$ ./bin/massdns -r resolvers.txt -t A -o S subdomains.txt
```

### Crawling Utilities

#### Gospider
```
$ go install github.com/jaeles-project/gospider@latest
$ gospider -s https://<TARGET> -c 10 -d 3
```

#### Waymore
```
$ pip3 install waymore
$ waymore -i <DOMAIN> -mode U -oU urls.txt
```

#### XnLinkFinder
```
$ pip3 install xnLinkFinder
$ xnLinkFinder -i https://<TARGET> -d 2
```

### Tomnomnom Pipeline Utilities

#### Anew
```
$ go install -v github.com/tomnomnom/anew@latest
$ cat new.txt | anew existing.txt
```

#### GF (Pattern Matching)
```
$ go install -v github.com/tomnomnom/gf@latest
$ git clone https://github.com/1ndianl33t/Gf-Patterns ~/.gf
$ cat urls.txt | gf xss
```

#### Qsreplace
```
$ go install github.com/tomnomnom/qsreplace@latest
$ cat urls.txt | qsreplace "FUZZ"
```

#### Unfurl
```
$ go install github.com/tomnomnom/unfurl@latest
$ cat urls.txt | unfurl domains
```

#### Meg
```
$ go install github.com/tomnomnom/meg@latest
$ meg /paths hosts.txt
```

### WAF & Tech Detection

#### Wafw00f
```
$ pip3 install wafw00f
$ wafw00f https://<TARGET>
```

#### Whatweb
```
$ sudo apt-get install whatweb
$ whatweb https://<TARGET>
```

### Cloud & S3 Bucket Hunting

#### S3Scanner
```
$ pip3 install s3scanner
$ s3scanner scan --bucket-file buckets.txt
```

#### CloudList
```
$ go install -v github.com/projectdiscovery/cloudlist/cmd/cloudlist@latest
$ cloudlist -config provider-config.yaml
```


> Note: All credit goes to the original developers of the tools in this repository. I've just listed them in this repository.



[![Twitter Follow](https://img.shields.io/twitter/follow/hetroublemakr?color=RED&style=flat-square)](https://twitter.com/hetroublemakr)

