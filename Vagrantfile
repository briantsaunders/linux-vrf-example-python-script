# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  ####################
  ## Site 1 Router  ##
  ####################
  config.vm.define 'site1router' do |router|
    router.vm.box = 'briantsaunders/frrouting-stable-7.0'
    router.vm.hostname = 'site1router'
    router.vm.synced_folder '.',
      '/vagrant',
      disabled: false
    router.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan1',
      ip: '10.1.1.1',
      netmask: '255.255.255.0'
    router.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan2',
      ip: '10.1.2.1',
      netmask: '255.255.255.0'
    router.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan3',
      ip: '10.1.3.1',
      netmask: '255.255.255.0'
    router.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan4',
      ip: '10.1.4.1',
      netmask: '255.255.255.0'
    router.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "pb.conf.all.yml"
      ansible.groups = {
        "routers" => ["site1router"],
        "all:children" => ["routers"]
      }
    end
  end

  #####################
  ## Site 1 Server 1 ##
  #####################
  config.vm.define 'site1server1' do |server|
    server.vm.box = 'generic/ubuntu1804'
    server.vm.provider "virtualbox" do |settings|
      settings.cpus = 1
      settings.memory = 512
    end
    server.vm.hostname = 'site1server1'
    server.vm.synced_folder '.',
      '/vagrant',
      disabled: false
    server.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan1',
      ip: '10.1.1.10',
      netmask: '255.255.255.0'
    server.vm.provision "shell",
      run: "always",
      inline: "route add default gw 10.1.1.1"
  end

  #####################
  ## Site 1 Server 2 ##
  #####################
  config.vm.define 'site1server2' do |server|
    server.vm.box = 'generic/ubuntu1804'
    server.vm.provider "virtualbox" do |settings|
      settings.cpus = 1
      settings.memory = 512
    end
    server.vm.hostname = 'site1server2'
    server.vm.synced_folder '.',
      '/vagrant',
      disabled: false
    server.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan2',
      ip: '10.1.2.10',
      netmask: '255.255.255.0'
    server.vm.provision "shell",
      run: "always",
      inline: "route add default gw 10.1.2.1"
  end

  #####################
  ## Site 1 Server 3 ##
  #####################
  config.vm.define 'site1server3' do |server|
    server.vm.box = 'generic/ubuntu1804'
    server.vm.provider "virtualbox" do |settings|
      settings.cpus = 1
      settings.memory = 512
    end
    server.vm.hostname = 'site1server3'
    server.vm.synced_folder '.',
      '/vagrant',
      disabled: false
    server.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan3',
      ip: '10.1.3.10',
      netmask: '255.255.255.0'
    server.vm.provision "shell",
      run: "always",
      inline: "route add default gw 10.1.3.1"
  end

  #####################
  ## Site 1 Server 4 ##
  #####################
  config.vm.define 'site1server4' do |server|
    server.vm.box = 'generic/ubuntu1804'
    server.vm.provider "virtualbox" do |settings|
      settings.cpus = 1
      settings.memory = 512
    end
    server.vm.hostname = 'site1server4'
    server.vm.synced_folder '.',
      '/vagrant',
      disabled: false
    server.vm.network 'private_network',
      auto_config: true,
      nic_type: '82540EM',
      virtualbox__intnet: 'site1_lan4',
      ip: '10.1.4.10',
      netmask: '255.255.255.0'
    server.vm.provision "shell",
      run: "always",
      inline: "route add default gw 10.1.4.1"
  end

end