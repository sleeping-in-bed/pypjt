Quick Reference
===============

This page provides a quick overview of essential commands, configuration, and tips for experienced users.

**1.Start project**

.. code-block:: bash

   pypjt
   python -m pypjt

**2.Install dependencies**

.. code-block:: bash

   cd scripts
   ./install_dep

**3.Create remote repository**

Set ``Workflow permissions`` to ``Read and write permissions``

Set actions secrets ``PYPI_P``

**4.Set .env**

**5.Initialize Git**

.. code-block:: bash

   cd scripts
   ./git_init

**6.Publish to Pypi**

.. code-block:: bash

   # Commit using Conventional Commits
   git commit -m "feat: first commit"

   # Push to main to trigger release
   cd scripts
   ./push_to_github

Make sure:

- ``pyproject.toml`` contains author and email
- GitHub secret ``PYPI_P`` is set
