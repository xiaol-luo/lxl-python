#include "SolLuaBindUtils.h"
#include <sol.hpp>

namespace SolLuaBind
{
	void LuaBind_OK(lua_State *L)
	{
		struct LuaBindImpl
		{
			struct ForOverloadFns
			{
			};

			static void DoLuaBind(lua_State *L)
			{
				std::string name_space = "OK";

				sol::state_view lua(L);

				sol::table ns_table = SolLuaBindUtils::GetOrNewLuaNameSpaceTable(lua, name_space);				
				{
					std::string name = "CommonIVal";
					sol::object obj = ns_table.raw_get_or(name, sol::nil);
					assert(!obj.valid());
					ns_table.set(name, OK::CommonIVal);
				}				
				{
					std::string name = "CommonFunc";
					sol::object obj = ns_table.raw_get_or(name, sol::nil);
					assert(!obj.valid());
					ns_table.set_function(name, OK::CommonFunc);
				}			
			}
		};

		LuaBindImpl::DoLuaBind(L);
	}
}