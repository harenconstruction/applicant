# Vagrant #

[Vagrant](https://www.vagrantup.com/) is used to create a reproducable development environment across different machines, with
consistent results.  Vagrant uses a configuration file, Vagrantfile, which should closely
match the production environment's operating system and required libraries.

To use vagrant to develop against the application, download and install it from [https://www.vagrantup.com/](https://www.vagrantup.com/)

## Running ##

If on Linux or OSX, you can:

  $ cd /path/to/project
  $ vagrant up

Or if you want to start and refresh from scratch:

  $ cd /path/to/project
  $ ./vagrant-refresh.sh
