.. index:: amd, llm, genai, technology

======================================================
Using AMD Radeon GPUs with Ollama
======================================================

.. note::

   This post and its contents are valid for :date:`2024-10-01`. Things with GenAI
   change so often that it's hard to stay valid. I'll version tag everything in the last section of this post.


I picked up an AMD Radeon RX 7900 XTX Nitro+ graphics card last week, and I've been looking forward to it.
I originally considering buying an NVIDIA RTX 4090, but I've given up trying to get Nvidia to play nice with Linux.
My Asus RoG X13 Flow with the 3050 is suffering constantly, and I'm done with trying to get the drivers to stay valid
when I update the Linux Kernel. I've had no luck with the 3070 on my desktop either.

I didn't have to look too hard to get the instructions for how to install the drivers this time. I run both Windows and Linux,
and my experience was fluid without having to reinstall either OS.

.. note::

   I only run LLMs on Linux, and do not program anything on Windows. When I mention Windows, I just mean that the drivers were
   easy to install or were automatically installed by the OS, and games work well.

I wanted to install the following things:

- The Radeon Drivers from AMD
- Any tool to help me monitor the GPU's power draw since I only have a 750W PSU and didn't want to upgrade if I could avoid it.
- Ollama to help me run models and interact with them.

----------------------------------------
Installing AMD Drivers
----------------------------------------

This was easy. I had to follow this page and install `amdgpu_install` from the `.deb` file, which granted me a CLI to manage the drivers.
This was not clear on the AMD webpage, which is odd. Installing `amdgpu_install` *does not install the drivers*, it only gives you the installer to do so.
This is *sort of* similar to installing `rustup` or `rye` for Rust or Python respectively.

---------------------------------------------------------
`amdgpu_top`
---------------------------------------------------------

I needed a CLI to help monitor the GPU's power draw. I found `amdgpu_top` and `radeon_top`, but I went with the former since it's in Rust and I could install it with `cargo`.
Sadly they don't support `binstall`, so my machine had to compile it from scratch. This meant installing the dependencies as well. I might file a PR to 

