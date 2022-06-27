
---@type Zone
local zone = Zone:new()
zone.name = Zone_Name.zone_1
zone.main_network = docker_net_map[Docker_Net_Name.net_zone_1]
zone.etcd_cluster = require("zone_1.zone_1_etcd_cluster")
zone.redis_cluster = require("zone_1.zone_1_redis_cluster")
zone.mongo_cluster = require("zone_1.zone_1_mongo_cluster")
zone.game_server_cluster = require("zone_1.zone_1_game_server_cluster")

do
    ---@type LocalAndDockerVolumeUse[]
    zone.test_to_docker_file_list = {}
    do
        ---@type LocalAndDockerVolumeUse
        local item = {}
        table.insert(zone.test_to_docker_file_list, item)
        item.local_path = "E:/diff.txt"
        item.volume_use = DockerVolumeUse:new()
        item.volume_use.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.volume_use.relative_path = path_combine("test", "diff.txt")
    end
    do
        ---@type LocalAndDockerVolumeUse
        local item = {}
        table.insert(zone.test_to_docker_file_list, item)
        item.local_path = "E:/diff.txt"
        item.volume_use = DockerVolumeUse:new()
        item.volume_use.docker_volume = docker_volume_map[Docker_Volume_Name.zone_1_data]
        item.volume_use.relative_path = path_combine("test", "diff2.txt")
    end
end


return zone