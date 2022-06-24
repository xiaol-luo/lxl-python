
local Repl_Set_Name = {}
Repl_Set_Name.rs_cfg = "rs_cfg"
Repl_Set_Name.rs_db_1 = "rs_db_1"
Repl_Set_Name.rs_db_2 = "rs_db_2"
Repl_Set_Name.rs_db_3 = "rs_db_3"

local ReplSet_Name_Role_Map = {}
ReplSet_Name_Role_Map[Repl_Set_Name.rs_cfg] = Mongo_Repl_Set_Role.configsvr
ReplSet_Name_Role_Map[Repl_Set_Name.rs_db_1] = Mongo_Repl_Set_Role.shardsvr
ReplSet_Name_Role_Map[Repl_Set_Name.rs_db_2] = Mongo_Repl_Set_Role.shardsvr
ReplSet_Name_Role_Map[Repl_Set_Name.rs_db_3] = Mongo_Repl_Set_Role.shardsvr


---@type Zone
local docker_net = docker_net_map[Docker_Net_Name.net_zone_1]
local zone_name = Zone_Name.zone_1

---@type MongoServerCluster
local mongo_cluster = MongoServerCluster:new()
mongo_cluster.cluster_token = zone_name

do
    mongo_cluster.private_key_file_content = 
"seO+K0qiWBH6O4bzuv7q9AifmtGEDuFHBSQbcTGFj3+GNlbMFaeHzebG71dr0lNj\\\
s0RfNSb4Vn0Faif3xGDpzdFhRKno6l0hzqulr29Ew9xDdeQ8rMM+0UTBBbQyzYUS\\\
Vwz2ALXqVBt3URfOpas8v8vPbQUDlCcouRDiM+gJpGm3/Tg1QVVABTw1DAMyxrxd\\\
0GTOKI1lObImspW2IPaIHKEgomjYNFcZQKdE9/JAZIH9Uw1ICfZxNAmx6+qQJGpu\\\
Wnx9Qb6amghAf5LaunRisOiBJmoyfWz1N5Vt5iS7nPqyP69qv5NySmswPIbLMt+O\\\
xbYbD9voeDXfOtvATcsP4LUdTVv0KOTcHOqfiaZabW8RHR57lon3lQTnNh5IHd4k\\\
S+HSuv69pjGCj7tikYaMqarju1XAcy/1FqkZkj4adk3j2eQfx48cCM7Gyq0qOwzG\\\
MP0Yfm7FVX07qnyS+11jeGgCZftC33J6Jes2d1a2XKZsJ/dp86VJUZReJTUtdOr4\\\
+E8DBwMPx7JbYqVcQ8cP8wABtUhk6biaVAPbBUPalpjjQrVvUTNIPykGrD8DX9v+\\\
RBUibf8FTIhw9t1AAI6o1FcDXosVO+XPUZls4j/wclrXIzPWkM8uDfL4o3SeEafz\\\
s0tPOQh28XnpxZGM8e20BQoKZxXNEQHRL5dUTRO1NlIWfYIveJdPPpLkp/AR5g5B\\\
bMxsx+AICGqkjcaATsr3veyVV/vzwSZsreYu630aoflnE7UBu30fwnU5ZRiCTYqI\\\
FoQMsBeGmnH1Ahb0tg2Bt1gAU0cE9IgvijZxFwNCDNs+eqZrFSvBlgpeMpEfAC0B\\\
ZSnKxj1SkcjiCvImYbBq1QDEK2VYleMp7QPkgt20tk1SDW2IbHUQe1IqO/Emih1L\\\
926ec3jewds2NCRoSDn8D3WBJwa2rbqaAvt2uAmur1usq8c5CPcOxUgNahxXitbS\\\
cYn+h6iWGwuNkjFiNzML+Ny4CFeb"

end

do
    ---@type MongoUser
    mongo_cluster.root_user = {}
    mongo_cluster.root_user.name = "root"
    mongo_cluster.root_user.pwd = "xiaolzz"
    mongo_cluster.user_list = {}
    do
        ---@type MongoUser
        local user = {}
        table.insert(mongo_cluster.user_list, user)
        user.name = "lxl"
        user.pwd = "xiaolzz"
        ---@type MongoRole
        user.role = {}
        user.role.name = "readWriteAnyDatabase"
        user.role.db = "admin"
    end
end


mongo_cluster.mongodb_server_list = {}
mongo_cluster.mongos_server_list = {}

do
    ---@type MongoDbServer
    local item = MongoDbServer:new()
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_1")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_cfg
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_2")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_cfg
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_3")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_cfg
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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

------------------------------------------------------------------------------------------------------

do
    ---@type MongoDbServer
    local item = MongoDbServer:new()
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_11")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_1
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_12")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_1
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_13")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_1
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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

------------------------------------------------------------------------------------------------------

do
    ---@type MongoDbServer
    local item = MongoDbServer:new()
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_21")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_2
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_22")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_2
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_23")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_2
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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

------------------------------------------------------------------------------------------------------

do
    ---@type MongoDbServer
    local item = MongoDbServer:new()
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_31")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_3
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_32")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_3
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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
    table.insert(mongo_cluster.mongodb_server_list, item)
    item.name = string_concat(zone_name, "mongodb_33")
    item.image = Image_Name.lxl_debian
    item.locate_machine = machine_map[Machine_Name.ll]
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.client_port = 27017
    item.repl_set_name = Repl_Set_Name.rs_db_3
    item.repl_set_role = ReplSet_Name_Role_Map[item.repl_set_name]
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

------------------------------------------------------------------------------------------------------

do
        ---@type MongosServer
        local item = MongosServer:new()
        table.insert(mongo_cluster.mongos_server_list, item)
        item.name = string_concat(zone_name, "mongos_1")
        item.image = Image_Name.lxl_debian
        item.locate_machine = machine_map[Machine_Name.ll]
        item.docker_ip = DockerNetUse:new()
        item.docker_ip.docker_net = docker_net
        item.docker_ip.ip_suffix = "dhcp"
        item.client_port = 27017
        item.log_path = DockerVolumeUse:new()
        item.log_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.log_path.relative_path = path_combine(zone_name, "mongos", item.name, "log.txt")
        item.pid_file_path = DockerVolumeUse:new()
        item.pid_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.pid_file_path.relative_path = path_combine(zone_name, "mongos", item.name, "pid.txt")
        item.key_file_path = DockerVolumeUse:new()
        item.key_file_path.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.key_file_path.relative_path = path_combine(zone_name, "mongos", item.name, "id_key_file")
end

return mongo_cluster

--[[
    mongod --configsvr --replSet rs_cfg  --bind_ip 0.0.0.0 --port 27019 --dbpath /shared/tmp/mongodb/rs_cfg_1/db --logpath /shared/tmp/mongodb/rs_cfg_1/log.txt --keyFile /shared/tmp/mongodb/rs_cfg_1/key_file
]]