#include "UserType/TryUserTypeUtil.h"
#include <sol.hpp>
#include "AutoBind/AutoHead.h"

namespace TryUserType
{
	void LuaBind_OK_Test(lua_State *L)
	{
		struct LuaBindImpl
		{
			static void DoLuaBind(lua_State *L)
			{
                std::string name = "Test";
				std::string name_space = "OK";

				{
					sol::usertype<OK::Test> meta_table(
						sol::constructors<\
						>()				
						,"a", &OK::Test::a
					);
					BindLuaUserType(sol::state_view(L), meta_table, name, name_space);
				}
            
				{
					sol::table ns_table = GetOrNewLuaNameSpaceTable(sol::state_view(L), name_space)[name];				
				}
			}
		};

		LuaBindImpl::DoLuaBind(L);
	}
}