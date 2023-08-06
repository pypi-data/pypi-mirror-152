# 🤝 Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### 🐞 Report Bugs

Report bugs at https://github.com/demberto/tlhelp32/issues.

If you are reporting a bug, please include:

* 💻 Windows version.
* 🕵️‍♂️ Any details about your local setup that might be helpful in troubleshooting.
* 📃 Detailed steps to reproduce the bug.

### 🛠 Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with **bug** and
**help wanted** is open to whoever wants to implement it.

### 🚀 Implement Features

Look through the GitHub issues for features. Anything tagged with **help
wanted** and **enhancement** is open to whoever wants to implement it.

### 📜 Write Documentation

tlhelp32 could always use more documentation, whether as part of the official
docs, in docstrings, or even on the web in blog posts, articles, and such.

### 🖋 Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/demberto/tlhelp32/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `tlhelp32` for local development.

1. Fork the `tlhelp32` repo on GitHub.
2. Clone your fork locally

    ```
    $ git clone git@github.com:demberto/tlhelp32.git
    ```

    Navigate to the newly created folder:

    ```
    cd tlhelp32
    ```

3. Create a virtualenv (optional):

   ```
   python -m venv venv
   ```

   Activate it:

   ```
   ./venv/Scripts/activate
   ```

4. Install dependencies:

    ```
    $ python -m pip install -r requirements.txt
    ```

5. Create a branch for local development:

    ```
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

6. When you're done making changes, check that your changes pass the
   tests, including testing other Python versions, with tox:

    ```
    $ tox
    ```

7. Commit your changes and push your branch to GitHub:

    ```
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

8. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.6, 3.7, 3.8 and 3.9. Check
   https://github.com/demberto/tlhelp32/actions
   and make sure that the tests pass for all supported Python versions.

## Deploying

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in CHANGELOG.md).
Then run:

```
$ tbump version     # version is of the form major.minor.patch
$ git push
$ git push --tags
```
