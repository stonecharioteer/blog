---
title: K3S on the 8GB Raspberry Pi 4 with Docker-CE
categories: [raspberry-pi, kubernetes, homelab]
---

I finally managed to fix the issue I was having with K3S on the Raspberry Pi 4.
Turns out, there is an issue with how Docker does IP configurations.

Long story short, here are a few github issues you should look at if you want
to dig in.

1. [Networking Issues on Raspbian](https://github.com/rancher/k3s/issues/703)
2. [kube-proxy currently incompatible with `iptables >= 1.8`](https://github.com/kubernetes/kubernetes/issues/71305)
3. [prometheus operator fails to start](https://github.com/carlosedp/cluster-monitoring/issues/74)

Finally, following **carlosedp's** [github repo on cluster-monitoring](https://github.com/carlosedp/) worked,
and my Raspberry Pi Bramble is up and running. Now, onto do *something* with it.
I am not sure what!
