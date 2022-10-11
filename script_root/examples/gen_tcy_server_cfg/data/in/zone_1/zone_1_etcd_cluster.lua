
---@type Zone
local docker_net = docker_net_map[Docker_Net_Name.net_zone_1]
local zone_name = Zone_Name.zone_1

local etcd_cluster = EtcdServerCluster:new()
etcd_cluster.cluster_token = zone_name
etcd_cluster.user = zone_name
etcd_cluster.pwd = zone_name
etcd_cluster.server_list = {}

do
    ---@type EtcdServer
    local item = EtcdServer:new()
    table.insert(etcd_cluster.server_list, item)
    item.name = string_concat(zone_name, "etcd_1")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.mm]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 2379
    item.peer_port = 2380
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "etcd", item.name)
end
do
    ---@type EtcdServer
    local item = EtcdServer:new()
    table.insert(etcd_cluster.server_list, item)
    item.name = string_concat(zone_name, "etcd_2")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 2379
    item.peer_port = 2380
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "etcd", item.name)
end
do
    ---@type EtcdServer
    local item = EtcdServer:new()
    table.insert(etcd_cluster.server_list, item)
    item.name = string_concat(zone_name, "etcd_3")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 2379
    item.peer_port = 2380
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "etcd", item.name)
end


return etcd_cluster