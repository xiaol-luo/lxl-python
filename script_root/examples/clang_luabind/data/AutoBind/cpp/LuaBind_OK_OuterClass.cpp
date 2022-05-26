#include "SolLuaBindUtils.h"
#include <sol.hpp>

namespace SolLuaBind
{
	void LuaBind_OK_OuterClass(lua_State *L)
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
                std::string name = "OuterClass";
				std::string name_space = "OK";

				{
					sol::usertype<OK::OuterClass> meta_table(
						sol::constructors<				
						OK::OuterClass(),				
						OK::OuterClass(int)
						>(),
						"__StructName__", sol::property([]() {return "OuterClass"; })				
						,"inClass", &OK::OuterClass::inClass				
						,"fval", &OK::OuterClass::fval				
						,"TestOuterFun", &OK::OuterClass::TestOuterFun				
						,"TestStaticFun", &OK::OuterClass::TestStaticFun				
						, sol::base_classes, sol::bases<
							OK::Base 
						>()
					);
					SolLuaBindUtils::BindLuaUserType(sol::state_view(L), meta_table, name, name_space);
				}
            
				{
					sol::table ns_table = SolLuaBindUtils::GetOrNewLuaNameSpaceTable(sol::state_view(L), name_space)[name];				
					{
						std::string var_name = "siVal";
						sol::object obj = ns_table.raw_get_or(var_name, sol::nil);
						assert(!obj.valid());
						ns_table.set(var_name, OK::OuterClass::siVal);
					}
				}
			}
		};

		LuaBindImpl::DoLuaBind(L);
	}
}