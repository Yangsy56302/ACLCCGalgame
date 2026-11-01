# mwam.comment "之后的变量就加这吧"

# --- 某些状态 ---
default session_title = None
default is_ingame = False

# --- 分支变量 ---
default variables = {
    "another_view": False,
    "gra_chemistry_name": None,
    "overwatch_first": None,
    "volunteer_to_do_curse": None,
    "yangsy_curse_impression": None,
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

init python:
    def migrate_persistent_variables():
        if persistent.variables is None:
            persistent.variables = {}

        for key, default in (
            ("has_seen_ending", False),
            ("duplicate_name_fixed", False),
            ("setup_saw_debug_screen", False),
        ):
            if key not in persistent.variables:
                persistent.variables[key] = default

        # 兼容旧存档：把旧的属性写法迁移到字典，然后删掉旧属性。
        for old_key in ("has_seen_ending", "duplicate_name_fixed", "setup_saw_debug_screen"):
            if persistent.__dict__.pop(old_key, None):
                persistent.variables[old_key] = True