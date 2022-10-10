
--去除后面的空格,换行
function string_rtrim(str, chs)
	local chs_val = {}
	for _, v in ipairs({string.byte(chs, 1, #chs)}) do
		chs_val[v] = true
	end
	local idx = 0
	for i = #str,1,-1 do
		if not chs_val[string.byte(str, i)] then
			idx = i
			break
		end
	end
	return idx < 1 and "" or string.sub(str,1, idx)
end

--去除前面的空格,换行
function string_ltrim(str, chs)
	local chs_val = {}
	for _, v in ipairs({string.byte(chs, 1, #chs)}) do
		chs_val[v] = true
	end
	local idx = #str + 1
	for i = 1, #str do
		if not chs_val[string.byte(str, i)] then
			idx = i
			break
		end
	end
	return idx > #str and "" or string.sub(str,idx)
end

--去除前后的空格和换行
function string_lrtrim(str, chs)
	return string_rtrim.rtrim(string_ltrim(str, chs), chs)
end

path = path or {}

function path_combine(...)
    local ret = ""
    local is_first = true
    for _, v in ipairs({...}) do
        if is_first then
            is_first = false
            ret = string_rtrim(tostring(v), "\\/")
        else
            ret = ret .. "/" .. string_ltrim(tostring(v), "\\/")
        end
    end
    ret = string.gsub(ret, "\\", "/")
    return ret
end

function is_table(v)
	return type(v) == "table"
end

function is_class(Cls)
	if not is_table(Cls) then return false end

	local __index = rawget(Cls, "__index")
	local __cname = rawget(Cls, "__cname")
	return __index ~= nil and __index == Cls and __cname ~= nil
end

function is_class_instance(ins, Cls)
	if not is_table(ins) then return false end
	if not is_class(Cls) then return false end
	local cls_type = getmetatable(ins)
	if not is_table(cls_type) then return false end
	local ins_cname = rawget(cls_type, "__cname")
	if not ins_cname then return false end
	local cls_cname = rawget(Cls, "__cname")
	if ins_cname ~= cls_cname then
		return false
	end
	return true
end

---@param visit_fn fun(tb: table):boolean
function travel_table(root_tb, visit_fn)
	if not visit_fn then
		return
	end

	local repeat_checker = {}
    local stack = {root_tb}
    while #stack > 0 do
        local elem = table.remove(stack, 1)
        if "table" == type(elem) and not repeat_checker[elem] then
            repeat_checker[elem] = true
			local local_repeat_checker = {}
			for _, v in ipairs(elem) do
                if "table" == type(v) then
					local_repeat_checker[v] = true
                    table.insert(stack, v)
                end
            end

            for _, v in pairs(elem) do
				if "table" == type(v) and not local_repeat_checker[v] then
					local_repeat_checker[v] = true
                    table.insert(stack, v)
				end
            end
			local ret = visit_fn(elem)
			if false == ret then
				break
			end
        end
    end
end


function string_concat(s1, ...)
	return string_concat_witch_sep("_", s1, ...)
end

function string_concat_witch_sep(sep, s1, ...)
	local tb = {s1, ...}
	local ret = table.concat(tb, sep)
	return ret
end