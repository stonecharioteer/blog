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

* Talk about how you can install applications *only* into certain folders.
* Talk about how you cannot add Environment variables in some computers
* Talk about Windows' amazing 256 character PATH limitation
* Talk about how *most* software isn't conduicive to installing stuff willy-nilly
on a Windows machine
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

