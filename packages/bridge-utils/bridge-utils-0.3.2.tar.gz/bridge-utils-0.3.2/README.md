# Introduction

There are several utity tools for writing bridge articles

## Key features (beta release)

* support xinrui url, bbo lin url (bbo soon)
* generate well tuned latex/html bridge layout (card diagram) 
* generate all kinds of ebook (`.pdf`/`.mobi`/`.epub`/`.html`/`.latex`) with related toolchains (`pandoc`,`multimarkdown`)

It contains several subpackage

* xin2pbn
* pbn2html
* mdbridge (mdbridge2latex, mdbrdige2html)

## Install

````
pip install bridge-utils
````

# Usage

## Use case 1: for student newsletter

This is for http://xrgopher.gitee.io/studentbridge

````
zyj-update README.txt
````

Using README.txt, all the materials are combined into `README.md` with xinrui links, then generate HTMLs

````
zyj-convert README.md
````

Then `README.html` and `README.pbn.html` are generated

## Use case 2: mdbridge - Article Samples 

* Ramsey's article for xinrui bridge (Chinese), see [ramsey.md](https://xrgopher.gitlab.io/mdbridge/ramsey.md) and [ramsey.pdf](https://xrgopher.gitlab.io/mdbridge/ramsey.pdf)

You need install [MulitMarkdown](https://fletcherpenney.net/multimarkdown/download/) first

### How to use it

Generally, follow below steps 

* write it in special format with markdown
* use `mdbridge` tool to generate intermediate markdown file
* use `multimarkdown` or `pandoc` to generate related format files
* generate final ebook

See below for latex 

````
$ mdbrdige2latex sample # download sample files ramsey.md, meta.txt
$ mdbridge2latex ramsey.md
ramsey.bridge-tex is created
$ multimarkdown -t latex meta.txt ramsey.bridge-tex -o ramsey.tex
$ xelatex ramsey.tex # use overleaf if u don't have latex env.
````

Then you can edit the file in [overleaf](https://www.overleaf.com) like [ramsey.tex@overleaf.com](https://www.overleaf.com/read/kzwczwjqhxhr)

See below for html

````
$ mdbridge2html ramsey.md
processing ramsey.md -> ramsey.bridge
write to file interesting.pbn
write to file interesting.pbn
$ multimarkdown.exe  -t html ramsey.bridge -o ramsey.html
````

# Usage in detail 

## markdown format

### define the deal from url first

<pre lang="bridge">
http://www.xinruibridge.com/deallog/DealLog.html?bidlog=P,2N,P%3B3C,P,3N,P%3B6N,P,P,P%3B&playlog=E:KD,3D,4D,JD%3BE:2D,5D,7D,AD%3BN:JS,6S,5S,8S%3BN:KS,4S,7S,2S%3BN:3S,TS,AS,8H%3BS:QS,TD,4C,9S%3BS:KH,JH,4H,2H%3BS:AH,TH,9H,3H%3BS:QH,9D,8C,5H%3BS:2C,JC,QC,6C%3BN:KC,9C,6D,5C%3BN:AC,7H,6H,3C%3BN:7C,QD,8D,TC%3B&deal=82.JT8.T974.JT53%20KJ3.94.AJ.AKQ874%20T964.7532.KQ2.96%20AQ75.AKQ6.8653.2&vul=All&dealer=W&contract=6N&declarer=N&wintrick=11&score=-100&str=%E7%BE%A4%E7%BB%84IMP%E8%B5%9B%2020201209%20%E7%89%8C%E5%8F%B7%204/8&dealid=995050099&pbnid=345464272
auction
</pre>

### customize the deal

`deal|cards=NS|ul="<str>"|ll=<str>|ur=<str>`

Two-Hand Diagram

<pre lang="bridge">
deal|cards=NS
</pre>

All-Hands Diagram

<pre lang="bridge">
deal
</pre>

Partial deal

<pre lang="bridge">
deal=.xxxx..xxx&.T4.A.AK87&-&.AKQ6.865.
</pre>

Partial deal with extra information

<pre lang="bridge">
deal=.xxxx..xxx&.94.A.AK87&-&.AKQ6.865.|ll="NS 4/12&EW 0"|ur="match 4/8"
</pre>

# Collaborator

* Ramsey @ xinrui : mainly for latex template and tune the card diagrams

# Reference

* http://www.rpbridge.net/7z69.htm