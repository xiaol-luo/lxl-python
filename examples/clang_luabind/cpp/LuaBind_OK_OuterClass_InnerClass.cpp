#include "UserType/TryUserTypeUtil.h"
#include <sol.hpp>
#include "AutoBind/AutoHead.h"

namespace TryUserType
{
	void LuaBind_OK_OuterClass_InnerClass(lua_State *L)
	{
		struct LuaBindImpl
		{
			static void DoLuaBind(lua_State *L)
			{
                std::string name = "InnerClass";
				std::string name_space = "OK.OuterClass";

				{
					sol::usertype<OK::OuterClass::InnerClass> meta_table(
						sol::constructors<\
						>()				
						,"ival", &OK::OuterClass::InnerClass::ival				
						,"TestInnerFunc", &OK::OuterClass::InnerClass::TestInnerFunc
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