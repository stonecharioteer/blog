---
title: No, A Virtual Machine is not enough
categories: [work, wfh, covid, programming, productivity]
---

I use a MacBook Pro 2018 for work. I work in a company which, like many corporates
uses JAMF to manage their Macs. The developer experience is, I have no other
words for it, abysmal.

The alternate for Macs at my workplace is Windows, and that's a whole other
bag of nope. Corporate Windows machines at my previous companies have had
extreme rules placed on the workstations. They give you Dell Latitude or XPS
machines, they're good machines otherwise, but they pile on the bloatware,
and more importantly, they don't let you run anything.

I'm not talking about running Wireshark btw. Of course, if I run that on a
workstation, I've been told that my manager will get a very salicious email.

You cannot run anything on these laptops.

I'm going to break this down into 2 sections: Windows and Macs.

## Windows Experience


### Custom Tooling

Enterprise Windows installations controlled by the IT team usually tells you
that you should not, and *can* not run software you download from the internet
on the laptop. The entire experience is geared towards Managers and people
who either use MS Excel or MS Powerpoint. I have spent my fair share time on
those tools and I would sacrifice them in a heartbeat to have my development
tools work as they should.

In some companies, IT tries to be cool and says you *can* run foreign
executibles, as long as you run them from a specific folder. I've seen this
applied to either `C:\TOOLS` (heh) or `C:\Software`. This is theoretically
a good idea. But now I'd like you to think back to the days when you used Windows and remember how you install *most* of your applications.

They don't go there. *Sure*, you *can* install applications wherever you want,
but the defaults are *defaults* for a very strong reason. Not all applications
allow this sort of Portability in Windows. You *have* places like [portableapps](https://portableapps.com) which give you portable packages of most common tools, but if you read between the lines, you'll realize that this portability is *inapplicable* to a lot of libraries.

The thing with using Windows is that sometimes, your tools depend on system
executibles, and, *surprise, surprise*, you can't execute other executables which are installed elsewhere through forks of the process you're executing from your special, IT-specified folder, since they *will not run*. This becomes a problem for the following reasons:

Python: You cannot make meaningful virtual environments anymore. You *have* to make *all* your `venv` folders in a central location, or fall back to using `conda`, which is yet another problem, since `conda` stores all environments in one central location.

The same problem exists with `Node` and `golang`. *Hell*, this problem is also
persistent with `Rust`!.

The widely accepted way of letting your devs run arbitrary tools on Windows is
dangerously flawed. If I were to get into that scenario (again), I would spend
more hours pulling my hair out rather than write code.

> *Most* software isn't conduicive to installations running willy-nilly on a Windows machine.

### Environment Variables

To add to this problem is Windows' *sweet, sweet Environment Variable* problem.
To add Envvars to Windows, you *need* to use the GUI and set them there.
The dialog not only has a cap of 256 characters (unless you choose to daisy chain them with `%VAR%`), it also has a huge problem with usability. Not to mention, IT blocks the setting of environment variables most of the time. If they don't do it right now, they *will*, sometime.

Why is this a problem? Can't I use a `bat` file with a bunch of `SET VAR=10`
lines?

*Sure*. I *can* do that. But it's not straightforward to `Import-Module` on
starting a Powershell instance, for example. Besides, there's another problem.

### Powershell

Your servers are running Linux. You're already dealing with `bash` foo. Do you want to keep up to date on `Powershell`?

Seriously. I, as do many other developers who care about their custom configs, store my `dotfiles` in Github. The first thing I do when I get a new laptop is run a few `ansible` scripts, and configure my machine to work the way I want. I need my terminal to run flawlessly, with the fonts I prefer, and with the predefined configurations for everything from `neovim`to `pgcli` to `VS Code`.

And why is this important?

It is *crippling* to use a machine which feels foreign to you. You neither
have the energy to recustomize a machine, nor the facility to do so on a Platform like Windows.


### The Arguments

#### Why Not Use Cygwin (or Mingw)?

Ah yes. The time-tested solution(s).

No. Both Cygwin and Mingw will try to get executibles and store them in a
*faux* HOME folder. This will *not* work, because IT specifies that only
one specific folder will work.

Atop of this, not everything that I use will work on both those platforms.
At times, I compile tools that I've found, either written in Golang or in Rust, and these won't have Windows supports some times. If you ask me to abandon those tools, all I have to say is that I am yet to find alteratives for such tools on Windows.

And more importantly, *why should I?* I use them all the time on a Linux machine. Why should I be denied them here?

#### Why not use a Virtual Machine or a Cloud Server and `ssh` into it?

I love this reply. I get it *all* the time. Even from friends who are good
coders.

The problem with this approach is that both of these are horrible experiences
from Windows. With VPNs usually poor at most companies, `ssh` connections are flaky at best. I'd rather use `mosh` to connect to a server. `mosh` is incompatible with Cygwin or MINGW. However, it *does* work with PuTTY.

*However*, Windows is not the best customer for terminal connections, especially if you use multiple monitors.

With a Virtual Machine on your own laptop, you could drop into a nice and fancy Linux instance, but that is again a horrible experience.

#### Use Docker and run multiple Containers

That is a good answer. In fact, this would work, *if* the executibles *and* the firewall isn't blocking everything in red tape from here to Timbucktu.

I'm serious. Docker will not work because of several reasons. You won't have a properly configured HyperVisor on your machine, because IT will say "Why do you need a VM?" *Or*, you will not get it working because of how convoluted your Administrator access protocols are.

#### Use WSL and the Windows Terminal

No. Again, the executible problem and the virtualization within a virtualizor
problem rear their ugly heads.




* Talk about how you cannot debug *why* your bluetooth keyboard or even your DIY
mechanical keyboard won't work on Windows


## MacBook Pro Experience

* Talk about how Minikube won't work on locked laptops because you cannot
override localhost firewall rules.
* Talk about how you can't run modern tools which are not "recognized" by Apple
and you cannot turn off what ever that Guardian app is supposed to be.
* Talk about how the USB protection tools block your access to even your custom
keyboards.
* Talk about the *shitty* Docker on Mac experience.
* Talk about the horrible shell experience where you need to do `xcode-install
--select` after an update.
* Talk about how Bash is outdated.
* Talk about how you can't use `sudo` properly. What do you mean?

## So what, use a Virtual Machine

* No.
* Talk about how a VM is a second-class citizen.
* Talk about how a VM cannot properly use the underlying hardware. Proprietary
tooling is locked into the base hardware.
* Talk about how you cannot ssh into servers on your company network through an
OSS Ubuntu VM
* Talk about how you cannot use modern CLIs to search through your files, which
you could use through mounting the disks, but that wouldn't work
* Talk about the lack of multimonitor experience.

## So what, use a cloud server, it has 256 GB RAM

* Lack of multimonitor experience.
* Network / VPN issues ruin it
* Not straightforward to install things you want/need
* Not easy to search for things on your local laptop.

## So what do you want, hotshot?

* Linux, preferably a home-grown distro.
* Bake in your dependencies, but give me posix
* 1 TB SSD 64 GB RAM AMD Ryzen 7 CPU and an Nvidia (although fuck 'em GPU')
* Teams should

## We're a corporate, we cannot give you a Linux Machine

* Yes you can.
* Redhat offers corporate offerings.
* Get Fedora, use that.
* Use Centos (Or Don't)
* Use a Windows VM! (Haha, no, seriously.)
* Use a Linux
