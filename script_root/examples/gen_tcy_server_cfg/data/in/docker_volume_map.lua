
Docker_Volume_Name = {}
Docker_Volume_Name.zone_1_code = "tcy_code"
Docker_Volume_Name.zone_1_build = "tcy_build"
Docker_Volume_Name.zone_1_data = "tcy_zone"

---@type table<string, DockerVolume>
docker_volume_map = {}
local tmp_list = {}
do
    ---@type DockerVolume
    local elem = {}
    table.insert(tmp_list, elem)
    elem.name = Docker_Volume_Name.zone_1_code
    elem.map_path = "/root/code"
end
do
    ---@type DockerVolume
    local elem = DockerVolume:new()
    table.insert(tmp_list, elem)
    elem.name = Docker_Volume_Name.zone_1_build
    elem.map_path = "/root/build"
end
do
    ---@type DockerVolume
    local elem = DockerVolume:new()
    table.insert(tmp_list, elem)
    elem.name = Docker_Volume_Name.zone_1_data
    elem.map_path = "/root/zone"
end

for _, v in ipairs(tmp_list) do
    assert(not docker_volume_map[v.name])
    docker_volume_map[v.name] = v
end
