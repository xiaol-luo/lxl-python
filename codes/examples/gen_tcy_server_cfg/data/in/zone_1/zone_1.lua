
---@type Zone
local zone = Zone:new()
zone.name = Zone_Name.zone_1
zone.main_network = docker_net_map[Docker_Net_Name.net_zone_1]
zone.etcd_cluster = require("zone_1.zone_1_etcd_cluster")
zone.redis_cluster = require("zone_1.zone_1_redis_cluster")


return zone