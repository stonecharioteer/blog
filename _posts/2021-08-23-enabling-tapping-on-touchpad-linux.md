---
title: Enabling Tapping on the Touchpad in Linux
layout: post
categories: [linux]
description: "How to fix your laptop's touchpad in Linux so that you can tap to click."
---

I've been trying to improve my Linux user experience lately. I use a Dell G5 SE
laptop, and it isn't the best laptop to use Linux in. I bought this thing only
because I didn't find another pure-AMD laptop at the time.

I run Manjaro XFCE, and I've had some issues running it. I'm a Linux Mint user
most of the time, and as of this writing I'm waiting for the Mint experience to
improve on this laptop.

This post is mostly to just remind myself how to enable tapping on the
touchpad. Earlier, I used to run `xinput` to solve this.

First, run `xinput list` to get the `id` value of the touchpad.

```
xinput list

⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ Logitech M720 Triathlon                 	id=10	[slave  pointer  (2)]
⎜   ↳ DELL09F5:00 04F3:30CB Mouse             	id=12	[slave  pointer  (2)]
⎜   ↳ DELL09F5:00 04F3:30CB Touchpad          	id=13	[slave  pointer  (2)]
⎜   ↳ ETPS/2 Elantech Touchpad                	id=15	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Video Bus                               	id=6	[slave  keyboard (3)]
    ↳ Power Button                            	id=7	[slave  keyboard (3)]
    ↳ Sleep Button                            	id=8	[slave  keyboard (3)]
    ↳ liliums Lily58                          	id=9	[slave  keyboard (3)]
    ↳ Integrated_Webcam_HD: Integrate         	id=11	[slave  keyboard (3)]
    ↳ AT Translated Set 2 keyboard            	id=14	[slave  keyboard (3)]
    ↳ Logitech M720 Triathlon                 	id=16	[slave  keyboard (3)]
```

Here, the device I want is `DELL09F5:00 04F3:30CB Touchpad` and as you can see,
the `id` is 13. So next, let's see the properties of the touchpad.

```
xinput list-props 13


Device 'DELL09F5:00 04F3:30CB Touchpad':
	Device Enabled (163):	1
	Coordinate Transformation Matrix (165):	1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000
	libinput Tapping Enabled (320):	0
	libinput Tapping Enabled Default (321):	0
	libinput Tapping Drag Enabled (322):	1
	libinput Tapping Drag Enabled Default (323):	1
	libinput Tapping Drag Lock Enabled (324):	0
	libinput Tapping Drag Lock Enabled Default (325):	0
	libinput Tapping Button Mapping Enabled (326):	1, 0
	libinput Tapping Button Mapping Default (327):	1, 0
	libinput Natural Scrolling Enabled (298):	0
	libinput Natural Scrolling Enabled Default (299):	0
	libinput Disable While Typing Enabled (328):	1
	libinput Disable While Typing Enabled Default (329):	1
	libinput Scroll Methods Available (300):	1, 1, 0
	libinput Scroll Method Enabled (301):	1, 0, 0
	libinput Scroll Method Enabled Default (302):	1, 0, 0
	libinput Click Methods Available (330):	1, 1
	libinput Click Method Enabled (331):	1, 0
	libinput Click Method Enabled Default (332):	1, 0
	libinput Middle Emulation Enabled (307):	0
	libinput Middle Emulation Enabled Default (308):	0
	libinput Accel Speed (309):	0.000000
	libinput Accel Speed Default (310):	0.000000
	libinput Accel Profiles Available (311):	1, 1
	libinput Accel Profile Enabled (312):	1, 0
	libinput Accel Profile Enabled Default (313):	1, 0
	libinput Left Handed Enabled (314):	0
	libinput Left Handed Enabled Default (315):	0
	libinput Send Events Modes Available (283):	1, 1
	libinput Send Events Mode Enabled (284):	0, 0
	libinput Send Events Mode Enabled Default (285):	0, 0
	Device Node (286):	"/dev/input/event10"
	Device Product ID (287):	1267, 12491
	libinput Drag Lock Buttons (316):	<no items>
	libinput Horizontal Scroll Enabled (317):	1
	libinput Scrolling Pixel Distance (318):	15
	libinput Scrolling Pixel Distance Default (319):	15
```

The line we are interested in shows something regarding tapping. So let's
filter the nonsense out.

```
xinput list-props 13 | grep -i tap

	libinput Tapping Enabled (320):	0
	libinput Tapping Enabled Default (321):	0
	libinput Tapping Drag Enabled (322):	1
	libinput Tapping Drag Enabled Default (323):	1
	libinput Tapping Drag Lock Enabled (324):	0
	libinput Tapping Drag Lock Enabled Default (325):	0
	libinput Tapping Button Mapping Enabled (326):	1, 0
	libinput Tapping Button Mapping Default (327):	1, 0
```

The first line here, `libinput Tapping Enabled (320):	0` is what we are
interested in. Let's set that to `1`.

```
xinput set-prop 13 320 1
```

This command sets the property ID 320 of device ID 13 to 1, which is what we
need.

A quick perusal of our previous command will reveal that the value has indeed
changed to `1`. However, you can also check that merely tapping your touchpad
to click works now.

While you *could* stuff this line into your `.xinputrc` file and have it run
there, know that the device ID _will_ change often. You shouldn't rely on it.
Instead, you need to persist these settings by modifying the xinput settings
file for your touchpad. Default configurations for xinput are in
`/usr/share/X11/xorg.conf.d/40-libinput.conf`, which you *should not modify*.
Instead, _copy_ the file to `/etc/X11/xorg.conf.d/40-libinput.conf`, which
normally shouldn't exist.

Now, find the section that looks like this:

```
Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"
EndSection
```

Just before `EndSection`, add `Option "Tapping" "on"`, so that the section now
looks like:

```
Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"
        Option "Tapping" "on"
EndSection
```

Now, save this file and reboot. This should preserve your settings even if your
touchpad device ID changes.

To see more settings you can modify for `libinput`, check out the [man pages](https://www.mankier.com/4/libinput).

