
Machine_Name = {}
Machine_Name.ll = "ll"
Machine_Name.mm = "mm"

---@type table<string, Machine>
machine_map = {}

local tmp_list = {}

do
    ---@type Machine
    local elem = Machine:new()
    table.insert(tmp_list, elem)
    elem.name = Machine_Name.ll
    elem.ip = "119.91.239.128"
    elem.ssh_port = 22
    elem.ssh_user = "root"
    elem.private_key_file = "C:/Users/luoxiaolong/.ssh/keys/root/id_rsa"
    elem.ssh_pwd = "xiaolzz"
end

do
    ---@type elem
    local elem = Machine:new()
    table.insert(tmp_list, elem)
    elem.name = Machine_Name.mm
    elem.ip = "119.91.239.128"
    elem.ssh_port = 22
    elem.ssh_user = "root"
    elem.private_key_file = "C:/Users/luoxiaolong/.ssh/keys/root/id_rsa"
    elem.ssh_pwd = "xiaolzz"
end



for _, v in ipairs(tmp_list) do
    assert(not machine_map[v.name])
    machine_map[v.name] = v
end
