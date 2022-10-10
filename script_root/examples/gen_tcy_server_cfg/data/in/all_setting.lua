require "setting_descript"
require "machine_map"
require "docker_net_map"
require "docker_volume_map"
require "utils"
require "json"
require "image_map"

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

local sort_way = require("zone_1/zone_1_sorted_uuid")

local sorted_setting = sort_way.sort_fn(all_setting, sort_way.sorted_uuid)

for _, elem in ipairs(sorted_setting) do
    if elem.get_uuid then
        local st_uuid = elem:get_uuid()
        if st_uuid then
           print(string.format("\"%s\",", st_uuid))
        end
    end
end

for _, elem in ipairs(sorted_setting) do
    if "function" == type(elem.init_self) then
        elem.init_self(elem)
    end
end

for _, elem in ipairs(sorted_setting) do
    if "function" == type(elem.figure_out_fields) then
        elem.figure_out_fields(elem)
    end
end

all_setting_json = lua_json.encode(all_setting)


