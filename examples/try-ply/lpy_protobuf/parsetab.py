
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'L_BRACE R_BRACE EQUAL SEMICOLON QUOTATION D_QUATION DOT NUMBER BOOL STRING ID COMMENT KW_MESSAGE KW_SYNTAX KW_OPTION KW_PACKAGE KW_REPEATED KW_ENUM KW_IMPORTbegin : exprexpr :expr : expr simple_keyword_exprexpr : expr enum_keyword_exprexpr : expr message_keyword_exprsimple_keyword_expr : KW_SYNTAX EQUAL STRING SEMICOLONsimple_keyword_expr : KW_OPTION ID EQUAL values SEMICOLONsimple_keyword_expr : KW_PACKAGE package_name SEMICOLONsimple_keyword_expr : KW_IMPORT STRING SEMICOLONvalues : BOOLvalues : NUMBERvalues : STRINGpackage_name : package_name DOT IDpackage_name : IDenum_keyword_expr : KW_ENUM ID L_BRACE enum_content R_BRACEenum_content : enum_content ID EQUAL NUMBER SEMICOLONenum_content :message_keyword_expr : KW_MESSAGE ID L_BRACE message_content R_BRACEmessage_content : message_content ID ID EQUAL NUMBER SEMICOLONmessage_content : message_content KW_REPEATED ID ID EQUAL NUMBER SEMICOLONmessage_content :message_content : message_content message_keyword_exprmessage_content : message_content enum_keyword_expr'
    
_lr_action_items = {'KW_SYNTAX':([0,2,3,4,5,21,23,26,34,36,38,],[-2,6,-3,-4,-5,-8,-9,-6,-7,-15,-18,]),'KW_OPTION':([0,2,3,4,5,21,23,26,34,36,38,],[-2,7,-3,-4,-5,-8,-9,-6,-7,-15,-18,]),'KW_PACKAGE':([0,2,3,4,5,21,23,26,34,36,38,],[-2,8,-3,-4,-5,-8,-9,-6,-7,-15,-18,]),'KW_IMPORT':([0,2,3,4,5,21,23,26,34,36,38,],[-2,9,-3,-4,-5,-8,-9,-6,-7,-15,-18,]),'KW_ENUM':([0,2,3,4,5,21,23,25,26,33,34,36,38,40,41,51,53,],[-2,10,-3,-4,-5,-8,-9,-21,-6,10,-7,-15,-18,-22,-23,-19,-20,]),'KW_MESSAGE':([0,2,3,4,5,21,23,25,26,33,34,36,38,40,41,51,53,],[-2,11,-3,-4,-5,-8,-9,-21,-6,11,-7,-15,-18,-22,-23,-19,-20,]),'$end':([0,1,2,3,4,5,21,23,26,34,36,38,],[-2,0,-1,-3,-4,-5,-8,-9,-6,-7,-15,-18,]),'EQUAL':([6,13,35,43,47,],[12,20,42,46,50,]),'ID':([7,8,10,11,22,24,25,32,33,36,37,38,39,40,41,44,48,51,53,],[13,15,17,18,31,-17,-21,35,37,-15,43,-18,44,-22,-23,47,-16,-19,-20,]),'STRING':([9,12,20,],[16,19,30,]),'SEMICOLON':([14,15,16,19,27,28,29,30,31,45,49,52,],[21,-14,23,26,34,-10,-11,-12,-13,48,51,53,]),'DOT':([14,15,31,],[22,-14,-13,]),'L_BRACE':([17,18,],[24,25,]),'BOOL':([20,],[28,]),'NUMBER':([20,42,46,50,],[29,45,49,52,]),'R_BRACE':([24,25,32,33,36,38,40,41,48,51,53,],[-17,-21,36,38,-15,-18,-22,-23,-16,-19,-20,]),'KW_REPEATED':([25,33,36,38,40,41,51,53,],[-21,39,-15,-18,-22,-23,-19,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'begin':([0,],[1,]),'expr':([0,],[2,]),'simple_keyword_expr':([2,],[3,]),'enum_keyword_expr':([2,33,],[4,41,]),'message_keyword_expr':([2,33,],[5,40,]),'package_name':([8,],[14,]),'values':([20,],[27,]),'enum_content':([24,],[32,]),'message_content':([25,],[33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> begin","S'",1,None,None,None),
  ('begin -> expr','begin',1,'p_begin','lpy_protobuf.py',114),
  ('expr -> <empty>','expr',0,'p_expr_empty','lpy_protobuf.py',118),
  ('expr -> expr simple_keyword_expr','expr',2,'p_expr_simple_keyword','lpy_protobuf.py',122),
  ('expr -> expr enum_keyword_expr','expr',2,'p_expr_enum_keyword','lpy_protobuf.py',127),
  ('expr -> expr message_keyword_expr','expr',2,'p_expr_message_keyword','lpy_protobuf.py',133),
  ('simple_keyword_expr -> KW_SYNTAX EQUAL STRING SEMICOLON','simple_keyword_expr',4,'p_simple_keyword_expr_syntax','lpy_protobuf.py',140),
  ('simple_keyword_expr -> KW_OPTION ID EQUAL values SEMICOLON','simple_keyword_expr',5,'p_simple_keyword_expr_option','lpy_protobuf.py',144),
  ('simple_keyword_expr -> KW_PACKAGE package_name SEMICOLON','simple_keyword_expr',3,'p_simple_keyword_expr_package','lpy_protobuf.py',148),
  ('simple_keyword_expr -> KW_IMPORT STRING SEMICOLON','simple_keyword_expr',3,'p_simple_keyword_expr_import','lpy_protobuf.py',152),
  ('values -> BOOL','values',1,'p_values_bool','lpy_protobuf.py',157),
  ('values -> NUMBER','values',1,'p_values_number','lpy_protobuf.py',161),
  ('values -> STRING','values',1,'p_values_string','lpy_protobuf.py',165),
  ('package_name -> package_name DOT ID','package_name',3,'p_package_name_composite','lpy_protobuf.py',170),
  ('package_name -> ID','package_name',1,'p_package_name_id','lpy_protobuf.py',178),
  ('enum_keyword_expr -> KW_ENUM ID L_BRACE enum_content R_BRACE','enum_keyword_expr',5,'p_enum_keyword_expr','lpy_protobuf.py',185),
  ('enum_content -> enum_content ID EQUAL NUMBER SEMICOLON','enum_content',5,'p_enum_content_normal','lpy_protobuf.py',192),
  ('enum_content -> <empty>','enum_content',0,'p_enum_content_empty','lpy_protobuf.py',201),
  ('message_keyword_expr -> KW_MESSAGE ID L_BRACE message_content R_BRACE','message_keyword_expr',5,'p_message_keyword_expr','lpy_protobuf.py',205),
  ('message_content -> message_content ID ID EQUAL NUMBER SEMICOLON','message_content',6,'p_message_content_normal','lpy_protobuf.py',221),
  ('message_content -> message_content KW_REPEATED ID ID EQUAL NUMBER SEMICOLON','message_content',7,'p_message_content_repeated','lpy_protobuf.py',232),
  ('message_content -> <empty>','message_content',0,'p_message_content_empty','lpy_protobuf.py',243),
  ('message_content -> message_content message_keyword_expr','message_content',2,'p_message_content_nested_message','lpy_protobuf.py',246),
  ('message_content -> message_content enum_keyword_expr','message_content',2,'p_message_content_nested_enum','lpy_protobuf.py',252),
]