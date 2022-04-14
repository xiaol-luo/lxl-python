
Machine_Name = {}
Machine_Name.ll = "ll"
Machine_Name.mm = "mm"

---@type table<string, Machine>
machine_map = {}

local tmp_list = {}

do
    ---@type Machine
    local machine = {}
    table.insert(tmp_list, machine)
    machine.name = Machine_Name.ll
end

do
    ---@type Machine
    local machine = {}
    table.insert(tmp_list, machine)
    machine.name = Machine_Name.mm
end



for _, v in ipairs(tmp_list) do
    assert(not machine_map[v.name])
    machine_map[v.name] = v
end
