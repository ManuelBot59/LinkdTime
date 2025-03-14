<p align = "center"><img src = "Banner/Banner.png" ></p>

<p align = "center">
  <img src = "https://img.shields.io/github/stars/Lucksi/LinkdTime">
  <img src = "https://img.shields.io/github/forks/Lucksi/LinkdTime">
  <img src = "https://img.shields.io/badge/Maintained%3F-yes-green.svg">
  <img src = "https://img.shields.io/github/license/Lucksi/LinkdTime">
  <img src = "https://img.shields.io/github/repo-size/Lucksi/LinkdTime">
  <img src= "https://img.shields.io/github/languages/count/Lucksi/LinkdTime">
</p>

## Introduction

**LinkdTime is a Timeline generator for Linkedin it can extract the exact date and time on a single post/comments or activity or generate a Timeline about a list of post/comments or activity**

## Screenshot:
<img src = "Screenshots/Screenshot.png" >

## Requirements:
```
Python3
```

## Installation Linux:
```bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install git
git clone https://github.com/Lucksi/LinkdTime
```
## Execution:
```bash
cd LinkdTime
python3 main.py
```

## Operating Sytstems:

| Platform | Tested |
| ------------- | ------------- |
| Linux  | ✅ |
| Mac-Os  | ❌ |
| Windows | ❌ |


## Recognized Activities:
| Name
| -------------
| `Posts` 
| `Comments`
| `Comments/Replies`
| `Profile-Pictures Changes`
| `Background-Images Changes`
| `Company-Logo Changes`

## Current Features:
| Feauture list | Require Internet |
| ------------- | ----------------|
| `Extracting Activity timestamp`  | False
| `Create Timelines`|  False
| `Timezone Change` | False
| `Saving images in Base64 format (Timelines only)` | True
| `Download images (Timelines only)`| True

## Timeline Example:

<img src = "Screenshots/Screenshot_Timeline.png" >

## Configuration:
| Parameter Name | Values | Default Value | Description |
| ------------- | ------------- | -------------| ------------ |
| `DATE-FORMAT` | Eu/Us/As| Eu | Date format used ex: '01/01/2025'
| `USER-AGENT` | input string | Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 | User agent used for downloading images
| `AUTO-DOWNLOAD` | True/False| False | Auto download for images (Timeline Only)
| `CLOCK-FORMAT` | 12/24| 24 | Clock format this is used for determine how many hours the clock will have. For the 12 hours clock it will be displayed AM (Morning) or PM (Afternoon)


## Advanced Commands:

| Option name | Description | Query Example |
| ------------- | ------------- | -------------|
| `timeline`  | Create a timeline from a group of activities| timeline test.txt |
| `--autoname`  | Generate a default name for each element in the timeline | timeline test.txt --autoname |
| `--description`  | Allows you to insert a description for each element in the timeline | timeline test.txt --description |
| `--save`  | Allows you to save images in base64 | timeline test.txt --save |
| `--download`  |Allows you to download images | timeline test.txt --save --download |
| `--timezone`  | Set a Timezone for the results (works with timelines and standalone links) (default GMT+2:OO) | timeline test.txt --timezone GMT+4:00 |

## Autoname Default element name example:
```bash
Element n°1
```

## Supported Timelines formats:
| Format Name | Extension 
| ------------- | -------------
| `Text File Format` | txt
| `Hyper Text Markup Language` | html




## STARGAZERS OVER TIME 

[![Stargazers over time](https://starchart.cc/Lucksi/LinkdTime.svg)](https://starchart.cc/Lucksi/LinkdTime)

<br>

## <p align = center>  ORIGINAL CREATOR: <a href = "https://github.com/Lucksi">LUCA GAROFALO (Lucksi)</a></p>


## <p align = center>LICENSE: GPL-3.0 License <br>COPYRIGHT: (C) 2025 Lucksi  
