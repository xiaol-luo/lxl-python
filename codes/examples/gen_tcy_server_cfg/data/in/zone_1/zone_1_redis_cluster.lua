
---@type Zone
local docker_net = docker_net_map[Docker_Net_Name.net_zone_1]
local zone_name = Zone_Name.zone_1

local redis_cluster = RedisServerCluster:new()
redis_cluster.replicas = 1
redis_cluster.pwd = zone_name
redis_cluster.server_list = {}

do
    ---@type RedisServer
    local es = RedisServer:new()
    table.insert(redis_cluster.server_list, es)
    es.name = string_concat(zone_name, "redis_1")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 6379
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "redis", es.name)
end
do
    ---@type RedisServer
    local es = RedisServer:new()
    table.insert(redis_cluster.server_list, es)
    es.name = string_concat(zone_name, "redis_2")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 6379
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "redis", es.name)
end
do
    ---@type RedisServer
    local es = RedisServer:new()
    table.insert(redis_cluster.server_list, es)
    es.name = string_concat(zone_name, "redis_3")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 6379
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "redis", es.name)
end
do
    ---@type RedisServer
    local es = RedisServer:new()
    table.insert(redis_cluster.server_list, es)
    es.name = string_concat(zone_name, "redis_4")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 6379
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "redis", es.name)
end
do
    ---@type RedisServer
    local es = RedisServer:new()
    table.insert(redis_cluster.server_list, es)
    es.name = string_concat(zone_name, "redis_5")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 6379
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "redis", es.name)
end
do
    ---@type RedisServer
    local es = RedisServer:new()
    table.insert(redis_cluster.server_list, es)
    es.name = string_concat(zone_name, "redis_6")
    es.image = Image_Name.lxl_debian
    es.locate_machine = machine_map[Machine_Name.ll]
    es.docker_ip = DockerNetUse:new()
    es.docker_ip.docker_net = docker_net
    es.docker_ip.ip_suffix = "dhcp"
    es.client_port = 6379
    es.db_path = DockerVolumeUse:new()
    es.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    es.db_path.relative_path = path_combine(zone_name, "redis", es.name)
end

return redis_cluster