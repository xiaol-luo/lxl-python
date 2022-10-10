
Docker_Net_Name = {}
Docker_Net_Name.net_zone_1 = "my-network"

---@type table<string, DockerNet>
docker_net_map = {}
local tmp_list = {}
do
    ---@type DockerNet
    local net = DockerNet:new()
    table.insert(tmp_list, net)
    net.name = Docker_Net_Name.net_zone_1
    net.subnet = "10.0.1.1/24"
end

for _, v in ipairs(tmp_list) do
    assert(not docker_net_map[v.name])
    docker_net_map[v.name] = v
    v:init_self()
end
