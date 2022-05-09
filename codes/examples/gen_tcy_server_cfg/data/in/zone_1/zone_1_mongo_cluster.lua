
local Repl_Set_Name = {}
Repl_Set_Name.rs_cfg = "rs_cfg"
Repl_Set_Name.rs_db_1 = "rs_db_1"
Repl_Set_Name.rs_db_2 = "rs_db_2"
Repl_Set_Name.rs_db_3 = "rs_db_3"

local ReplSet_Name_Role_Map = {}
ReplSet_Name_Role_Map[Repl_Set_Name.rs_cfg] = "configsvr"
ReplSet_Name_Role_Map[Repl_Set_Name.rs_db_1] = "shardsvr"
ReplSet_Name_Role_Map[Repl_Set_Name.rs_db_2] = "shardsvr"
ReplSet_Name_Role_Map[Repl_Set_Name.rs_db_3] = "shardsvr"


---@type Zone
local docker_net = docker_net_map[Docker_Net_Name.net_zone_1]
local zone_name = Zone_Name.zone_1

local mongo_cluster = MongoServerCluster:new()
mongo_cluster.cluster_token = zone_name
mongo_cluster.user = zone_name
mongo_cluster.pwd = zone_name
mongo_cluster.shard_server_list = {}

do
    ---@type MongoDbServer
    local item = MongoDbServer:new()
    table.insert(mongo_cluster.shard_server_list, item)
    item.name = string_concat(zone_name, "mongodb_1")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_cfg
    item.cluster_role = ReplSet_Name_Role_Map[item.repl_set_name]
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "mongodb", item.name, "db")
    item.log_path = DockerVolumeUse:new()
    item.log_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.log_path.relative_path = path_combine(zone_name, "mongodb", item.name, "log.txt")
    item.pid_file_path = DockerVolumeUse:new()
    item.pid_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.pid_file_path.relative_path = path_combine(zone_name, "mongodb", item.name, "pid.txt")
    item.key_file_path = DockerVolumeUse:new()
    item.key_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.key_file_path.relative_path = path_combine(zone_name, "mongodb", item.name, "id_key_file")
end
do
    ---@type MongoDbServer
    local item = MongoDbServer:new()
    table.insert(mongo_cluster.shard_server_list, item)
    item.name = string_concat(zone_name, "mongodb_2")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_cfg
    item.cluster_role = ReplSet_Name_Role_Map[item.repl_set_name]
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "mongodb", item.name, "db")
    item.log_path = DockerVolumeUse:new()
    item.log_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.log_path.relative_path = path_combine(zone_name, "mongodb", item.name, "log.txt")
    item.pid_file_path = DockerVolumeUse:new()
    item.pid_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.pid_file_path.relative_path = path_combine(zone_name, "mongodb", item.name, "pid.txt")
    item.key_file_path = DockerVolumeUse:new()
    item.key_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.key_file_path.relative_path = path_combine(zone_name, "mongodb", item.name, "id_key_file")
end
do
    ---@type MongoDbServer
    local item = MongoDbServer:new()
    table.insert(mongo_cluster.shard_server_list, item)
    item.name = string_concat(zone_name, "mongodb_3")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_cfg
    item.cluster_role = ReplSet_Name_Role_Map[item.repl_set_name]
    item.db_path = DockerVolumeUse:new()
    item.db_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.db_path.relative_path = path_combine(zone_name, "mongodb", item.name, "db")
    item.log_path = DockerVolumeUse:new()
    item.log_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.log_path.relative_path = path_combine(zone_name, "mongodb", item.name, "log.txt")
    item.pid_file_path = DockerVolumeUse:new()
    item.pid_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.pid_file_path.relative_path = path_combine(zone_name, "mongodb", item.name, "pid.txt")
    item.key_file_path = DockerVolumeUse:new()
    item.key_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
    item.key_file_path.relative_path = path_combine(zone_name, "mongodb", item.name, "id_key_file")
end


return mongo_cluster

--[[
    mongod --configsvr --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27019 --dbpath /shared/tmp/mongodb/rs_cfg_1/db --logpath /shared/tmp/mongodb/rs_cfg_1/log.txt --keyFile /shared/tmp/mongodb/rs_cfg_1/key_file
]]