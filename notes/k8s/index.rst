.. _notes-k8s:
=================================
Kubernetes
=================================

.. update:: Dec 30, 2021

   This section contains my notes on Kubernetes. As of this update, while I've
   gone through some resources and the `learnk8s.io <https://learnk8s.io>`_
   course on K8s, I haven't been able to use it at work. I'm going to work my
   way through the material from the course, which is *really*, **really**
   good, and also read :ref:`books-k8s-in-action`.


I've installed both `minikube <https://minikube.sigs.k8s.io/docs/>`_ and
`microk8s <https://microk8s.io/>`_ on my ThinkPad P14S, but for the sake of
these exercises, I plan on using microk8s. There's no reason, just that it's
configured and works. I also run `k3s <>`_ on my Raspberry Pi 4 cluster,
which I hope to better leverage after learning how to use k8s properly.

--------
Goals
--------

I'd like to chart out my learning goals. I'm also learning :ref:`notes-golang`
at the moment, so I'd like to be able to understand Kubernetes *deeply*, so
that I can perhaps meddle with its inner workings. That being said, my goals are:

1. Be able to run a CLI-based application on k8s.
2. Be able to run a HTTP API service on k8s.
3. Be able to run a HTTP API service on k8s which also speaks to Redis and RabbitMQ instances
   running on the cluster.
4. Work with namespaces.

   1. What are they for?
   2. How do I limit their resources?
   3. How do I manage access control?
   4. Is it possible to inter-communicate between resources?
5. Understand pods.

   1. What are pods?
   2. Does 1 pod == 1 container?
   3. Can I run multiple containers on the same pod?
   4. Do services running on separate pods share the same resource pool?
   5. Limit pod resources
6. What are Linux Namespaces?
7. Run an ETL job on k8s.
