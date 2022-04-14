
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