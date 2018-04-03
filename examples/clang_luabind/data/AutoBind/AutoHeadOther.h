#pragma once

namespace OKOther
{
	class Test;
	class Test
	{ 
	public:
		int a;
	};
	class Base {};

	class OuterClas : public Base
	{
	public:
		struct InnerClass
		{
			int ival = 0;
			const int * TestInnerFunc(const int param) { return 0; }
		};

	public:
		OuterClas() {}

		InnerClass inClas;
		const float fval = 2;
		static int siVal;
		int TestOuterFun(InnerClass && param, int param2) { return 0; }
	};
	
	extern int CommonFunc(OuterClas outerClass, int param);
	extern int CommonIVal;
}