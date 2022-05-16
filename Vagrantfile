# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # config.vm.box = "bento/ubuntu-16.04"
  # config.vm.box_version = "=2.2.9"
  config.vm.box = "ubuntu/focal64"
  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end
  config.vm.network "forwarded_port", guest: 8000, host: 8095
  config.vm.network "forwarded_port", guest: 80, host: 8096
  config.vm.provision "shell", path: "provision.sh"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
end
