import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

# ===============================
# 基础配置
# ===============================
WIN_W, WIN_H = 950, 680
FONT_TEXT = ("微软雅黑", 12)
FONT_TITLE = ("微软雅黑", 12, "bold")
BOOK_BG = "#FAF0E6"
PAGE_BORDER = "#D2B48C"
PAGE_BG = "#FFFFFF"
BTN_BG = "#E0F7FA"
BTN_HOVER = "#B2EBF2"

# ===============================
# 核心线索定义（仅用于记录，不影响结局）
# ===============================
CORE_CLUES = {
    "旧馆B区书架排列规律",
    "绝版书外观特征",
    "封闭层钥匙与时间"
}

# ===============================
# 图片路径
# ===============================
IMG = {
    "aunt": "images/aunt.png",
    "cleaner": "images/cleaner.png",
    "opening": "images/opening.png",
    "closed": "images/closed.png",
    "perfect_end": "images/perfect_end.png"  # 确保该路径对应完美结局插画
}

# ===============================
# Tk 初始化
# ===============================
root = tk.Tk()
root.title("校园图书馆寻宝")
root.geometry(f"{WIN_W}x{WIN_H}")
root.resizable(False, False)
root.configure(bg=BOOK_BG)

# ===============================
# 工具：加载图片
# ===============================
# 全局变量存储图片引用，防止被垃圾回收
img_cache = {}

def load_img(path, w, h):
    global img_cache
    # 先从缓存读取，避免重复加载
    if path in img_cache:
        return img_cache[path]
    try:
        img = Image.open(path).resize((w, h), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        img_cache[path] = tk_img
        return tk_img
    except (FileNotFoundError, ImportError, AttributeError):
        # 无图片时返回占位文本（不返回None，避免显示异常）
        return f"[插画：{path.split('/')[-1]}]"

# ===============================
# UI 布局（保持已调整好的显示区域）
# ===============================
# 剧情展示区（画中框主区域）
outer = tk.Frame(root, bg=PAGE_BORDER)
outer.place(x=30, y=20, width=620, height=430)

inner = tk.Frame(outer, bg=PAGE_BG)
inner.place(x=10, y=10, width=600, height=410)

top = tk.Frame(inner, bg=PAGE_BG)
top.pack(fill=tk.X)

avatar_frame = tk.Frame(top, bg=PAGE_BG, highlightbackground="#8B4513", highlightthickness=2)
avatar_label = tk.Label(avatar_frame, bg=PAGE_BG)
avatar_label.pack(padx=5, pady=5)
avatar_frame.pack_forget()

illu_frame = tk.Frame(top, bg=PAGE_BG, highlightbackground="#000000", highlightthickness=1)
illu_label = tk.Label(illu_frame, bg=PAGE_BG)
illu_label.pack(padx=5, pady=5)
illu_frame.pack_forget()

text_box = scrolledtext.ScrolledText(
    inner, font=FONT_TEXT, wrap=tk.WORD,
    state="disabled", bg=PAGE_BG, relief="flat"
)
text_box.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

# 按钮区域（保持已调整好的排版）
btn_outer = tk.Frame(root, bg=PAGE_BORDER)
btn_outer.place(x=30, y=470, width=620, height=180)
btn_inner = tk.Frame(btn_outer, bg=BOOK_BG)
btn_inner.place(x=10, y=10, width=600, height=160)

# 线索本区域（保留原有样式，仅用于记录）
clue_outer = tk.Frame(root, bg=PAGE_BORDER)
clue_outer.place(x=680, y=20, width=240, height=630)

tk.Label(clue_outer, text="线索本", font=FONT_TITLE, bg=PAGE_BORDER).pack(pady=5)
clue_box = tk.Text(clue_outer, state="disabled", bg=PAGE_BG, font=("微软雅黑", 11))
clue_box.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
clue_box.tag_config("core", foreground="darkgreen", font=("微软雅黑", 10, "bold"))

# ===============================
# 游戏状态（初始化完善）
# ===============================
clues = set()
time_flag = True  # 是否错过时间窗口

def add_clue(c):
    """线索仅用于记录，不影响结局判定"""
    if c not in clues and c in CORE_CLUES:
        clues.add(c)
        clue_box.config(state="normal")
        clue_box.insert(tk.END, f"• ★ 核心线索 ★ {c}\n", "core")
        clue_box.see(tk.END)
        clue_box.config(state="disabled")

# ===============================
# 剧情数据
# ===============================
story = {
    "start": {
        "text": "期末周的图书馆安静得只剩翻书声，你在靠窗座位的桌肚里摸到一张泛黄纸条，纸条只写了半句话：“旧馆三层，B区，藏着……”，周围只有服务台的张阿姨在整理书籍。",
        "image": "opening",
        "options": [
            ("打开纸条，辨认残留字迹", "note"),
            ("观察环境（桌角、邻座）", "observe"),
            ("先做两道题，稍后探索", "study")
        ]
    },

    "note": {
        "text": "你小心翼翼展开纸条，看清末尾有个淡淡的银杏印，字迹褪色严重无法辨认更多信息，服务台的张阿姨朝你投来了好奇的目光。",
        "options": [
            ("拿着纸条询问张阿姨", "aunt"),
            ("不打扰别人，直接去旧馆", "gate_cleaner")
        ]
    },

    "observe": {
        "text": "你仔细观察四周，发现桌角刻着“B-317”和一个小小的银杏标记，邻座桌上放着一本图书馆馆藏指南，里面还夹着一张旧馆地图。",
        "options": [
            ("悄悄翻看馆藏指南（看完放回）", "guide"),
            ("记下桌角编号，去旧馆门口打探", "gate_cleaner")
        ]
    },

    "study": {
        "text": "你收起纸条开始做题，无意间翻到教材里夹着一张旧借阅笔记，笔记主人是2016级学生，上面写着：“深蓝的书，在B区最里面，夹着银杏书签”，这时张阿姨过来整理你身边的书架。",
        "options": [
            ("放下习题，询问张阿姨旧馆B区事宜", "aunt_blue"),
            ("做完这道题再去，多花10分钟", "late_gate")
        ]
    },

    "aunt": {
        "text": "张阿姨压低声音对你说：“旧馆B区的书早就不对外借了，尤其是深处的封闭层——那里面放的都是几十年前的绝版书，平时锁着，只有管理员有钥匙”，说完给你指了指墙上的馆藏图。",
        "avatar": "aunt",
        "options": [
            ("去看墙上的馆藏图，记录布局", "rule"),
            ("感谢张阿姨，直接前往旧馆", "gate_cleaner")
        ]
    },

    "guide": {
        "text": "你在馆藏指南里找到了旧馆B区的详细地图，地图上标注着“B区深处有封闭层（因书籍年代久远，仅管理员可开启）”，还看到一行小字备注：“书架按出版年代倒序排列，末尾补号区分同年代书籍”。\n（你默默记下：封闭层是旧馆B区的特殊区域，需要特定条件才能进入）",
        "options": [
            ("去服务台找张阿姨，询问封闭层钥匙", "aunt_key"),
            ("收好指南，直接去旧馆找B区", "rule")
        ]
    },

    "aunt_key": {
        "text": "你找到张阿姨，询问封闭层钥匙的下落。张阿姨犹豫了一下说：“钥匙藏在服务台抽屉下方的暗格里，每天傍晚6点管理员换班时解锁，错过就没机会了”。",
        "avatar": "aunt",
        "clue": "封闭层钥匙与时间",
        "options": [
            ("立刻去旧馆，先找书架规律", "rule"),
            ("先等临近6点，再去旧馆", "gate_cleaner")
        ]
    },

    "gate_cleaner": {
        "text": "你来到旧馆门口，发现大门半掩着，一位保洁阿姨正在门口打扫卫生，阿姨看到你笑着说：“小伙子/小姑娘，这旧馆每天傍晚6点，管理员会来换班，顺便给封闭层通风”。",
        "avatar": "cleaner",
        "options": [
            ("向保洁阿姨追问，封闭层钥匙放在哪里", "key_info"),
            ("谢过阿姨，先进入旧馆找到B区", "rule"),
            ("谢过阿姨，先确认钥匙信息，再找B区", "key_info_first")
        ]
    },

    "key_info_first": {
        "text": "你向保洁阿姨追问钥匙下落，阿姨悄悄说：“钥匙藏在服务台抽屉下的暗格里，6点换班时解锁，千万别错过时间”。",
        "avatar": "cleaner",
        "clue": "封闭层钥匙与时间",
        "options": [
            ("立刻进入旧馆，寻找B区书架规律", "rule"),
            ("稍作等待，临近6点再进入旧馆", "gate_cleaner")
        ]
    },

    "aunt_blue": {
        "text": "张阿姨回忆了一下说：“2016级有个学生总来借旧馆的书，后来还留下过一本深蓝封面、没有ISBN的书，没人认领就放在B区了”，说完指了指服务台的抽屉。",
        "avatar": "aunt",
        "options": [
            ("询问张阿姨，抽屉里是否有旧馆钥匙", "key_info"),
            ("谢过阿姨，立刻前往旧馆寻找深蓝书籍", "rule_book")
        ]
    },

    "rule_book": {
        "text": "你赶到旧馆B区，书架编号混乱，你想起张阿姨的提示，先梳理书架规律。",
        "options": [
            ("按年代倒序整理，寻找末尾补号书架", "get_rule"),
            ("直接寻找深蓝封面的书籍", "book_feature")
        ]
    },

    "late_gate": {
        "text": "你做完题赶到旧馆时，已经快傍晚5点半了，管理员正在收拾东西准备换班，门口的学长已经离开了，只留下一张写着“银杏书签”的纸条。",
        "options": [
            ("主动上前，询问管理员能否进入B区封闭层", "miss_time"),
            ("躲在一旁，等管理员换班时寻找钥匙", "key_info"),
            ("先进入旧馆，快速寻找书架规律", "rule")
        ]
    },

    # ===== 关键节点：书架规律（线索1，仅记录）=====
    "rule": {
        "text": "你进入旧馆找到B区，发现书架编号混乱不堪，有的标着年份，有的标着数字，完全没有规律可循，这时你想起了张阿姨/馆藏指南的提示。",
        "options": [
            ("按年代倒序整理，寻找末尾补号书架", "get_rule"),
            ("忽略年份标记，按数字顺序翻找", "wrong_rule")
        ]
    },

    "get_rule": {
        "text": "你按照年代倒序梳理书架，果然发现了末尾补号的规律（同年代书籍用数字补号区分），很快锁定了目标书架区域。\n你注意到目标区域旁边有一扇带锁的小门，门上方贴着“封闭层，非管理员禁止入内”的标识（这正是馆藏指南/张阿姨提到的封闭层）。",
        "clue": "旧馆B区书架排列规律",
        "options": [
            ("继续寻找绝版书特征", "book_feature"),
            ("先去确认封闭层钥匙信息", "key_info"),
            ("直接前往封闭层，准备最终确认", "closed")
        ]
    },

    "wrong_rule": {
        "text": "你按数字顺序翻找了半天，只找到了一些普通旧书，完全没有头绪，浪费了大量时间。",
        "options": [
            ("重新回忆提示，按年代倒序寻找", "rule"),
            ("放弃梳理，先去确认钥匙信息", "key_info"),
            ("随便拿一本深蓝书离开", "wrong_book")
        ]
    },

    # ===== 关键节点：绝版书特征（线索2，仅记录）=====
    "book_feature": {
        "text": "你在目标书架上找到了几本深蓝封面的书，有的有ISBN编号，有的没有，还有的夹着普通书签，这时你想起了借阅笔记上的提示。",
        "options": [
            ("严格筛选：无ISBN+夹着银杏书签", "get_book"),
            ("懒得筛选，随便拿一本深蓝封面的书", "wrong_book")
        ]
    },

    "get_book": {
        "text": "你仔细筛选后，找到了一本完全符合条件的书：深蓝封面、无ISBN编号、书中还夹着一枚干枯的银杏书签。",
        "clue": "绝版书外观特征",
        "options": [
            ("先去获取封闭层钥匙信息", "key_info"),
            ("带着这本书，直接前往封闭层", "closed")
        ]
    },

    # ===== 关键节点：钥匙与时间（线索3，仅记录）=====
    "key_info": {
        "text": "你从保洁阿姨/张阿姨口中得知：封闭层的钥匙藏在服务台抽屉下方的暗格里，只有傍晚6点管理员换班时，暗格才会解锁。",
        "clue": "封闭层钥匙与时间",
        "options": [
            ("立刻返回旧馆B区，确认绝版书特征", "book_feature"),  # 补充连贯选项
            ("立刻前往封闭层，准备最终抉择", "closed"),
            ("稍作等待，确保暗格解锁后再去封闭层", "closed_safe")
        ]
    },

    "closed_safe": {
        "text": "你等到傍晚6点，确认管理员换班后，成功从服务台暗格拿到钥匙，前往旧馆B区封闭层。",
        "options": [
            ("进入封闭层，进行最终抉择", "closed")
        ]
    },

    "miss_time": {
        "text": "你犹豫了半天，等赶到服务台时，已经过了6点，管理员已经换班离开，暗格重新上锁。",
        "options": [
            ("接受现实，遗憾离开图书馆", "end_time"),
            ("不死心，返回B区再找其他线索", "rule"),
            ("尝试强行打开封闭层", "closed")
        ]
    },

    # ===== 最终节点：封闭层抉择（唯一结局判定点）=====
    "closed": {
        "text": "你成功获取钥匙，打开了B区深处那扇带锁的小门——这就是你之前在书架旁看到的封闭层。\n封闭层里只有一个书架，书架上放着两本书：一本是深蓝封面、无ISBN、夹着银杏书签，另一本是深蓝封面、有ISBN、夹着普通书签。",
        "image": "closed",
        "options": [
            ("选择：银杏书签+无ISBN的那本", "judge_perfect"),
            ("选择：普通书签+有ISBN的那本", "end_wrong_book")
        ]
    },

    # ===== 普通结局节点 =====
    "wrong_book": {
        "text": "你拿着随便选的深蓝书，走出旧馆才发现，这只是一本普通的旧小说，并不是你要找的绝版书。",
        "options": [("确认结局", "end_wrong_book")]
    }
}

# ===============================
# 剧情展示函数
# ===============================
def show(node):
    avatar_frame.pack_forget()
    illu_frame.pack_forget()

    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, story[node]["text"])
    text_box.see(tk.END)
    text_box.config(state="disabled")

    if "clue" in story[node]:
        add_clue(story[node]["clue"])

    # 显示NPC头像
    if "avatar" in story[node]:
        avatar_path = IMG[story[node]["avatar"]]
        avatar_img = load_img(avatar_path, 80, 80)
        if isinstance(avatar_img, str):
            avatar_label.config(text=avatar_img, image="")
        else:
            avatar_label.config(image=avatar_img, text="")
            avatar_label.image = avatar_img  # 保留引用
        avatar_frame.pack(side=tk.LEFT, padx=8, pady=5)

    # 显示剧情插画
    if "image" in story[node]:
        illu_path = IMG[story[node]["image"]]
        illu_img = load_img(illu_path, 200, 150)
        if isinstance(illu_img, str):
            illu_label.config(text=illu_img, image="")
        else:
            illu_label.config(image=illu_img, text="")
            illu_label.image = illu_img  # 保留引用
        illu_frame.pack(side=tk.RIGHT, padx=8, pady=5)

    # 生成选项按钮
    for w in btn_inner.winfo_children():
        w.destroy()

    for text, nxt in story[node]["options"]:
        b = tk.Button(
            btn_inner, text=text, bg=BTN_BG, width=45, height=2,
            command=lambda n=nxt: navigate(n)
        )
        b.pack(pady=2, padx=10)
        b.bind("<Enter>", lambda e, b=b: b.config(bg=BTN_HOVER))
        b.bind("<Leave>", lambda e, b=b: b.config(bg=BTN_BG))

# ===============================
# 结局判断区域
# ===============================
def navigate(node):
    """简化结局逻辑，正确选书即触发完美结局"""
    if node == "judge_perfect":
        # 显示完美结局+插画
        show_perfect_ending()
    elif node == "end_wrong_book":
        end("😔 普通结局：选错书籍",
            "你拿起那本书，翻了半天才发现，它虽然看起来相似，但并不是绝版书，只是一本普通的旧书。",
            None)
    elif node == "end_time":
        end("😔 普通结局：错过时间",
            "管理员已经换班离开，封闭层再次上锁，你只能带着遗憾离开图书馆。",
            None)
    else:
        show(node)

def show_perfect_ending():
    """单独处理完美结局，确保插画正常显示"""
    # 清空剧情区，显示完美结局文本
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    perfect_text = "✨ 完美结局 ✨\n\n你成功找到了真正的绝版文学书！\n翻开书页，一张泛黄的纸条掉了出来，上面写着：“如果你能看到这句话，说明你真的很认真——2016级 某位学长”。"
    text_box.insert(tk.END, perfect_text)
    text_box.config(state="disabled")

    # 加载并显示完美结局插画
    illu_path = IMG["perfect_end"]
    illu_img = load_img(illu_path, 200, 150)
    if isinstance(illu_img, str):
        illu_label.config(text=illu_img, image="")
    else:
        illu_label.config(image=illu_img, text="")
        illu_label.image = illu_img  # 强制保留图片引用
    illu_frame.pack(side=tk.RIGHT, padx=8, pady=5)  # 强制显示插画区域

    # 清空按钮，显示重新开始
    for w in btn_inner.winfo_children():
        w.destroy()

    restart_btn = tk.Button(
        btn_inner, text="重新开始游戏", bg=BTN_BG, width=40, height=2,
        command=restart
    )
    restart_btn.pack(pady=30)
    restart_btn.bind("<Enter>", lambda e: restart_btn.config(bg=BTN_HOVER))
    restart_btn.bind("<Leave>", lambda e: restart_btn.config(bg=BTN_BG))

def end(title, text, img_key):
    """结局展示函数"""
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, f"{title}\n\n{text}")
    text_box.config(state="disabled")

    # 显示插画（若有）
    if img_key:
        illu_path = IMG[img_key]
        illu_img = load_img(illu_path, 200, 150)
        if isinstance(illu_img, str):
            illu_label.config(text=illu_img, image="")
        else:
            illu_label.config(image=illu_img, text="")
            illu_label.image = illu_img
        illu_frame.pack(side=tk.RIGHT, padx=8)
    else:
        illu_frame.pack_forget()

    # 清空按钮，显示重新开始
    for w in btn_inner.winfo_children():
        w.destroy()

    restart_btn = tk.Button(
        btn_inner, text="重新开始游戏", bg=BTN_BG, width=40, height=2,
        command=restart
    )
    restart_btn.pack(pady=30)
    restart_btn.bind("<Enter>", lambda e: restart_btn.config(bg=BTN_HOVER))
    restart_btn.bind("<Leave>", lambda e: restart_btn.config(bg=BTN_BG))

def restart():
    """重置游戏状态+清空图片缓存"""
    global clues, img_cache
    clues = set()
    img_cache = {}  # 重置图片缓存，避免重复加载异常
    clue_box.config(state="normal")
    clue_box.delete(1.0, tk.END)
    clue_box.config(state="disabled")
    show("start")

# ===============================
# 启动游戏
# ===============================
if __name__ == "__main__":
    show("start")
    root.mainloop()
