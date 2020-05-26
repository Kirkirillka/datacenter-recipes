$instance_name_prefix = "kub"
$vm_cpus = 2
$num_instances = 3
$os = "ubuntu1804"
$subnet = "192.168.30"
$network_plugin = "calico"
$inventory = "inventory/itpark_dev_lab"
$shared_folders = { 'temp/docker_rpms' => "/var/cache/yum/x86_64/7/docker-ce/packages" }
