require "class"

-- fo figure out

---@class SettingBase
SettingBase = SettingBase or class("SettingBase")

function SettingBase:init_self()

end

function SettingBase:figure_out_fields()

end

---@class Machine
---@field name string
---@field ip string
---@field ssh_port
---@field ssh_user
---@field ssh_pwd
---@field private_key_file
Machine = Machine or class("Machine", SettingBase)

---@class DockerVolume
---@field name string
---@field map_path string
DockerVolume = DockerVolume or class("DockerVolume", SettingBase)

---@class DockerVolumeUse
---@field docker_volume DockerVolume
---@field relative_path string
---@field fo_abs_path string
DockerVolumeUse = DockerVolumeUse or class("DockerVolumeUse", SettingBase)

function DockerVolumeUse:figure_out_fields()
    self.fo_abs_path = path_combine(self.docker_volume.map_path, self.relative_path)
end

---@class LocalAndDockerVolumeUse
---@field volume_use DockerVolumeUse
---@field local_path string
LocalAndDockerVolumeUse = LocalAndDockerVolumeUse or class("LocalAndDockerVolumeUse", SettingBase)

function LocalAndDockerVolumeUse:figure_out_fields()
    self.volume_use:figure_out_fields()
end

---@class DockerNet
---@field name string
---@field subnet string
---@field fo_ip_prefix
---@field fo_ip_suffix_dhcp_max number
---@field fo_ip_suffix_dhcp_min number
---@field private _ip_dhcp_val number
DockerNet = DockerNet or class("DockerNet", SettingBase)

function DockerNet:ctor()
    self._ip_dhcp_val = nil
end

function DockerNet:init_self()
    local mask = nil
    self.fo_ip_prefix, mask = string.match(self.subnet, "(.*)%.%d+/(%d+)")
    print("DockerNet:init_self", self.fo_ip_prefix,mask)
    mask = tonumber(mask)
    assert(mask > 0 and mask < 32)
    local sub_ip_count = 2 ^ (32 - mask)
    self.fo_ip_suffix_dhcp_max = sub_ip_count - 1
    self.fo_ip_suffix_dhcp_min = math.ceil(sub_ip_count * 0.7)
    self._ip_dhcp_val = self.fo_ip_suffix_dhcp_min
end

function DockerNet:cal_ip(ip_suffix, is_apply)
    local ret = nil
    if "dhcp" == ip_suffix then
        ret = string.format("%s.%s", self.fo_ip_prefix, self._ip_dhcp_val)
        if is_apply then
            self._ip_dhcp_val = self._ip_dhcp_val + 1
        end
    else
        ret = string.format("%s.%s", self.fo_ip_prefix, ip_suffix)
    end
    print("DockerNet:cal_ip ", ret, ip_suffix, is_apply, self._ip_dhcp_val)
    return ret
end

---@class DockerNetUse
---@field docker_net DockerNet
---@field ip_suffix string
---@field fo_ip string
DockerNetUse = DockerNetUse or class("DockerNetUse", SettingBase)

function DockerNetUse:init_self()
    self.fo_ip = self.docker_net:cal_ip(self.ip_suffix, true)
end

---@class PortPublish
---@field docker_port
---@field machine_port
PortPublish = PortPublish or class("PortPublish", SettingBase)

---@class EtcdServer
---@field name string
---@field locate_machine Machine
---@field docker_ip DockerNetUse
---@field client_port number
---@field peer_port number
---@field db_path DockerVolumeUse
---@field image string
EtcdServer = EtcdServer or class("EtcdServer", SettingBase)

---@class EtcdServerCluster
---@field server_list table<number, EtcdServer>
---@field user string
---@field pwd string
---@field cluster_token string
---@field fo_initial_cluster string
---@field fo_end_points string
---@field fo_game_server_hosts string @给生成game_config.xml用
EtcdServerCluster = EtcdServerCluster or class("EtcdServerCluster", SettingBase)

function EtcdServerCluster:figure_out_fields()
    do
        local elems = {}
        local end_points = {}
        local game_server_hosts = {}
        for _, v in ipairs(self.server_list) do
            table.insert(elems, string.format("%s=http://%s:%s", v.name, v.docker_ip.fo_ip, v.peer_port))
            table.insert(end_points, string.format("//%s:%s", v.docker_ip.fo_ip, v.client_port))
            table.insert(game_server_hosts, string.format("http://%s:%s", v.docker_ip.fo_ip, v.peer_port))
        end
        self.fo_initial_cluster = table.concat(elems, ",")
        self.fo_end_points = table.concat(end_points, ",")
        self.fo_game_server_hosts = table.concat(game_server_hosts, ";")
    end
end

---@class RedisServer
---@field name string
---@field locate_machine Machine
---@field docker_ip DockerNetUse
---@field client_port number
---@field db_path DockerVolumeUse
---@field image string
RedisServer = RedisServer or class("RedisServer", SettingBase)

---@class RedisServerCluster
---@field replicas number
---@field pwd string
---@field server_list table<number, RedisServer>
---@field fo_cli_visit_ip string @提供给redis-cli访问
---@field fo_cli_visit_port string @提供给redis-cli访问
---@field fo_all_hosts string
---@field fo_comma_separate_all_hosts string
RedisServerCluster = RedisServerCluster or class("RedisServerCluster", SettingBase)

function RedisServerCluster:figure_out_fields()
    do
        local all_hosts = {}
        for _, v in ipairs(self.server_list) do
            table.insert(all_hosts, string.format("%s:%s", v.docker_ip.fo_ip, v.client_port))
            if not self.fo_cli_visit_ip then
                self.fo_cli_visit_ip = v.docker_ip.fo_ip
                self.fo_cli_visit_port = v.client_port
            end
        end
        self.fo_all_hosts = table.concat(all_hosts, " ")
        self.fo_comma_separate_all_hosts = table.concat(all_hosts, ",")
    end
end

---@class MongoDbServer
---@field name string
---@field image string
---@field locate_machine Machine
---@field docker_ip DockerNetUse
---@field client_port number
---@field repl_set_role string @ shardsvr or configsvr
---@field repl_set_name string
---@field log_path DockerVolumeUse
---@field db_path DockerVolumeUse
---@field pid_file_path DockerVolumeUse
---@field key_file_path DockerVolumeUse
MongoDbServer = MongoDbServer or class("MongoDbServer", SettingBase)

---@class MongosServer
---@field name string
---@field locate_machine Machine
---@field docker_ip DockerNetUse
---@field client_port number
---@field log_path DockerVolumeUse
---@field pid_file_path DockerVolumeUse
---@field key_file_path string
MongosServer = MongosServer or class("MongosServer", SettingBase)

---@class MongoRole
---@field name string
---@field db string
MongoRole = MongoRole or class("MongoRole", SettingBase)

---@class MongoUser
---@field name string
---@field pwd string
---@field role MongoRole
MongoUser = MongoUser or class("MongoUser", SettingBase)

---@class MongoReplSet
---@field name string
---@field repl_set_role string
---@field host_list string[]
---@field server_list MongoDbServer[]
---@field fo_host_list_str string
MongoReplSet = MongoReplSet or class("MongoReplSet", SettingBase)

---@class MongoServerCluster
---@field mongos_server_list table<number, MongosServer>
---@field mongodb_server_list table<number, MongoDbServer>
---@field private_key_file_content string @openssl rand -base64 741 可产生
---@field root_user MongoUser
---@field user_list table<number, MongoUser>
---@field fo_repl_set_map table<string, MongoReplSet>
---@field fo_cfg_repl_set MongoReplSet
MongoServerCluster = MongoServerCluster or class("MongoServerCluster", SettingBase)

function MongoServerCluster:figure_out_fields()
    do
        local repl_set_map = {}
        ---@param v MongoDbServer
        for _, v in pairs(self.mongodb_server_list) do
            local repl_set = repl_set_map[v.repl_set_name]
            if not repl_set then
                ---@type MongoReplSet
                repl_set = MongoReplSet:new()
                repl_set.name = v.repl_set_name
                repl_set_map[repl_set.name] = repl_set
                repl_set.repl_set_role = v.repl_set_role
                repl_set.host_list = {}
                repl_set.server_list = {}
            end
            assert(repl_set.repl_set_role == v.repl_set_role)
            table.insert(repl_set.host_list, string.format("%s:%s", v.docker_ip.fo_ip, v.client_port))
            table.insert(repl_set.server_list, v)
        end
        self.fo_repl_set_map = repl_set_map
        self.fo_cfg_repl_set = nil
        ---@param v MongoReplSet
        for _, v in pairs(repl_set_map) do
            if v.repl_set_role == Mongo_Repl_Set_Role.configsvr then
                assert(not self.fo_cfg_repl_set)
                self.fo_cfg_repl_set = v
            end
            v.fo_host_list_str = table.concat(v.host_list, ",")
        end
    end
end

---@class Zone
---@field name string
---@field mongo_cluster MongoServerCluster
---@field redis_cluster RedisServerCluster
---@field etcd_cluster EtcdServerCluster
---@field game_server_cluster GameServerCluster
---@field main_network DockerNet
---@field fo_used_network_map table<string, DockerNet> @不包含main_network
---@field fo_used_volume_map table<string, DockerVolume>
Zone = Zone or class("Zone", SettingBase)

---@return GameServer
function Zone:get_game_server(server_name)
    local ret = nil
    for _, v in ipairs(self.game_server_cluster.server_list) do
        if v.server_name == server_name then
            ret = v
            break
        end
    end
    return ret
end

function Zone:figure_out_fields()
    self.fo_used_network_map = {}
    self.fo_used_volume_map = {}
    travel_table(self, function(elem)
        if is_class_instance(elem, DockerNet) then
            if elem ~= self.main_network then
               self.fo_used_network_map[elem.name] = elem
            end
        end
        if is_class_instance(elem, DockerVolume) then
            self.fo_used_volume_map[elem.name] = elem
        end
    end)
    ---@param server GameServer
    for server_idx, server in ipairs(self.game_server_cluster.server_list) do
        do
            local remote_server_map = server.remote_server_map
            server.remote_server_map = {}
            for k, v in pairs(remote_server_map) do
                ---@type GameServer
                local other_server = self:get_game_server(v.ext_params)
                if other_server then
                    ---@type RemoteServer
                    local rs = {}
                    server.remote_server_map[k] = rs
                    rs.ip = other_server.docker_ip.fo_ip
                    if Regular_Replace_Flag.zone_game_server_http_ip then
                        rs.port = other_server.http_port
                    end
                    if Regular_Replace_Flag.zone_game_server_client_ip then
                        rs.port = other_server.client_port
                    end
                end
            end
        end
        do
            local etcd_cluster_map = server.etcd_cluster_map
            server.etcd_cluster_map = {}
            for k, v in pairs(etcd_cluster_map) do
                if Regular_Replace_Flag.zone_db_cluster == v.flag then
                   server.etcd_cluster_map[k] = self.etcd_cluster
                end
            end
        end
        do
            local redis_cluster_map = server.redis_cluster_map
            server.redis_cluster_map = {}
            for k, v in pairs(redis_cluster_map) do
                if Regular_Replace_Flag.zone_db_cluster == v.flag then
                   server.redis_cluster_map[k] = self.redis_cluster
                end
            end
        end
        do
            local mongo_cluster_map = server.mongo_cluster_map
            server.mongo_cluster_map = {}
            for k, v in pairs(mongo_cluster_map) do
                if Regular_Replace_Flag.zone_db_cluster == v.flag then
                   server.mongo_cluster_map[k] = self.mongo_cluster
                end
            end
        end
    end
end

---@class RemoteServer
---@field ip string
---@field port string
RemoteServer = RemoteServer or class("RemoteServer", SettingBase)

---@class GameServer
---@field server_role string
---@field server_name string
---@field locate_machine Machine
---@field image string
---@field docker_ip DockerNetUse
---@field client_port number
---@field peer_port number
---@field http_port number
---@field work_dir DockerVolumeUse
---@field config_file DockerVolumeUse
---@field remote_server_map table<string, RemoteServer>
---@field etcd_cluster_map table<string, EtcdServerCluster>
---@field redis_cluster_map table<string, RedisServerCluster>
---@field mongo_cluster_map table<string, MongoServerCluster>
GameServer = GameServer or class("GameServer", SettingBase)

---@class GameServerCluster
---@field server_list GameServer[]
GameServerCluster = GameServerCluster or class("GameServerCluster", SettingBase)


---@class Mongo_Repl_Set_Role
Mongo_Repl_Set_Role = {}
Mongo_Repl_Set_Role.configsvr = "configsvr"
Mongo_Repl_Set_Role.shardsvr = "shardsvr"


---@class Game_Server_Role
Game_Server_Role = {}
Game_Server_Role.platform = "platform"
Game_Server_Role.auth = "auth"
Game_Server_Role.login = "login"
Game_Server_Role.world = "world"
Game_Server_Role.game = "game"
Game_Server_Role.gate = "gate"
Game_Server_Role.match = "match"
Game_Server_Role.fight = "fight"
Game_Server_Role.room = "room"
Game_Server_Role.create_role = "create_role"
Game_Server_Role.world_sentinel = "world_sentinel"
Game_Server_Role.workbench = "workbench"
Game_Server_Role.message_hub = "message_hub"

---@class Regular_Replace_Flag
Regular_Replace_Flag = {}
Regular_Replace_Flag.zone_db_cluster = "zone_db_cluster"
Regular_Replace_Flag.zone_game_server_client_ip = "zone_game_server_client_ip"
Regular_Replace_Flag.zone_game_server_http_ip = "zone_game_server_http_ip"


