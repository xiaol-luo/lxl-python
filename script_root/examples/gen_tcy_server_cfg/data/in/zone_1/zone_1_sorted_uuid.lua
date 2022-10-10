
local sorted_uuid = {
    "etcd_server_zone_1_etcd_1",
    "etcd_server_zone_1_etcd_2",
    "etcd_server_zone_1_etcd_3",
    "redis_server_zone_1_redis_1",
    "redis_server_zone_1_redis_2",
    "redis_server_zone_1_redis_3",
    "redis_server_zone_1_redis_4",
    "redis_server_zone_1_redis_5",
    "redis_server_zone_1_redis_6",
    "mongos_serverzone_1_mongos_1",
    "mongodb_serverzone_1_mongodb_1",
    "mongodb_serverzone_1_mongodb_2",
    "mongodb_serverzone_1_mongodb_3",
    "mongodb_serverzone_1_mongodb_11",
    "mongodb_serverzone_1_mongodb_12",
    "mongodb_serverzone_1_mongodb_13",
    "mongodb_serverzone_1_mongodb_21",
    "mongodb_serverzone_1_mongodb_22",
    "mongodb_serverzone_1_mongodb_23",
    "mongodb_serverzone_1_mongodb_31",
    "mongodb_serverzone_1_mongodb_32",
    "mongodb_serverzone_1_mongodb_33",
    "game_server_zone_1_platform",
    "game_server_zone_1_auth",
    "game_server_zone_1_login_0",
    "game_server_zone_1_create_role_0",
    "game_server_zone_1_world_0",
    "game_server_zone_1_world_1",
    "game_server_zone_1_game_0",
    "game_server_zone_1_gate_0",
    "game_server_zone_1_match_0",
    "game_server_zone_1_room_0",
    "game_server_zone_1_fight_0",
    "game_server_zone_1_world_sentinel_0",
    "game_server_zone_1_workbench_0",
    "game_server_zone_1_message_hub_0",
}

local function sort_fn(all_setting, uuid_list)
    local uuid_map = {}
    for idx, elem in ipairs(uuid_list) do
        uuid_map[elem] = idx
    end
    local sorted_named_setting_list = {}
    local unsorted_named_setting_list = {}
    local unnamed_setting_list = {}
    travel_table(all_setting, function(st)
        local st_uuid = nil
        if st and st.get_uuid and "function" == type(st.get_uuid) then
            st_uuid = st.get_uuid(st)
        end
        if not st_uuid then
            table.insert(unnamed_setting_list, st)
        else
            if uuid_map[st_uuid] then
                table.insert(sorted_named_setting_list, st)
            else
                table.insert(unsorted_named_setting_list, st)
            end
        end
    end)

    table.sort(sorted_named_setting_list, function(a, b)
        local a_uuid = a:get_uuid()
        local b_uuid = b:get_uuid()
        return uuid_map[a_uuid] < uuid_map[b_uuid]
    end)

    local ret = {}
    for _, elem in ipairs(sorted_named_setting_list) do
        table.insert(ret, elem)
    end
        for _, elem in ipairs(unsorted_named_setting_list) do
        table.insert(ret, elem)
    end
        for _, elem in ipairs(unnamed_setting_list) do
        table.insert(ret, elem)
    end
    return ret
end

return {sorted_uuid=sorted_uuid, sort_fn=sort_fn}