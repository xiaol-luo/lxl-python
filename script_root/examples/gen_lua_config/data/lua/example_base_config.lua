

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
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "234" 
        item.raw_val = a.b 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 3024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "2345" 
        item.raw_val = cd;ab 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 5024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "4456" 
        item.raw_val = abcd; 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 7024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "6567" 
        item.raw_val = 6567 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 9024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "8678" 
        item.raw_val = 8678 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 11024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "10789" 
        item.raw_val = 10789 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 13024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "12900" 
        item.raw_val = 12900 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 15024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "15011" 
        item.raw_val = 15011 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 17024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "17122" 
        item.raw_val = 17122 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 19024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "19233" 
        item.raw_val = 19233 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end
    do
        ---@type LogicConfigCurrency
        local item = {}
        table.insert(item_list, item) 
        item.config_id = 21024 
        item.float_val = false 
        item.int_vec = {}
        do
            item.int_vec[1] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[2] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[3] = "currency|1|100;currency|2|200;currency|3|300"
            item.int_vec[4] = ""
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
        item.vec_map = {}
        do
            local tb = {}
            item.vec_map[1] = tb
            tb["a"] = 2
            tb["b"] = 3
        end
        do
            local tb = {}
            item.vec_map[2] = tb
            tb["3"] = 1
            tb["c"] = 4
        end 
        item.str_val = "21344" 
        item.raw_val = 21344 
        item.int_raw_map_vec = {}
        do
            local tb = {}
            item.int_raw_map_vec[1] = tb
            tb[1] = 101|111
            tb[2] = 101
            tb[3] = 102
        end
        do
            local tb = {}
            item.int_raw_map_vec[2] = tb
            tb[1] = 201
            tb[2] = 202
            tb[3] = 203
        end
    end

    local item_map = {}
    for _, v in ipairs(item_list) do
        item_map[v.config_id] = v
    end
    return item_map, item_list
end

function _config_require_currency()
    return Logic_Config_Name.explore, get_config_map()
end