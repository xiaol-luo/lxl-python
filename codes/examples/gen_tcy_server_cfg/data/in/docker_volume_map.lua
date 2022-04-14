
Docker_Volume_Name = {}
Docker_Volume_Name.zone_1_code = "zone_1_code"
Docker_Volume_Name.zone_1_build = "zone_1_build"
Docker_Volume_Name.zone_1_data = "zone_1_data"

---@type table<string, DockerVolume>
docker_volume_map = {}
local tmp_list = {}
do
    ---@type DockerVolume
    local net = {}
    table.insert(tmp_list, net)
    net.name = Docker_Volume_Name.zone_1_code
    net.map_path = "/root/code"
end
do
    ---@type DockerVolume
    local net = {}
    table.insert(tmp_list, net)
    net.name = Docker_Volume_Name.zone_1_build
    net.map_path = "/root/build"
end
do
    ---@type DockerVolume
    local net = {}
    table.insert(tmp_list, net)
    net.name = Docker_Volume_Name.zone_1_data
    net.map_path = "/root/data"
end

for _, v in ipairs(tmp_list) do
    assert(not docker_volume_map[v.name])
    docker_volume_map[v.name] = v
end
