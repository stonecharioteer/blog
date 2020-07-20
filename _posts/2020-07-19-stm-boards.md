---
title: The STM32F401 Boards
layout: post
categories: [iot, rust]
image: /assets/images/posts/iot/stm32f401.png
description: "A post about the STM32F401 Boards"
customexcerpt: "I finally receives the STM32F401 boards from AliExpress!"
---

![STM Board]()


A while ago, a user posted [a link to this repo](https://github.com/TeXitoi/keyberon) on [/r/mk](https://www.reddit.com/r/mk).

The *madlad* had written firmware for a handmade mechanical keyboard in *Rust*.

I absolutely loved this idea and wanted to get the chip that runs it myself. It was the [STM32F401 board](https://www.st.com/en/microcontrollers-microprocessors/stm32f401.html) running the [Arm Cortex-M4 processor](https://developer.arm.com/ip-products/processors/cortex-m/cortex-m4).

Check this thing out! It has the Armv7 architecture and runs at 84MHz with a performance of 105 DMIPS/285 CoreMark.

[For comparison,](https://www.eembc.org/viewer/?benchmark_seq=13243,13244) the Espressif ESP8266 reaches 80MHz and gets a score of 191, while the ESP32 is at 160MHz and a Coremark of 661.

The STM32F401 costs the same as the ESP8266 and I obviously would be running Rust on it, so I should get much better performance.

And AliExpress had it. Delivery took a couple of months but I finally received them last month. I am going to get busy hacking a rudimentary implementation of this guy's firmware onto this.

I wanted to build a programmable dial into an Altoids box, so perhaps I'll do that. Time to find a dial though!

