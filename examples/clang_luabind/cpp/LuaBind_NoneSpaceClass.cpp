#include "UserType/TryUserTypeUtil.h"
#include <sol.hpp>
#include "AutoBind/AutoHead.h"

namespace TryUserType
{
	void LuaBind_NoneSpaceClass(lua_State *L)
	{
		struct LuaBindImpl
		{
			static void DoLuaBind(lua_State *L)
			{
                std::string name = "NoneSpaceClass";
				std::string name_space = "";

				{
					sol::usertype<NoneSpaceClass> meta_table(
						sol::constructors<\
						>()				
						,"iVal", &NoneSpaceClass::iVal				
						,"Test", &NoneSpaceClass::Test
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