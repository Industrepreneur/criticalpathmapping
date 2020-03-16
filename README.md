# Factory Concepts Mapping App.

## Development Setup - OSX & Windows

The following prerequisite tools are required:

- [Git](http://www.git-scm.com/)
- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)

You will also need to install a pre-seeded Vagrant box.  In order to save the hassle of downloading/installing docker images for Postgres, Python, and Node every time a new vagrant box is spun up I've created a Vagrant box pre-populated with Docker images.  The upshot is that once this is installed on your computer, any project derived from it will spin up, fully provisioned in under two minutes.

To download the vagrant box open a terminal (Git Bash on Windows) in the project directory and run:

$ _sh prepare-dev-server.sh_

## Development Commands

### Restart Docker containers

$ _fab dev app.restart_

$ _fab dev db.restart_

### Rebuild app image and launch new container

$ _fab dev app.rebuild_

### List environment variables for each container

$ _fab dev app.env_

$ _fab dev db.env_

### Launch bash shell within current instance of app container

$ _fab dev app.bash_

### Launch bash shell within a new instance of app container

$ _fab dev app.bash_

### Launch Python REPL with all models imported

$ _fab dev app.py.shell_

__OR__

$ _vagrant ssh -c "docker exec -it app_mapping python3 manage.py shell_plus"_

### Launch psql connection to database

$ _fab dev db.shell_

### Run Database Migrations

$ _fab dev app.py:migrate_

## Deployment Setup

Currently [Dokku-Alt](https://dokku-alt.github.io/) is being used to manage app deployment.  [Deis](http://deis.io/) or [Shipyard](http://shipyard-project.com/) may become preferred alternatives if the projects requirements expand to include server clustering.

### Prepare DigitalOcean Droplet

1. In a local terminal window, create a new SSH key for access control:

    $ _ssh-keygen -t rsa -b 4096 -f pugetworks@criticalpathmapping.com-id_rsa -C pugetworks@criticalpathmapping.com_

    When prompted for a password, you may elect to simply press enter twice to create a passwordless keyfile.

1. Copy the contents of the newly created __public__ keyfile to your clipboard:

    $ _pbcopy < criticalpathmapping.com-id_rsa.pub_

1. Paste keyfile into cloud-config file.

1. Make two backups of the two newly created files.  Without this you have no access to the server.  Also place a copy within the __.ssh__ folder in your user directory (__~/.ssh/__)

1. Log into the DigitalOcean admin interface and navigate to the __SSH Keys page__.

1. Select __Add SSH Key__, paste the contents of your clipboard into the Public SSH Key form field and click __Create SSH Key__.

1. Select __Create Droplet__, enter the domain name, select a size, and choose Ubuntu 14.04 x64.  ***ADD USER DATA*** At the bottom of the page select the SSH key that you just uploaded and click __Create Droplet__ at the bottom of the page.

1. On the homepage make note of the IP address for your newly created Droplet.

1. Locate and edit the ssh config file in your user directory (~/.ssh/config), adding the following:

  <pre>
  Host criticalpathmapping.com {alias}
    Hostname {IP Address}
    IdentityFile "~/.ssh/criticalpathmapping.com-id_rsa"
    RequestTTY yes
    User pugetworks
  </pre>

You now have a provisioned Dokku server ready to start deploying apps.  For a list of Dokku commands type:

    $ _ssh dokku@criticalpathmapping.com_

On OSX/Linux you may want to add the following function to your .zshenv, .bashrc, or wherever you like to put these things:

    dokku() { ssh -t dokku@$@; }

This will enable you to type:

$ _dokku criticalpathmapping.com {command}_

instead of:

$ _ssh dokku@criticalpathmapping.com {command}_


### Setup Deployment

1. First start by creating and configuring the main Docker image:

    $ _ssh dokku@criticalpathmapping.com create {app_name}_

    $ _ssh dokku@criticalpathmapping.com domains:set {app_name} criticalpathmapping.com_

    __OR__

    $ _dokku criticalpathmapping.com create {app_name}_

    $ _dokku criticalpathmapping.com domains:set {app_name} criticalpathmapping.com_


1. Create a database and link it to the application (if required):

    $ _dokku criticalpathmapping.com postgresql:create {db_name}_

    $ _dokku criticalpathmapping.com postgresql:link {app_name} {db_name}_

1. Configure git and deploy the app:

    $ _cd {project_dir}_

    $ _git remote add criticalpathmapping.com dokku@criticalpathmapping.com:{app_name}_

    $ _git push criticalpathmapping.com master_ &nbsp; __OR__ &nbsp; _git push criticalpathmapping.com {local_branch}:master_

1. Do the Django setup bits:

    $ _dokku enter {app_name}_

    % _python3 manage.py migrate_

    % exit

1. [Peanut butter jelly time!](https://www.youtube.com/watch?v=s8MDNFaGfT4)
