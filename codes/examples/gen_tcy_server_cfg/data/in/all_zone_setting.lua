
zone_1 = {1, 2, 3}
all_setting =
{
    zone_settings = {
        zone_1 = require "zone_1_setting",
    },
    servers = {
        zone_1 = zone_1,
    },
    c = {servers, 1, 2},
    d = 1,
    f = 2,
}

---@class server
--- @field name string
local server = {}

