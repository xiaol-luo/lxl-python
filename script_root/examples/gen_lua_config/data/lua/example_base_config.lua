

---@return table<int, LogicConfigCurrency>
local function get_config_map ()
    local item_list = {}
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 1024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 6
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 6
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 203.0
        end 
        item.str_val = "234"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 3024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 7
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 7
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 204.0
        end 
        item.str_val = "2345"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 5024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 8
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 8
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 205.0
        end 
        item.str_val = "4456"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 7024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 9
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 9
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 206.0
        end 
        item.str_val = "6567"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 9024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 10
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 10
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 207.0
        end 
        item.str_val = "8678"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 11024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 11
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 11
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 208.0
        end 
        item.str_val = "10789"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 13024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 12
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 12
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 209.0
        end 
        item.str_val = "12900"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 15024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 13
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 13
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 210.0
        end 
        item.str_val = "15011"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 17024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 14
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 14
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 211.0
        end 
        item.str_val = "17122"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 19024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 15
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 15
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 212.0
        end 
        item.str_val = "19233"
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 21024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "1"
            item.int_vec[2] = "2"
            item.int_vec[3] = "3"
            item.int_vec[4] = "14;1223"
        end 
        item.int_int_map = {}
        do
            item.int_int_map["1"] = 2
            item.int_int_map["3"] = 4
            item.int_int_map["5"] = 16
        end 
        item.int_vec_vec = {}
        do
            local tb = {}
            item.int_vec_vec[1] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.int_vec_vec[2] = tb
            tb[1] = 4
            tb[2] = 5
            tb[3] = 16
        end 
        item.int_float_map_vec = {}
        do
            local tb = {}
            item.int_float_map_vec["1"] = tb
            tb[1] = 100.0
            tb[2] = 101.0
            tb[3] = 102.0
        end
        do
            local tb = {}
            item.int_float_map_vec["2"] = tb
            tb[1] = 201.0
            tb[2] = 202.0
            tb[3] = 213.0
        end 
        item.str_val = "21344"
    end
end

function _config_require_currency()
    return Logic_Config_Name.explore, get_config_map()
end