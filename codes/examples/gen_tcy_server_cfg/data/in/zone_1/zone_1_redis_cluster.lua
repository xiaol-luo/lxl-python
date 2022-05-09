
---@type Zone
local docker_net = docker_net_map[Docker_Net_Name.net_zone_1]
local zone_name = Zone_Name.zone_1

local redis_cluster = RedisServerCluster:new()
redis_cluster.replicas = 1
redis_cluster.pwd = zone_name
redis_cluster.server_list = {}

do
    ---@type RedisServer
    local item = RedisServer:new()
    table.insert(redis_cluster.server_list, item)
    item.name = string_concat(zone_name, "redis_1")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 6379
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "redis", item.name)
end
do
    ---@type RedisServer
    local item = RedisServer:new()
    table.insert(redis_cluster.server_list, item)
    item.name = string_concat(zone_name, "redis_2")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 6379
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "redis", item.name)
end
do
    ---@type RedisServer
    local item = RedisServer:new()
    table.insert(redis_cluster.server_list, item)
    item.name = string_concat(zone_name, "redis_3")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 6379
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "redis", item.name)
end
do
    ---@type RedisServer
    local item = RedisServer:new()
    table.insert(redis_cluster.server_list, item)
    item.name = string_concat(zone_name, "redis_4")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 6379
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "redis", item.name)
end
do
    ---@type RedisServer
    local item = RedisServer:new()
    table.insert(redis_cluster.server_list, item)
    item.name = string_concat(zone_name, "redis_5")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 6379
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "redis", item.name)
end
do
    ---@type RedisServer
    local item = RedisServer:new()
    table.insert(redis_cluster.server_list, item)
    item.name = string_concat(zone_name, "redis_6")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 6379
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "redis", item.name)
end

return redis_cluster