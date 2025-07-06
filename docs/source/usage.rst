Usage
=====

Now that the project template has been created, how do we use it?

Configure Environment Variables
-------------------------------

The first step is to configure the environment variables in the ``.env`` file:

- **GIT_NAME**: Your Git username, used for Git configuration.
- **GIT_EMAIL**: Your Git email address, used for Git configuration.
- **REMOTE_REPO**: The remote repository URL for this project.
- **REPO_USERNAME**: Your remote repository username, used for authentication.
- **REPO_TOKEN**: Your remote repository personal access token, used for authentication.

Install Dependencies
--------------------

After configuring these variables, run the ``install_dep`` script in the ``scripts`` directory:

.. code-block:: bash

   cd scripts
   ./install_dep

.. note::

   Make sure to run the script **from within the scripts directory**,
   not from the project root or any other directory.

This will install all dependencies required by the project, including the ``uv`` package manager,
Python packages (via pip), and JavaScript packages (via npm).

Initialize Git
--------------

Next, run the ``git_init`` script:

.. code-block:: bash

   cd scripts
   ./git_init

This script initializes a Git repository, sets the remote origin,
and installs Husky hooks. These hooks will perform two checks:

- A **pre-commit** check, as defined in ``.pre-commit-config.yaml``
- A **commit message lint** check, as defined in ``commitlint.config.mjs``

Before pushing to the GitHub remote repository for the first time,
you must update the GitHub Actions workflow permissions:

1. Go to your GitHub repository.
2. Navigate to:

   .. code-block::

      Settings -> Actions -> General -> Workflow permissions

3. Select **"Read and write permissions"**
4. Click **"Save"**

Once this is done, you can commit and push to the remote repository as usual.
Because the GitHub credentials are set in the ``.env`` file, you can use the ``push_to_github`` script
to push your repository to GitHub automatically.

Semantic Release
----------------

This project uses `semantic-release <https://github.com/semantic-release/semantic-release>`_
by default to automate versioning and changelog generation based on conventional commit messages.

Features of ``semantic-release`` include:

- Automatic versioning based on commit history
- Automatic changelog generation
- Publishing GitHub releases
- No need to manually bump version numbers

To trigger a release, simply merge a commit into the ``main`` branch that follows the
`Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ format.
``semantic-release`` will handle the rest via CI.

For configuration details, see the
`semantic-release documentation <https://semantic-release.gitbook.io/semantic-release/>`_.

Publishing to PyPI
------------------

You can configure ``PYPI_U`` and ``PYPI_P`` in the ``.env`` file,
then run the ``build_and_upload_to_pypi`` script to upload the package to PyPI.
However, this manual method is **not recommended**.

Instead, the recommended approach is to use automated publishing via CI:

1. **Set author information in ``pyproject.toml``**

   You must define the following fields in your ``pyproject.toml`` file:

   .. code-block:: toml

      [project]
      name = "your-package-name"
      version = "0.0.0"  # This field is managed by semantic-release
      description = "Your package description"
      authors = [
          { name = "Your Name", email = "your@email.com" }
      ]
      # ... other required metadata

   .. note::

      You do **not** need to manually update the ``version`` field.
      It is managed automatically by ``semantic-release``.

   .. warning::

      If the ``authors`` field is missing or incomplete (missing name or email),
      the PyPI publishing step will **fail during CI**.

2. **Configure the PyPI token**

   In your GitHub repository, navigate to:

   .. code-block::

      Settings -> Secrets and variables -> Actions -> New repository secret

   Create a new secret named **PYPI_P** and paste your PyPI API token as the value.
   You can generate the token from your PyPI account under:

   .. code-block::

      Account settings -> API tokens

3. **Trigger the release**

   Once the above steps are complete:

   - Make a commit that follows the Conventional Commits format.
   - Push or merge it into the ``main`` branch.

   This will trigger the GitHub Actions workflow, which will:

   - Let ``semantic-release`` determine the next version
   - Automatically update the changelog and create a Git tag
   - Publish the package to PyPI

Write the Documentation
-----------------------

This project uses ``Sphinx`` as the documentation generator.

You can run the following command to enable live documentation building and preview while editing:

.. code-block:: bash

   make livehtml

You can run the ``make_po`` script to generate translation template files (``.po`` files) for your documentation.

For more information on Sphinx internationalization (i18n),
refer to the `official Sphinx guide <https://www.sphinx-doc.org/en/master/usage/advanced/intl.html>`_.

.. code-block:: bash

   cd scripts/docs
   ./make_po  # Optional: specify languages with -l, e.g., -l zh_CN -l es

This project also supports documentation hosting via
`Read the Docs <https://about.readthedocs.com/>`_.
You can sign in and configure it to enable automatic documentation hosting and updates.

Codecov
-------

This project supports `Codecov <https://about.codecov.io/>`_, a popular code coverage reporting tool.

After running your test suite and generating coverage reports, the coverage data can be uploaded to Codecov as part of the CI/CD pipeline.

To enable Codecov integration:

1. Sign in to Codecov with your GitHub/GitLab account.
2. Add this repository to your Codecov dashboard.
3. Generate a Codecov token (optional for public repos).
4. In your CI environment (e.g., GitHub Actions), upload the coverage report using the official Codecov uploader.
5. Add a badge to your README to display the current coverage status.

The CI workflow is pre-configured to handle this integration automatically if the coverage report is generated and uploaded correctly.
