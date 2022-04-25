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
    print("DockerNet:cal_ip ", ip_suffix, is_apply, self._ip_dhcp_val)
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
---@field namesubprocess
---@field locate_machine Machine
---@field docker_net DockerNet
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
EtcdServerCluster = EtcdServerCluster or class("EtcdServerCluster", SettingBase)

function EtcdServerCluster:figure_out_fields()
    do
        local elems = {}
        for _, v in ipairs(self.server_list) do
            table.insert(elems, string.format("%s=http://%s:%s", v.name, v.docker_ip.fo_ip, v.peer_port))
        end
        self.fo_initial_cluster = table.concat(elems, ",")
    end
end

---@class RedisServer
---@field name
---@field locate_machine Machine
---@field docker_net DockerNet
---@field docker_ip DockerNetUse
---@field listen_port number
---@field db_dir string
---@field pwd string
RedisServer = RedisServer or class("RedisServer", SettingBase)

---@class RedisServerCluster
---@field replicas number
---@field pwd string
---@field server_list table<number, RedisServer>
RedisServerCluster = RedisServerCluster or class("RedisServerCluster", SettingBase)


---@class MongoDbServer
---@field name string
---@field locate_machine Machine
---@field docker_net DockerNet
---@field docker_ip string
---@field listen_port number
---@field cluster_role string @ shardsvr or configsvr
---@field repl_set_name string
---@field log_path string
---@field db_path string
---@field pid_file_path string
---@field id_key_file_path string
MongoDbServer = MongoDbServer or class("MongoDbServer", SettingBase)

---@class MongosServer
---@field name
---@field locate_machine Machine
---@field docker_net DockerNet
---@field docker_ip string
---@field listen_port number
---@field port_publish table<number, number>
---@field config_db_name string
---@field log_path string
---@field pid_file_path string
---@field config_db_hosts table<number, string>
---@field id_key_file_path string
MongosServer = MongosServer or class("MongosServer", SettingBase)

---@class MongoRole
---@field name string
---@field db string
MongoRole = MongoRole or class("MongoRole", SettingBase)

---@class MongoUser
---@field user string
---@field pwd string
---@field role_list table<number, MongoRole>
MongoUser = MongoUser or class("MongoUser", SettingBase)

---@class MongoDbServerCluster
---@field mongos_server_list table<number, MongosServer>
---@field config_server_list table<number, MongoDbServer>
---@field shard_server_list table<number, MongoDbServer>
---@field user_list table<number, MongoUser>
MongoDbServerCluster = MongoDbServerCluster or class("MongoDbServerCluster", SettingBase)

---@class Zone
---@field name
---@field mongo_cluster MongoDbServerCluster
---@field redis_cluster RedisServerCluster
---@field etcd_cluster EtcdServerCluster
---@field game_servers
---@field main_network DockerNet
---@field fo_used_network_map table<string, DockerNet> @不包含main_network
---@field fo_used_volume_map table<string, DockerVolume>
Zone = Zone or class("Zone", SettingBase)

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
end






