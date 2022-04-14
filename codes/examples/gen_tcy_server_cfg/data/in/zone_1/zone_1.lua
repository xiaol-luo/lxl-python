
---@type Zone
local zone = {
    name = "zone_1",
    etcd_cluster = {}
}

local docker_net = docker_net_map[Docker_Net_Name.net_zone_1]

zone.name = "zone_1"
zone.etcd_cluster = EtcdServerCluster:new()
zone.etcd_cluster.server_list = {}
do
    ---@type EtcdServer
    local es = EtcdServer:new()
    table.insert(zone.etcd_cluster.server_list, es)
    es.name = "etcd_1"
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_net = docker_net
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.sub_ip = "dhcp"
    es.client_port = 2379
    es.peer_port = 2380
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine("etcd_db", es.name)
end
do
    ---@type EtcdServer
    local es = EtcdServer:new()
    table.insert(zone.etcd_cluster.server_list, es)
    es.name = "etcd_2"
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_net = docker_net
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.sub_ip = "dhcp"
    es.client_port = 2379
    es.peer_port = 2380
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine("etcd_db", es.name)
end
do
    ---@type EtcdServer
    local es = EtcdServer:new()
    table.insert(zone.etcd_cluster.server_list, es)
    es.name = "etcd_3"
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_net = docker_net
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.sub_ip = "dhcp"
    es.client_port = 2379
    es.peer_port = 2380
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine("etcd_db", es.name)
end


return zone