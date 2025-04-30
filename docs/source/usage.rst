Usage
=====

Now that we have created the project template, how do we use it?

Git
---

The first step is to configure some environment variables in the ``.env`` file:

- **GIT_NAME**: Your Git username, used for Git configuration.
- **GIT_EMAIL**: Your Git email address, used for Git configuration.
- **REMOTE_REPO**: The remote repository URL for this project.
- **GITHUB_USERNAME**: Your GitHub username, used for authentication.
- **GITHUB_TOKEN**: Your GitHub personal access token, used to push to GitHub.

After configuring these variables, run the ``git_init`` script located in the ``scripts`` directory:

.. code-block:: bash

   cd scripts
   ./git_init

.. note::

   Make sure to run the script **from the scripts directory**,
   not from the project root or any other directory.

This script initializes a Git repository, sets the remote origin,
and installs Husky hooks.

Before pushing to the GitHub remote repository for the first time,
you need to change the GitHub workflow permissions:

1. Go to your GitHub repository.
2. Navigate to:

   .. code-block::

      Settings -> Actions -> General -> Workflow permissions

3. Select **"Read and write permissions"**.
4. Click **"Save"**.

Once this is done, you can commit and push to the remote repository as usual.

Semantic Release
----------------

This project uses `semantic-release <https://github.com/semantic-release/semantic-release>`_
by default to automate version management and
changelog generation based on conventional commit messages.

Features of ``semantic-release`` include:

- Automatic versioning based on commit history
- Automatic changelog generation
- GitHub releases publishing
- No need to manually bump versions

To trigger a release, simply merge a commit into the ``main`` branch that follows the
`Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ format.
``semantic-release`` will handle the rest in CI.

For configuration details, see the
`semantic-release documentation <https://semantic-release.gitbook.io/semantic-release/>`_.

Publishing to PyPI
------------------

This project also supports automated publishing to `PyPI <https://pypi.org>`_.

To enable this functionality, follow these steps:

1. **Set author information in ``pyproject.toml``**

   You must define the following fields in your ``pyproject.toml`` file:

   .. code-block:: toml

      [project]
      name = "your-package-name"
      version = "0.0.0"  # This field will be managed by semantic-release
      description = "Your package description"
      authors = [
          { name = "Your Name", email = "your@email.com" }
      ]
      # ... other required metadata

   .. note::

      You do **not** need to manually change the ``version`` field.
      It's managed automatically by ``semantic-release``.

   .. warning::

      If the ``authors`` field is missing or incomplete (either name or email),
      the PyPI publishing step will **fail during CI**.

2. **Configure the PyPI token**

   In your GitHub repository, navigate to:

   .. code-block::

      Settings -> Secrets and variables -> Actions ->
      New repository secret

   Create a new secret named **PYPI_P** and paste your PyPI API token as its value.
   You can generate this token in your PyPI account under:

   .. code-block::

      Account settings -> API tokens

3. **Trigger the release**

   Once the above steps are complete:

   - Make a commit that follows the Conventional Commits convention.
   - Push or merge it into the ``main`` branch.

   This will trigger the GitHub Actions workflow, which will:

   - Let ``semantic-release`` determine the next version.
   - Automatically update the changelog and create a Git tag.
   - Publish the package to PyPI.
