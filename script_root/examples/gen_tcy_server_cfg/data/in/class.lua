local meta_fn_name = {
    "__gc",
    "__pairs",
    "__add",
    "__sub",
    "__mul",
    "__div",
    "__mod",
    "__pow",
    "__unm",
    "__idiv",
    "__band",
    "__bor",
    "__bxor",
    "__bnot",
    "__shl",
    "__shr",
    "__concat",
    "__len",
    "__eq",
    "__lt",
    "__le",
    "__newindex",
    "__call",
}

local setmetatable_help_
setmetatable_help_ = function(t, index)
    assert(not getmetatable(t))
    setmetatable(t, index)
end
setmetatable_help = setmetatable_help_

-- local tRegisterClass = {}

function class(class_name, super)
    -- assert(not tRegisterClass[class_name], string.format("class() - has created class \"%s\" ", class_name))
    -- tRegisterClass[class_name] = true

    local super_type = type(super)
    assert("nil" == super_type or "table" == super_type,
            string.format("class() - create class \"%s\" with invalid super class type \"%s\"", class_name, super_type))

    local cls = { __cname = class_name }
    cls.super = super
    cls.__index = cls
    setmetatable(cls, { __index = cls.super })

    if not cls.ctor then
        cls.ctor = function() end
    end

    cls.new = function(_, ...)
        local instance = {}
        setmetatable_help(instance, cls)
        instance:ctor(...)
        return instance
    end

    return cls
end