# mwam.comment "之后的变量就加这吧"

# --- 某些状态 ---
default another_view = False
default session_title = None
default is_ingame = False

# --- 分支变量 ---
default variables = {
    "gra_chemistry_name": None,
    "overwatch_first": None,
    "volunteer_to_do_curse": None,
}

# --- 持久化变量 ---
default persistent.debug_mode = False

# yangsy.comment 不是谁想的把debug模式密码扔到persistent里的啊（
# yangsy.comment Yangsy改成判断条件硬编码了（（（

default persistent.variables = {
    "has_seen_ending": False,
    "duplicate_name_fixed": False,
    "setup_saw_debug_screen": False,
}