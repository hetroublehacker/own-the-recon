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
$ tar xvf go1.16.5.linux-amd64.tar.gz
$ sudo chown -R root:root ./go
$ sudo mv go /usr/local
$ rm -rf go1.16.5.linux-amd64.tar.gz
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



> Note: All credit goes to the original developers of the tools in this repository. I've just listed them in this repository.



[![Twitter Follow](https://img.shields.io/twitter/follow/hetroublemakr?color=RED&style=flat-square)](https://twitter.com/hetroublemakr)

