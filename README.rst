=============================================
BINF690: Numerical Methods for Bioinformatics
=============================================

This project contains programming assignments for numerical methods
for bioinformatics. It also provides resources for instantiating a
containerized development environment as well as automation for
installing and running the project.

None of the Docker or testing stuff was needed for this course, but
the threat was made that we would have to reuse this code later in our
academic careers, so I made an extra effort to make it maintainable.

**Important: Do not use these resources if you are currently taking
this course.**


Supported Platforms
===================

- Docker running on x86_64

This project was tested on Docker Desktop running on a Macbook Pro.

The Docker image is somewhat large, around 2G, mainly because it
includes LaTeX.


Files
=====

The "src/" directory contains Python source code.

The "doc/" directory contains a Sphinx document tree and ReStructured
Text source files used in generating the assignment workbook.

The "docker/" directory contains Docker resources and the "build.sh"
script used to build the container image for this project.

The root directory of this project includes project metadata files,
the "install.sh" script, and "setup.py" Python package metadata.


Setup and Installation
======================

1.  Build the container image::

        $ docker/build.sh $REPO $TAG

    This will build an image with the name "$REPO/binf690:$TAG". Both
    arguments are optional, and the repo name will default to the
    local username ("$USER"). This image is based off the publicly
    available Fedora image.

2.  Run the container::

        $ docker run --rm -it  -v ${PROJECT_ROOT}:/BINF690 myuser/binf690 bash

    When we run the container, we do so as an interactive session
    (hence the "-it" options). We also mount the project source code
    into the container (using "-v"). In this example, we also specify
    to automatically delete the container when finished ("--rm").

3.  From within the container, install the project::

        $ cd /BINF690
        $ ./install.sh

    This step creates a Python environment using Conda, installs any
    required software dependencies, and finally installs the project
    itself.

4.  Within the container, activate the Python environment::

        $ conda activate binf690

    This command activates the Python environment for use. It's
    required to be able to run the project files, run tests, or
    generate the report document. This step is only needed once per
    session.

    The environment may be deactivated using the command::

        $ deactivate


Testing
=======

From within a running environment (as described in the "Setup &
Installation" section), run::

    $ cd /BINF690
    $ pytest

This step will run Python doctests from both the "tests/" and "doc/"
directories.


Compiling the Assignment Workbook
=================================

From within a running environment (as described in the "Setup &
Installation" section), run::


    $ cd /BINF690/doc
    $ make latexpdf

This will run all assignments and produce a workbook containing their
results. The workbook can be found in "doc/build/latex/binf690.pdf"


Author and Copyright
====================

Alexander Smith

Copyright 2021
