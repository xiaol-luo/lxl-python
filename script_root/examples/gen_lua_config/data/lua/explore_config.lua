
 

---@class LogicConfigExplore_
---@field config_id
---@field theme_name
---@field config_name
---@field descript
---@field first_reward_id
---@field reward_id
---@field background
---@field level_factor
---@field scene_width
---@field scene_height
---@field role_fish_id
---@field phase_effect_role_fish_size_list
---@field phase_appear_fish_group
---@field lv1_fish_num_min
---@field lv1_fish_num_max
---@field lv1_fish_ids
---@field lv1_group_density
---@field lv2_fish_num_min
---@field lv2_fish_num_max
---@field lv2_fish_ids
---@field lv2_group_density
---@field lv3_fish_num_min
---@field lv3_fish_num_max
---@field lv3_fish_ids
---@field lv3_group_density
---@field ai_group_num
---@field ai_fish_smart_factor
---@field ai_fish_ids
---@field common_fish_cruise_path
---@field ai_fish_cruise_path
local LogicConfigExplore = {}
 

---@return table<string, LogicConfigExplore_>
local function get_config_map ()
    local item_list = {}
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1000" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 1" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.1 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 32 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 2 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 1 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1001" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 2" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.2 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 33 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 6 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 2 
        item.ai_fish_smart_factor = 2 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1002" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 3" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.3 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 34 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 4 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 3 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1003" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 4" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.4 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 35 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 4 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1004" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 5" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.5 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 36 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 5 
        item.ai_fish_smart_factor = 5 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1005" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 6" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.6 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 37 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 5 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 6 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1006" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 7" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.7 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 38 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 7 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1007" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 8" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.8 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 39 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 2 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 8 
        item.ai_fish_smart_factor = 5 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1008" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 9" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 1.9 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 9 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 9 
        item.ai_fish_smart_factor = 2 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "1009" 
        item.theme_name = "pool" 
        item.config_name = "pool.level 10" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.0 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 10 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 10 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2000" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 1" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.1 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 11 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 1 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2001" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 2" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.2 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 12 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 11
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 11
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 11
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 2 
        item.ai_fish_smart_factor = 2 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 11
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2002" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 3" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.3 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 13 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 5 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 12
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 12
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 12
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 3 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 12
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2003" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 4" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.4 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 14 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 13
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 13
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 13
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 4 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 13
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2004" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 5" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.5 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 15 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 5 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 14
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 14
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 14
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 5 
        item.ai_fish_smart_factor = 5 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 14
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2005" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 6" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.6 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 16 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 15
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 15
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 15
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 6 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 15
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2006" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 7" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.7 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 17 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 16
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 16
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 16
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 7 
        item.ai_fish_smart_factor = 4 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 16
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2007" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 8" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.8 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 18 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 6 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 17
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 17
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 17
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 8 
        item.ai_fish_smart_factor = 4 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 17
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2008" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 9" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 2.9 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 19 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 6 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 9 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2009" 
        item.theme_name = "brook" 
        item.config_name = "brook.level 10" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.0 
        item.scene_width = 90.0 
        item.scene_height = 22.0 
        item.role_fish_id = 20 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 4 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 10 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2010" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 1" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.1 
        item.scene_width = 1042.0 
        item.scene_height = 1045.0 
        item.role_fish_id = 21 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 2 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 1 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2011" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 2" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.2 
        item.scene_width = 1088.0 
        item.scene_height = 999.0 
        item.role_fish_id = 22 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 6 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 2 
        item.ai_fish_smart_factor = 2 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2012" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 3" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.3 
        item.scene_width = 1029.0 
        item.scene_height = 1098.0 
        item.role_fish_id = 23 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 4 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 3 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2013" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 4" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.4 
        item.scene_width = 1007.0 
        item.scene_height = 1240.0 
        item.role_fish_id = 24 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 4 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2014" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 5" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.5 
        item.scene_width = 1164.0 
        item.scene_height = 1052.0 
        item.role_fish_id = 25 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 5 
        item.ai_fish_smart_factor = 5 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2015" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 6" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.6 
        item.scene_width = 1234.0 
        item.scene_height = 1101.0 
        item.role_fish_id = 26 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 5 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 6 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2016" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 7" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.7 
        item.scene_width = 988.0 
        item.scene_height = 1068.0 
        item.role_fish_id = 27 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 7 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2017" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 8" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.8 
        item.scene_width = 1478.0 
        item.scene_height = 1068.0 
        item.role_fish_id = 28 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 2 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 8 
        item.ai_fish_smart_factor = 5 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2018" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 9" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 3.9 
        item.scene_width = 1231.0 
        item.scene_height = 1058.0 
        item.role_fish_id = 29 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 9 
        item.ai_fish_smart_factor = 2 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2019" 
        item.theme_name = "theme_3" 
        item.config_name = "brook.level 10" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.0 
        item.scene_width = 1389.0 
        item.scene_height = 1537.0 
        item.role_fish_id = 30 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 10 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.common_fish_cruise_path[19] = tb
            tb[1] = 0
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = -40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = -30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = -20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = -10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 0
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 10
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 20
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 30
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 40
            tb[2] = -8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[12] = tb
            tb[1] = 20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[13] = tb
            tb[1] = 10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[14] = tb
            tb[1] = 0
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[15] = tb
            tb[1] = -10
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[16] = tb
            tb[1] = -20
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[17] = tb
            tb[1] = -30
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[18] = tb
            tb[1] = -40
            tb[2] = 8
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[19] = tb
            tb[1] = 0
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2020" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 1" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.1 
        item.scene_width = 1166.0 
        item.scene_height = 1234.0 
        item.role_fish_id = 31 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 1 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2021" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 2" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.2 
        item.scene_width = 1509.0 
        item.scene_height = 1156.0 
        item.role_fish_id = 32 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 2 
        item.ai_fish_smart_factor = 2 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2022" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 3" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.3 
        item.scene_width = 1727.0 
        item.scene_height = 1056.0 
        item.role_fish_id = 33 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 5 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 3 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2023" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 4" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.4 
        item.scene_width = 1235.0 
        item.scene_height = 1361.0 
        item.role_fish_id = 34 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 4 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2024" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 5" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.5 
        item.scene_width = 1749.0 
        item.scene_height = 983.0 
        item.role_fish_id = 35 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 5 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 5 
        item.ai_fish_smart_factor = 5 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2025" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 6" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.6 
        item.scene_width = 1113.0 
        item.scene_height = 1081.0 
        item.role_fish_id = 36 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 1 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 6 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2026" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 7" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.7 
        item.scene_width = 1465.0 
        item.scene_height = 1085.0 
        item.role_fish_id = 37 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 3 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 7 
        item.ai_fish_smart_factor = 4 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2027" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 8" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.8 
        item.scene_width = 1630.0 
        item.scene_height = 1827.0 
        item.role_fish_id = 38 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 6 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 8 
        item.ai_fish_smart_factor = 4 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2028" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 9" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.9 
        item.scene_width = 1223.0 
        item.scene_height = 1355.0 
        item.role_fish_id = 39 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 1 
        item.lv1_fish_num_max = 6 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 9 
        item.ai_fish_smart_factor = 3 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end
    do
        ---@type LogicConfigExplore_
        local item = {}
        table.insert(item_list, item) 
        item.config_id = "2029" 
        item.theme_name = "theme_4" 
        item.config_name = "brook.level 10" 
        item.descript = "Eat one fish to pass level" 
        item.first_reward_id = {}
        do
            item.first_reward_id[1] = 1000
            item.first_reward_id[2] = 1001
        end 
        item.reward_id = {}
        do
            item.reward_id[1] = 1000
            item.reward_id[2] = 1001
        end 
        item.background = {}
        do
            local tb = {}
            item.background[1] = tb
            tb[1] = "map_001.png"
            tb[2] = "0"
            tb[3] = "0"
        end
        do
            local tb = {}
            item.background[2] = tb
            tb[1] = "map_stone_001.png"
            tb[2] = "15"
            tb[3] = "15"
        end 
        item.level_factor = 4.99999999999999 
        item.scene_width = 1826.0 
        item.scene_height = 1357.0 
        item.role_fish_id = 10 
        item.phase_effect_role_fish_size_list = {}
        do
            item.phase_effect_role_fish_size_list[1] = 0.5
            item.phase_effect_role_fish_size_list[2] = 1.0
        end 
        item.phase_appear_fish_group = {}
        do
            local tb = {}
            item.phase_appear_fish_group[1] = tb
            tb[1] = 1
            tb[2] = 2
        end
        do
            local tb = {}
            item.phase_appear_fish_group[2] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
        end
        do
            local tb = {}
            item.phase_appear_fish_group[3] = tb
            tb[1] = 1
            tb[2] = 2
            tb[3] = 3
            tb[4] = 4
        end 
        item.lv1_fish_num_min = 2 
        item.lv1_fish_num_max = 4 
        item.lv1_fish_ids = {}
        do
            item.lv1_fish_ids[1] = 1
            item.lv1_fish_ids[2] = 2
        end 
        item.lv1_group_density = 1 
        item.lv2_fish_num_min = 1 
        item.lv2_fish_num_max = 1 
        item.lv2_fish_ids = {}
        do
            item.lv2_fish_ids[1] = 2
            item.lv2_fish_ids[2] = 3
        end 
        item.lv2_group_density = 14 
        item.lv3_fish_num_min = 1 
        item.lv3_fish_num_max = 1 
        item.lv3_fish_ids = {}
        do
            item.lv3_fish_ids[1] = 3
            item.lv3_fish_ids[2] = 4
        end 
        item.lv3_group_density = 20 
        item.ai_group_num = 10 
        item.ai_fish_smart_factor = 0 
        item.ai_fish_ids = {}
        do
            item.ai_fish_ids[1] = 4
            item.ai_fish_ids[2] = 5
        end 
        item.common_fish_cruise_path = {}
        do
            local tb = {}
            item.common_fish_cruise_path[1] = tb
            tb[1] = 955
            tb[2] = 755
        end
        do
            local tb = {}
            item.common_fish_cruise_path[2] = tb
            tb[1] = 17
            tb[2] = 279
        end
        do
            local tb = {}
            item.common_fish_cruise_path[3] = tb
            tb[1] = 78
            tb[2] = 148
        end
        do
            local tb = {}
            item.common_fish_cruise_path[4] = tb
            tb[1] = 284
            tb[2] = 889
        end
        do
            local tb = {}
            item.common_fish_cruise_path[5] = tb
            tb[1] = 109
            tb[2] = 676
        end
        do
            local tb = {}
            item.common_fish_cruise_path[6] = tb
            tb[1] = 497
            tb[2] = 209
        end
        do
            local tb = {}
            item.common_fish_cruise_path[7] = tb
            tb[1] = 594
            tb[2] = 168
        end
        do
            local tb = {}
            item.common_fish_cruise_path[8] = tb
            tb[1] = 453
            tb[2] = 869
        end
        do
            local tb = {}
            item.common_fish_cruise_path[9] = tb
            tb[1] = 389
            tb[2] = 451
        end
        do
            local tb = {}
            item.common_fish_cruise_path[10] = tb
            tb[1] = 356
            tb[2] = 950
        end
        do
            local tb = {}
            item.common_fish_cruise_path[11] = tb
            tb[1] = 131
            tb[2] = 285
        end 
        item.ai_fish_cruise_path = {}
        do
            local tb = {}
            item.ai_fish_cruise_path[1] = tb
            tb[1] = 379
            tb[2] = 80
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[2] = tb
            tb[1] = 913
            tb[2] = 206
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[3] = tb
            tb[1] = 770
            tb[2] = 839
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[4] = tb
            tb[1] = 116
            tb[2] = 271
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[5] = tb
            tb[1] = 543
            tb[2] = 769
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[6] = tb
            tb[1] = 210
            tb[2] = 426
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[7] = tb
            tb[1] = 618
            tb[2] = 735
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[8] = tb
            tb[1] = 672
            tb[2] = 179
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[9] = tb
            tb[1] = 426
            tb[2] = 44
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[10] = tb
            tb[1] = 967
            tb[2] = 258
        end
        do
            local tb = {}
            item.ai_fish_cruise_path[11] = tb
            tb[1] = 929
            tb[2] = 554
        end
    end

    local item_map = {}
    for _, v in ipairs(item_list) do
        item_map[v.config_id] = v
    end
    return item_map, item_list
end

function _config_require_explore()
    return Logic_Config_Name.explore, get_config_map()
end