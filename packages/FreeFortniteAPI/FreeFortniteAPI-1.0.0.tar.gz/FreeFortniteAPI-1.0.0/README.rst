FreeFortniteAPI
=============

.. image:: https://discord.com/api/guilds/881251978951397396/embed.png
    :target: https://discord.com/invite/pFUTyqqcUx
    :alt: Discord server invite

Easy to use FreeFortniteAPI module.


Installing
~~~~~~~~~~

**Python 3.5 or higher is required**


.. code:: sh
    
    pip install FreeFortniteAPI



Documentation
~~~~~~~~~~~~~

To get started we first need to import the api and initialize the client.

.. code:: py

    import FreeFortniteAPI

    api = FreeFortniteAPI.FortniteAPI


Aes
~~~

.. code:: py

    api.aes("build", "main key", "updated")


News
~~~~

.. code:: py
    api.news("image gif", "date", "hash")