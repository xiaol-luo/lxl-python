#include "UserType/TryUserTypeUtil.h"
#include <sol.hpp>
#include "AutoBind/AutoHead.h"

namespace TryUserType
{
	void LuaBind_OK_OuterClass(lua_State *L)
	{
		struct LuaBindImpl
		{
			static void DoLuaBind(lua_State *L)
			{
                std::string name = "OuterClass";
				std::string name_space = "OK";

				{
					sol::usertype<OK::OuterClass> meta_table(
						sol::constructors<\				
						OK::OuterClass(), \				
						OK::OuterClass(int) \
						>()				
						,"inClass", &OK::OuterClass::inClass				
						,"fval", &OK::OuterClass::fval				
						,"TestOuterFun", &OK::OuterClass::TestOuterFun				
						,"TestStaticFun", &OK::OuterClass::TestStaticFun				
						, sol::base_classes, sol::bases<\
							OK::Base \
						\>()
					);
					BindLuaUserType(sol::state_view(L), meta_table, name, name_space);
				}
            
				{
					sol::table ns_table = GetOrNewLuaNameSpaceTable(sol::state_view(L), name_space)[name];				
					ns_table.set("siVal", OK::OuterClass::siVal);				
				}
			}
		};

		LuaBindImpl::DoLuaBind(L);
	}
}