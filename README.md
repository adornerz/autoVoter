# autoVoter
Auto voter script for a minecraft server on topminecraftservers.org with protonvpn IPs. <br/>
This is a simple python script which votes for our minecraft server with every Protonvpn free servers, adding 16 votes everyday.
It's build using selenium, and it won't work on Windows, so you need a linux machine for this.
Yeah that was it, don't expect an 100% clean code I put this up in 10 mins.
Aight bye and vote for the minecaft server, the link is inside the code.

## Table of Contents
- Installation
- Usage
- Keep-in-mind

###  Installation
To run this script you need:
- A linux machine: This script does not work on windows as windows doesn't have protonvpn cli version.
- Protonvpn-cli: to install on debian use `sudo apt install protonvpn-cli` and in manjaro use `pamac build protonvpn-cli` in terminal.
- Firefox; You can change selenium to use chrome as well but eh why would you.
- Geckodriver: this is needed so selenium can work with firefox. If you don't have it installed then download it [here](https://github.com/mozilla/geckodriver/releases) then move the `geckodriver` executable in `/usr/local/bin`, or if that doesn't work with you try `/usr/bin`.
- Patience.

### Usage

Pretty simple, just run the script and wait. Since topminecraftservers.org let you vote only once per day you should run the script daily. Note that others might be using this script as well and it might tell you "You Already Voted For Today", nothing I can do about that.

### Keep In Mind
This script is not perfect, far from it and it might break sometimes. I didn't handle the error if "You Already Voted For Today" shows up because I think you are grown up enough to understand that. Star this repo if you will use the script so ppl can see how many are using it. <br/>
That's pretty much it, see ya.
