
---@type Zone
local zone = Zone:new()
zone.name = Zone_Name.zone_1
zone.main_network = docker_net_map[Docker_Net_Name.net_zone_1]

local docker_net = zone.main_network
local zone_name = zone.name

zone.etcd_cluster = EtcdServerCluster:new()
zone.etcd_cluster.server_list = {}
do
    ---@type EtcdServer
    local es = EtcdServer:new()
    table.insert(zone.etcd_cluster.server_list, es)
    es.name = string_concat(zone_name, "etcd_1")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_net = docker_net
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 2379
    es.peer_port = 2380
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "etcd", es.name)
end
do
    ---@type EtcdServer
    local es = EtcdServer:new()
    table.insert(zone.etcd_cluster.server_list, es)
    es.name = string_concat(zone_name, "etcd_2")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_net = docker_net
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 2379
    es.peer_port = 2380
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "etcd", es.name)
end
do
    ---@type EtcdServer
    local es = EtcdServer:new()
    table.insert(zone.etcd_cluster.server_list, es)
    es.name = string_concat(zone_name, "etcd_3")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_net = docker_net
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 2379
    es.peer_port = 2380
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "etcd", es.name)
end


return zone