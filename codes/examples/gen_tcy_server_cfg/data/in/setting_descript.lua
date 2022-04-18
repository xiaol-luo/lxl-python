require "class"

---@class SettingBase
SettingBase = SettingBase or class("SettingBase")

function SettingBase:fill_fields()

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
DockerVolumeUse = DockerVolumeUse or class("DockerVolumeUse", SettingBase)

---@class DockerNet
---@field name string
---@field subnet string
DockerNet = DockerNet or class("DockerNet", SettingBase)

---@class DockerNetUse
---@field docker_net DockerNet
---@field sub_ip string
DockerNetUse = DockerNetUse or class("DockerNetUse", SettingBase)

---@class PortPublish
---@field docker_port
---@field machine_port
PortPublish = PortPublish or class("PortPublish", SettingBase)

---@class EtcdServer
---@field name
---@field locate_machine Machine
---@field docker_net DockerNet
---@field docker_ip DockerNetUse
---@field client_port number
---@field peer_port number
---@field db_path DockerVolumeUse
EtcdServer = EtcdServer or class("EtcdServer", SettingBase)


---@class EtcdServerCluster
---@field server_list table<number, EtcdServer>
EtcdServerCluster = EtcdServerCluster or class("EtcdServerCluster", SettingBase)

---@class RedisServer
---@field name
---@field locate_machine Machine
---@field docker_net DockerNet
---@field docker_ip string
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
Zone = Zone or class("Zone", SettingBase)





