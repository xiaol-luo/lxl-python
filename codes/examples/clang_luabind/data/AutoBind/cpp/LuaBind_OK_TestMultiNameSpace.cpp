#include "SolLuaBindUtils.h"
#include <sol.hpp>

namespace SolLuaBind
{
	void LuaBind_OK_TestMultiNameSpace(lua_State *L)
	{
		struct LuaBindImpl
		{
			struct ForOverloadFns
			{
			};
			
			struct ForPropertyField
			{
			};			
			

			static void DoLuaBind(lua_State *L)
			{
                std::string name = "TestMultiNameSpace";
				std::string name_space = "OK";

				{
					sol::usertype<OK::TestMultiNameSpace> meta_table(
						"__StructName__", sol::property([]() {return "TestMultiNameSpace"; })
					);
					SolLuaBindUtils::BindLuaUserType(sol::state_view(L), meta_table, name, name_space);
				}
            
				{
					sol::table ns_table = SolLuaBindUtils::GetOrNewLuaNameSpaceTable(sol::state_view(L), name_space)[name];
				}
			}
		};

		LuaBindImpl::DoLuaBind(L);
	}
}