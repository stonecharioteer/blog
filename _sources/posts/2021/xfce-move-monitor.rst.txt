:blogpost:true
:tags: linux, manjaro, xfce, x11
:category: Tech
:date: Sept 1, 2021

.. _xfce-move-monitor:

=================================================
Moving a Window to the Next Monitor on XFCE
=================================================
-------------------------------
Step 1 - Install ``yay``
-------------------------------

``yay`` `is a package manager for AUR. <https://github.com/Jguer/yay>`_
It's super useful when installing Arch packages in Manjaro.

From the Github README.md:

.. code-block:: bash

   sudo pacman -S --needed git base-devel
   git clone https://aur.archlinux.org/yay.git
   cd yay
   makepkg -si

-------------------------
Step 2 - Dependencies
-------------------------

The core dependencies for this to work are:

1. ``xdtool``
2. ``wmctrl``
3. ``xorg-xwinfo``

---------------------------------------------------------------
Step 3 - Clone ``move-to-next-monitor`` to a folder in your path
---------------------------------------------------------------

Personally, I prefer ``~/.local/bin``, but you can use ``/usr/bin``, or any
folder that's in your path.

.. code-block:: bash

   git clone https://github.com/jc00ke/move-to-next-monitor

Note that I'm maintaining a fork at ``stonecharioteer/move-to-next-monitor``. I
want to see if I can rewrite this to work natively.

Add execution permissions to this file.

.. code-block::

   chmod +x move-to-next-monitor


----------------------------------------------------------
Step 4 - Add Keyboard bindings to invoke this script
----------------------------------------------------------

Use your XFCE window manager tools to bind a keyboard shortcut to invoke this tool.
