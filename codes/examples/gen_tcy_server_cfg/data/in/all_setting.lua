require "setting_descript"
require "machine_map"
require "docker_net_map"
require "docker_volume_map"
require "utils"
require "json"

lua_json = require "json"

Zone_Name = {}
Zone_Name.zone_1 = "zone_1"

all_setting =
{
    machine_map = machine_map,
    docker_net_map = docker_net_map,
    docker_volume_map = docker_volume_map,
    zone_map = {
        [Zone_Name.zone_1] = require "zone_1/zone_1",
    },
}

all_setting_json = lua_json.encode(all_setting)


