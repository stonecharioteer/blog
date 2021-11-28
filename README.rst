============================
Stonecharioteer.com Blog
============================

This is the source code for my blog. I used to use Jekyll before, but I abhor
Markdown and don't consider it a worthwhile format to type coding
articles in. I've migrated the blog to use `ablog <>`_, which uses Sphinx underneath
the hood. I'm super happy with the way it allows me to use RestructuredText.

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

