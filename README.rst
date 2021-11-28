============================
Stonecharioteer.com Blog
============================

This is the source code for my `blog. <https://stonecharioteer.com/>`_ I used
to use Jekyll before, but I abhor Markdown and don't consider it a worthwhile
format to type coding articles in. I've migrated the blog to use `ablog
<https://ablog.readthedocs.org>`_, which uses Sphinx underneath the hood. I'm
super happy with the way it allows
me to use RestructuredText.

-------
Setup
-------

Dependencies: you'll need Python 3 (install the latest, always), and nodejs
with npm installed (I recommend using nvm to manage your node versions).

.. code-block:: bash
   
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ablog build
   npm install -g live-server
   live-server docs

.. tip::

   I know it isn't the *best* idea, but I use Tmux with my blog, and I rely on
   `Tmuxinator <https://github.com/tmuxinator/tmuxinator>`_ to automatically
   run my blog setup. My config is in the ``.tmuxinator.yml`` file.

   In one pane, I run:

   .. code-block::
       
       fd . | entr sh -c 'env/bin/ablog build'

   `entr <https://github.com/eradman/entr>`_ is one of my favourite tools for
   setting up live builds on file changes.

   And in another, I run ``live-server docs/``


