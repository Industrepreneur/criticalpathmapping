# Commands required to setup, link and run containers
$setup = <<-SHELL
# Set proper hostname
echo "dev.mapping.criticalpathmapping.com" > /etc/hostname
/bin/hostname -F /etc/hostname

# Stop and remove all existing containers
containers=$(docker ps -a -q)
if [ -n "$containers" ]; then
  docker rm -f $containers
fi

# Build images from Dockerfiles
# docker build --no-cache -t dokku/devtools /app/docker/devtools
# docker build --no-cache -t dokku/postgres /app/docker/postgres
docker build --no-cache -t dokku/mapping /app/docker/factoryconcepts

# Run and link containers
docker run -d --name postgresql_single_container \
  -p 5432:5432 \
  postgres:9.4.1

# docker run -d --name app_devtools \
#   -v /app:/app \
#   dokku/devtools

docker run -d --name app_mapping \
  -p 8000:8000 \
  -v /app:/app \
  --link postgresql_single_container:postgres \
  dokku/mapping

# Sync database with latest changes
# docker exec -it app_mapping python3 manage.py migrate
SHELL


# Restart containers when VM is rebooted
$start = <<-SHELL
docker start postgresql_single_container
docker start app_mapping
# docker start app_devtools
SHELL


VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "pugetworks/boot2docker"
  config.vm.box_url = "https://www.dropbox.com/s/ccdxv7qdq7k9nlk/pugetworks-boot2docker-primed-virtualbox.box?dl=1"
  # config.vm.box_url = "file:///Users/robin/Dropbox/Shared/Vagrant/pugetworks-boot2docker-primed-virtualbox.box"
  config.vm.box_download_checksum = "758c04fc0da54ea00c8b6c3ba45dce3449a75ff4"
  config.vm.box_download_checksum_type = "sha1"
  config.vm.box_check_update = false

  # Virtualbox
  config.vm.provider "virtualbox" do |vm|
    vm.memory = 1356
    vm.cpus   = 2
  end

  # Disable guest updating in boot2docker
  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end

  # Hostname mapping
  if Vagrant.has_plugin?("vagrant-hostmanager")
    config.hostmanager.enabled     = true
    config.hostmanager.manage_host = true
  end


  config.vm.define "mapping.web.local", primary: true do |web|

    web.hostmanager.aliases = %w(dev.mapping.criticalpathmapping.com mapping.criticalpathmapping.com.local)

    # Create a private network for NFS shares
    web.vm.network "private_network", ip: "192.168.42.42"

    # Forward port 8000 to localhost:8000
    web.vm.network "forwarded_port", guest: 8000, host: 8000
    # web.vm.network "forwarded_port", guest: 5432, host: 5432

    # Share app folder with VM, using NFS for performance
    web.vm.synced_folder ".", "/app", type: "nfs"
    # web.vm.synced_folder ".", "/app"

    # Setup containers on VM initialization
    web.vm.provision "shell", inline: $setup

    # Restart containers on subsequent VM runs
    web.vm.provision "shell", run: "always", inline: $start

    # web.vm.post_up_message = "The web box is now up and running."

  end

config.vm.post_up_message = <<-EOS
Machine 'mapping.web.local' has a post `vagrant up` message. This is a message
------------------------------------------------------------------------------
--                                                                          --
--  All boxes successfully spun up!                                         --
--  This is line 2                                                          --
--                                                                          --
--  Then a space and line 3                                                 --
--                                                                          --
------------------------------------------------------------------------------
EOS

end
