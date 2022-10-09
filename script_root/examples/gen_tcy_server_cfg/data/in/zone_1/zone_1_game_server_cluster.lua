
---@type Zone
local docker_net = docker_net_map[Docker_Net_Name.net_zone_1]
local zone_name = Zone_Name.zone_1
local game_server_dir = "game_server"
local lus_script_dir = "tanchiyu/server/lua_script"
local datas_dir = "tanchiyu/server/datas"
local server_bin_name = "service"

local game_server_cluster = GameServerCluster:new()
game_server_cluster.server_list = {}

do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.platform
    item.server_name = string_concat(zone_name, "platform")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "10"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = 41101
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = 41102
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
    do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
    do
        item.mongo_cluster_map["platform"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
end

do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.auth
    item.server_name = string_concat(zone_name, "auth")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "12"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = 41201
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = 41202
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    do
        item.remote_server_map["platform_http"] = { flag=Regular_Replace_Flag.zone_game_server_http_ip, ext_params=string_concat(zone_name, "platform") }
    end
    item.etcd_cluster_map = {}
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
    do
        item.mongo_cluster_map["auth"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
        item.mongo_cluster_map["uuid"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
end

do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.login
    item.server_name = string_concat(zone_name, "login_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "20"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = 41301
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = 41302
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    do
        item.remote_server_map["auth_http"] = { flag=Regular_Replace_Flag.zone_game_server_http_ip, ext_params=string_concat(zone_name, "auth") }
    end
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
    do
        item.mongo_cluster_map["login"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.create_role
    item.server_name = string_concat(zone_name, "create_role_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
    do
        item.mongo_cluster_map["game"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
        item.mongo_cluster_map["uuid"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.world
    item.server_name = string_concat(zone_name, "world_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    do
        item.redis_cluster_map["online_servers"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.mongo_cluster_map = {}
    do
        item.mongo_cluster_map["game"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.world
    item.server_name = string_concat(zone_name, "world_1")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    do
        item.redis_cluster_map["online_servers"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.mongo_cluster_map = {}
    do
        item.mongo_cluster_map["game"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.game
    item.server_name = string_concat(zone_name, "game_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    do
        item.redis_cluster_map["online_servers"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.mongo_cluster_map = {}
    do
        item.mongo_cluster_map["game"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.gate
    item.server_name = string_concat(zone_name, "gate_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "30"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = 41401
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = 41402
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    do
        item.redis_cluster_map["online_servers"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.mongo_cluster_map = {}
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.match
    item.server_name = string_concat(zone_name, "match_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
end

do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.room
    item.server_name = string_concat(zone_name, "room_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
end

do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.fight
    item.server_name = string_concat(zone_name, "fight_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = 41501
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = 41502
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.world_sentinel
    item.server_name = string_concat(zone_name, "world_sentinel_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    do
        item.redis_cluster_map["online_servers"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.mongo_cluster_map = {}
end

do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.workbench
    item.server_name = string_concat(zone_name, "workbench_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "40"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = 41603
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    do
        item.remote_server_map["platform_http"] = { flag=Regular_Replace_Flag.zone_game_server_http_ip, ext_params=string_concat(zone_name, "platform") }
    end
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
end


do
    ---@type GameServer
    local item = GameServer:new()
    table.insert(game_server_cluster.server_list, item)
    item.server_role = Game_Server_Role.message_hub
    item.server_name = string_concat(zone_name, "message_hub_0")
    item.locate_machine = machine_map[Machine_Name.ll]
    item.image = Image_Name.lxl_debian
    item.docker_ip = DockerNetUse:new()
    item.docker_ip.docker_net = docker_net
    item.docker_ip.ip_suffix = "dhcp"
    item.peer_port = 10002
    do
        ---@type DockerNetMachinePort
        item.client_net_add = DockerNetMachinePort:new()
        item.client_net_add.machine = item.locate_machine
        item.client_net_add.docker_ip = item.docker_ip
        item.client_net_add.docker_port = 10001
        item.client_net_add.machine_port = nil
    end
    do
        ---@type DockerNetMachinePort
        item.http_net_add = DockerNetMachinePort:new()
        item.http_net_add.machine = item.locate_machine
        item.http_net_add.docker_ip = item.docker_ip
        item.http_net_add.docker_port = 10003
        item.http_net_add.machine_port = nil
    end
    do
        item.work_dir = DockerVolumeUse:new()
        item.work_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.work_dir.relative_path = path_combine(zone_name, game_server_dir, item.server_name)
    end
    do
        item.config_file = DockerVolumeUse:new()
        item.config_file.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.config_file.relative_path = path_combine(zone_name, game_server_dir, item.server_name, "game_config.xml")
    end
    do
        item.server_bin = DockerVolumeUse:new()
        item.server_bin.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_build]
        item.server_bin.relative_path = path_combine(server_bin_name)
    end
    do
        item.lua_script_dir = DockerVolumeUse:new()
        item.lua_script_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.lua_script_dir.relative_path = path_combine(lus_script_dir)
    end
	do
        item.data_dir = DockerVolumeUse:new()
        item.data_dir.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_code]
        item.data_dir.relative_path = path_combine(datas_dir)
    end
	item.remote_server_map = {}
    item.etcd_cluster_map = {}
    do
        item.etcd_cluster_map["service_discovery"] = { flag=Regular_Replace_Flag.zone_db_cluster, ext_params=nil }
    end
    item.redis_cluster_map = {}
    item.mongo_cluster_map = {}
end

return game_server_cluster