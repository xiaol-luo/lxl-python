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

travel_table({all_setting, all_setting.machine_map, all_setting.docker_net_map, all_setting.docker_volume_map}, function(elem)
    if "function" == type(elem.init_self) then
        elem.init_self(elem)
    end
end)

travel_table({all_setting, all_setting.machine_map, all_setting.docker_net_map, all_setting.docker_volume_map}, function(elem)
    if "function" == type(elem.figure_out_fields) then
        elem.figure_out_fields(elem)
    end
end)

all_setting_json = lua_json.encode(all_setting)


