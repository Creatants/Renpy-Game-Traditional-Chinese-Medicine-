# 游戏的脚本可置于此文件中。
#{size=45}{/size};{color=}{/color}:{alpha=0.5}{/alpha};{font}{/font};{b}{/b};{i}{/i};{a}{/a}:{a=jump\call:nihao}{/a};{image=lujing}{/image}
#junmp nihao ;   label nihao:  return; call nihao;

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define config.gl2 = True
define A = Character("南烛", what_size=25,who_size=30,who_color="#ccffeb",who_outlines = [(1, "#ccffeb", 0, 0)],what_prefix="【",what_suffix="】")
define B = Character("华佗",what_size=25,who_size=30,who_color="#fffdcc",who_outlines = [(1, "#fffdcc", 0, 0)],what_prefix="【",what_suffix="】")
define C = Character("系统",what_size=25,who_size=30,who_color="#ccffde",who_outlines = [(1, "#ccffde", 0, 0)],what_prefix="【",what_suffix="】")
define D = Character("患者",what_size=25,who_size=30,who_color="#ffcce0",who_outlines = [(1, "#ffcce0", 0, 0)],what_prefix="【",what_suffix="】")
define E = Character("明溪",what_size=25,who_size=30,who_color="#ccffde",who_outlines = [(1, "#ccffde", 0, 0)],what_prefix="【",what_suffix="】")
define F = Character("老妇人",what_size=25,who_size=30,who_color="#ccffde",who_outlines = [(1, "#ccffde", 0, 0)],what_prefix="【",what_suffix="】")
define G = Character("孙思邈",what_size=25,who_size=30,who_color="#ccffde",who_outlines = [(1, "#ccffde", 0, 0)],what_prefix="【",what_suffix="】")
define H = Character("伙计",what_size=25,who_size=30,who_color="#ccffde",who_outlines = [(1, "#ccffde", 0, 0)],what_prefix="【",what_suffix="】")
define I = Character("李时珍",what_size=25,who_size=30,who_color="#ccffde",who_outlines = [(1, "#ccffde", 0, 0)],what_prefix="【",what_suffix="】")
define config.say_attribute_transition = dissolve

#ctc
#define B = Character("华佗",image="eileen happy"，ctc="ctc",ctc_position="nestled")
#image ctc = "images/''''"
define X = 0

init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("images/序幕/转场/eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("images/序幕/转场/eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
image hei:
    Solid("#000")
image white:
    Solid("#FFF")
#头像
#image side eileen happy  = ""
#image side eileen happy b = ""
#image side eileen happy c = ""
#B c ""
#头像人物同时变
#image  eileen happy  = ""
#image  eileen happy b = ""
#image  eileen happy c = ""
image bg_family:
    "images/序幕/背景/全家福.png"
    size(1280,720)
image bg_work:
    "images/序幕/背景/上班生活.png"
    size(1280,720)

image bg_daxue:
    "images/序幕/背景/校园.png"
    size(1280,720)

image bg_station:
    "images/序幕/背景/列车站台.png"
    size(1280,720)
image 列车穿森林:
    "images/序幕/背景/列车穿梭.png"
    size(1280,720)
image 风景:
    "images/序幕/背景/夕阳.png"
    size(1280,720)
image black:
    contains:
        "images/序幕/人物/1.jpg"
        size(640,360)
        topleft
    contains:
        "images/序幕/人物/2.jpg"
        size(640,360)
        topright
    contains:
        "images/序幕/人物/3.jpg"
        size(640,360)
        left
    contains:
        "images/序幕/人物/3.1.jpg"
        size(640,360)
        right
image fm:
    contains:
        "images/序幕/人物/1.jpg"
        size(640,360)
        topleft
    contains:
        "images/序幕/人物/2.jpg"
        size(640,360)
        topright
    contains:
        "images/序幕/人物/3.jpg"
        size(640,360)
        left
    contains:
        "images/序幕/人物/3.1.jpg"
        size(640,360)
        right

image 列车内部:
        "images/序幕/背景/列车内部.png"
        size(1280,720)

image 列车停靠:
        "images/序幕/背景/列车停靠.png"
        size(1280,720)
image 列车关门:
        "images/序幕/背景/列车关门.png"
        size(1280,720)


image 林间小道:
        "images/序幕/背景/林间小道.png"
        size(1280,720)

image 小路尽头:
        "images/序幕/背景/小路尽头.png"
        size(1280,720)

image village:
        "images/序幕/背景/village.png"
        size(1280,720)

image 科技感村庄:
        "images/序幕/背景/系统_village.png"
        size(1280,720)
image 科技感列车:
        "images/序幕/背景/系统_列车.png"
        size(1280,720)   

image 村路:
        "images/华佗篇/村路.png"
        size(1280,720)  
image 村路2:
        "images/华佗篇/村路2.png"
        size(1280,720)   
image 村路和华佗:
        "images/华佗篇/村路和华佗.png"
        size(1280,720)  
image 茅草屋:
        "images/华佗篇/茅草屋.png"
        size(1280,720) 
image 茅草屋内:
        "images/华佗篇/茅草屋内.png"
        size(1280,720) 
#孙思邈篇背景
image 农田:
        "images/孙思邈篇/列车停靠在田野.png"
        size(1280,720) 
image 常州街道:
        "images/孙思邈篇/常州街道.png"
        size(1280,720) 
image 常州街道系统:
        "images/孙思邈篇/常州街道_系统.png"
        size(1280,720) 
image 人群屠苏庵:
        "images/孙思邈篇/人群屠苏庵.jpg"
        size(1280,720) 
image 屠苏庵屋外:
        "images/孙思邈篇/屠苏庵屋外.png"
        size(1280,720) 
image 屠苏庵:
        "images/孙思邈篇/屠苏庵.png"
        size(1280,720) 
image 野猪农田:
        "images/孙思邈篇/野猪农田.jpg"
        size(1280,720) 
#李时珍篇背景
image 明代村庄:
        "images/李时珍篇/村庄.png"
        size(1280,720) 
image 明代村庄科技:
        "images/李时珍篇/明代村庄科技.png"
        size(1280,720) 
image 江南水乡:
        "images/李时珍篇/江南水乡.png"
        size(1280,720) 
image 江南水乡2:
        "images/李时珍篇/江南水乡2.png"
        size(1280,720) 
image 人群:
        "images/李时珍篇/人群.png"
        size(1280,720) 
image 山林:
        "images/李时珍篇/山林.png"
        size(1280,720) 
image 屋子:
        "images/李时珍篇/屋子.png"
        size(1280,720) 
image 药房:
        "images/李时珍篇/药房.png"
        size(1280,720) 
image 系统药房:
        "images/李时珍篇/系统药房.jpg"
        size(1280,720) 
image 山林2:
        "images/序幕/背景/风景1.png"
        size(1280,720) 
#第一次融合
#这里是人物（华佗篇及其之前）
image 华佗正常:
        "images/华佗篇/人物/华佗正常.png"
        size(600,600)
image 华佗正常左:
        "images/华佗篇/人物/华佗正常左.png"
        size(600,600)
image 华佗微笑:
        "images/华佗篇/人物/华佗微笑.png"
        size(600,600)
image 华佗微笑左:
        "images/华佗篇/人物/华佗微笑左.png"
        size(600,600)
image 患者生病:
        "images/华佗篇/人物/老人.png"
        size(600,600)
image 患者放松:
        "images/华佗篇/人物/患者放松.png"
        size(600,600)
image 患者热泪盈眶:
        "images/华佗篇/人物/患者流泪.png"
        size(600,600)
image 现代1:
        "images/序幕/人物/现代1.png"
        size(600,600)
    
image 现代惊讶:
        "images/序幕/人物/现代_惊讶.png"
        size(600,600)
image 现代打哈欠:
        "images/序幕/人物/现代打哈欠.png"
        size(800,800)

image 汉服吃惊:
        "images/序幕/人物/汉服3.png"
        size(600,600)

image 汉服劳累惶恐:
        "images/序幕/人物/汉服4.png"
        size(600,600)
image 汉服饿了:
        "images/序幕/人物/汉服_饿了.png"
        size(600,600)
image 汉服微笑:
        "images/序幕/人物/汉服1.png"
        size(600,600)
image 汉服正常:
        "images/序幕/人物/汉服2.png"
        size(600,600)  
image 汉服下定决心:
        "images/序幕/人物/汉服下定决心.png"
        size(600,600)  
image 汉服大惊失色:
        "images/序幕/人物/大惊失色.png"
        size(600,600) 
image 汉服十分震惊:
        "images/序幕/人物/汉服震惊2.png"
        size(600,600)
image 汉服尴尬:
        "images/序幕/人物/汉服尴尬.png"
        size(600,600)
image 汉服犹豫:
        "images/序幕/人物/汉服犹豫.png"
        size(600,600)
image 汉服想跑:
        "images/序幕/人物/汉服想跑.png"
        size(600,600)
image 现代正常:
        "images/序幕/人物/现代_惊讶.png"
        size(600,600)
#孙思邈篇人物
image 唐惊讶:
        "images/孙思邈篇/人物/唐惊讶.png"
        size(600,600)
image 唐眯眼笑:
        "images/孙思邈篇/人物/唐眯眼笑.png"
        size(600,600)
image 唐微笑:
        "images/孙思邈篇/人物/唐微笑.png"
        size(600,600)
image 唐疲惫:
        "images/孙思邈篇/人物/唐疲惫.png"
        size(600,600)
image 老妇人:
        "images/孙思邈篇/人物/老妇人.png"
        size(600,600)
image 孙思邈:
        "images/孙思邈篇/人物/孙思邈.png"
        size(600,600)
#李时珍篇人物篇
image 李时珍:
        "images/李时珍篇/人物/李时珍.png"
        size(480,600)
image 明惊讶:
        "images/李时珍篇/人物/惊讶.png"
        size(600,600)     
image 明难过:
        "images/李时珍篇/人物/难过.png"
        size(600,600)      
image 明疲惫:
        "images/李时珍篇/人物/疲惫.png"
        size(600,600) 
image 明微笑:
        "images/李时珍篇/人物/微笑.png"
        size(600,600)  
image 明笑容:
        "images/李时珍篇/人物/笑容.png"
        size(600,600)      


#华佗
# image 华佗正常:
#         "images/华佗篇/人物/华佗正常.png"
#         size(600,600)
#孙思邈篇的内容放这里！
label start:


    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    play music "<from 20.0>music/bg_start_wanan.mp3" volume 0.5 
    scene bg_family 
    with fade      #我的名字是祖父给我起的，取自《本草拾遗》中的“南烛生高山，经冬不凋”，寄托着家中长辈对我将中医传承发扬下去的殷切期望。
    """
    我叫南烛，出生于一个中医世家。
    """
    """
    也许是家庭环境的熏陶，从小我对中医药就抱有浓厚的兴趣。自然而然的，高考报志愿时选择了一所中医药大学。
    """
    scene bg_daxue
    with fade
    """
    上大学后，我感受到了前所未有的迷茫。
    """
    """
    很多学长毕业后选择了与中医药毫不相干的企业或单位，而周围的许多同学们也在为以后可以去大公司而努力。
    """
    """
    似乎，大企业那里的“前途”更加广阔。
    """
    scene bg_work
    with fade
    """
    今年我已经大三了，因为对未来充满茫然，我还是选择了去一家互联网企业实习。
    """
    """
    每天枯燥且繁重的工作压得我喘不过气。
    不禁让我思考：这真的是我想要的生活吗？
    """
    """
    完成了一天的工作，终于迎来了梦寐以求的一个小长假。
    """
    scene bg_station
    with fade
    
    A """
    终于放假了，可以好好休息休息。想起来好久都没有回家了，还是回家看看吧。
    """
    """
    虽然很疲倦，但对家人的思念更加无法抑制。第二天一大早我便踏上了回家的路。
    """
    scene 列车内部
    with fade

    "奇怪的是，直到列车开动，整个车厢里只有我一人。"

    #show 1 
    show 现代惊讶 
    play sound "music/train01_4loop.mp3" volume 0.15  
    with dissolve

    A "咦？是因为太早了吗？"
    A "先不管了，可能到下一站就会有人吧。"

    
    hide 现代惊讶
    with fade

    "一段时间后......"
    
    show 现代打哈欠 
    with dissolve  
    play audio "music/打哈欠.wav" volume 0.3
    stop audio
    stop sound
    play sound "music/train01_4loop.mp3" volume 0.15 
    A """
    啊～～好困啊，果然还是起太早了，先睡一会吧。
    """
      
    hide 现代打哈欠  
    
    scene hei
    with eye_shut
       
    "我闭眼小憩了一会儿，不知过了多久 ，列车播报的声音响起。"
    
    stop sound    
    play audio "music/叮咚.wav" volume 0.3   
    "列车已到站，请乘客们收拾好随身物品，有序下车。"
    scene 列车内部
    with eye_open
    stop audio    
    A"""
    这么快就到了吗？
    """

    "虽然有些惊讶，但在意识朦胧间我已经走出了列车......"

    #此处换背景
    scene 列车停靠
    with dissolve

    stop sound
    stop music
    play music "music/bg_start_xiehou.mp3" volume 0.3
    play sound "<to 1>music/bird.mp3" volume 0.2

    """
    下车后映入眼帘的的不是列车站台的场景，而是一片茂密且寂静的树林！
    """

    """
    还有一条蜿蜒曲折的小路不知道通向哪里。
    """
    
    stop sound
    show 汉服正常
    with dissolve 
    """
    #甚至我身上的外套也不知何时变成了直裾之衣！
    """ 
    scene 列车关门 
    show 汉服正常
    play sound "<from 2>music/列车关门声音ID_36981.wav" volume 0.5 
    hide 汉服正常
    show 汉服吃惊 
    A "这是怎么回事？！这是哪儿？"
    A "欸？我的衣服！"       
    "我突然清醒过来，并意识到在自己身上发生了奇怪的事情。"     
    
    "但面对未知，一种恐惧感油然而生，我下意识地便想回到列车里。"     
    "但很不巧，不知什么原因，列车的门被紧紧关住了。"
    stop sound 
    hide 汉服吃惊 
    show  汉服劳累惶恐       
    with dissolve
    A "我该怎么办？"  
    call xuanze1
    scene 林间小道
    play sound "music/走路_作者_柏语涵.mp3" volume 0.5
    "迫于无奈，我只好沿小路往树林深处中走去。"
    "......"   
    stop sound
    scene 小路尽头
    with fade
    "走了好些距离以后..."    
    show 汉服吃惊 at left
    with dissolve
    A"远处的视线开阔起来了，会不会有人家？"    
    """
    意识到这一点的我不禁加快了脚步。
    """   
    play sound "music/快步行走声音ID15082.wav" volume 0.5    
    hide 汉服吃惊
    stop sound
    """
    ......
    """
    """
    终于穿过了树林，一切都变得豁然开朗。
    """
    scene village
    with dissolve
    """
    远处层层叠叠的好像是一些茅草屋。
    """
    show 汉服正常
    A"这里看起来像是一个村庄。"    
    A"看起来村子里还有挺多人，赶快去问问这是什么情况吧。"
    hide 汉服正常
    play sound "music/走路_作者_柏语涵.mp3" volume 0.2   

    show 汉服劳累惶恐 
    stop sound
    with dissolve  
    A "呼......好累！"
    A "明明这么靠近村庄，怎么这一路没有遇到一个人。"
    
    scene 科技感村庄
    with dissolve
    """
    正当我十分疑惑时，面前突然出现了一个蓝色的系统界面。
    """
      
    play music "music/雨夜.mp3" volume 0.15
    play sound "<from 0.8>music/系统激活ID32285.mp3" volume 0.4

    #插入音效——系统
    C "欢迎您来到东汉末年！"
    stop sound
    hide 汉服劳累惶恐
    show 汉服吃惊 at left
    with dissolve  
    play sound "music/震惊声音ID17779.wav"    volume 0.4
    C "南烛，很高兴见到你。"
    call talk_xt_and_cz
    A "你是谁？这里是哪？这一切都是真的吗！"
    """
    这魔幻的一切来得太过突然，以至于我不敢相信它的真实性。
    """
    C "请不要着急，我会逐个回答你的问题。"
    C "我是你的专属系统，你可以叫我<明溪>"
    hide 汉服正常 at left
    show 汉服吃惊 at left
    with dissolve
    A "<明溪>,你能告诉我这里是哪里吗？"
    E "这里是东汉时期的一个小村庄。"
    A "哈？！"
    hide 汉服吃惊 at left
    show 汉服十分震惊 at left
    with dissolve
    A "东汉？！ 我没有听错吧，这一定是在做梦。"
    E "南烛，请你冷静,难道你不想回家吗？"
    hide 汉服十分震惊 at left
    show 汉服正常 at left
    with dissolve
    """
    听到这里，我逐渐在震惊中回过神来。
    """
    A "那我应该怎么做？"

    E "如果要回到原来的世界，你就必须完成两项任务。"

    A "什么任务？"

    E "第一个任务。"
    E "任务背景：东汉末年，神医华佗凭一己之力攻克了让其他医师都束手无策的黄疸病，从而名震中原。"
    E "现在华佗就在这个村子里，而你的任务就是协助他治疗黄疸病。"
    E "进入村庄将会自动接取任务。"
    E "系统提示结束。"
    scene village
    show 汉服正常 at left
    with dissolve   
    """
    浮现在眼前的系统界面也随着<明溪>说完最后一句话而消失不见。
    """
    hide 汉服正常 at left 
    show 汉服劳累惶恐 at left
    with dissolve
    A "欸？<明溪>你还在吗？"
    """
    ......
    """
    A "这就消失了？"
    """
    也许是今天经历的奇怪的事情太多，对于<明溪>的突然消失，我并没有表现出多大的震惊。
    """
    hide 汉服劳累惶恐 at left
    show 汉服犹豫
    with dissolve
    call 任务one_start
    show 汉服劳累惶恐
    with dissolve
    A "进去看看吧。"
    scene 村路
    with fade
    play sound "music/叮咚.wav"  volume 0.5
    E "任务已接取。"    
    """
    伴随着进入村庄，一直忐忑的心逐渐恢复平静。
    """
    """
    也许是从未有过这种体验，我开始四处打量周围的环境。
    """
    show 汉服劳累惶恐 at left
    with dissolve  
    """
    这里环境贫瘠，偶尔路过的村民大都貌似蜡黄。
    """
    """
    旁边的破旧茅草屋中隐隐还传出病人在病魔折磨下发出的痛苦的呻吟声。
    """
    """
    看到此情此景，难过与心痛不知什么时候悄悄涌上心头，不安与紧张让我攥紧了拳头。
    """
    scene 村路和华佗
    with fade
    show 汉服劳累惶恐 at left
    with dissolve
    A "那里好像有人。"
    """
    渐渐的，远处一位衣着朴素、头顶布巾的老人出现在了我的视线中。
    """
    scene 村路2
    play sound "music/砾石上走路声音ID0150.wav"  volume 0.4
    show 汉服劳累惶恐 at left
    show 华佗正常 at right
    with dissolve
    """
    等他走近后我发现，他头发斑白，面带疲惫，仿佛因为长时间的劳累脸上浮现出几分憔悴。
    """
    stop sound
    call meethuatuo     
    E "这位老人就是我们要找的华佗神医。华佗，字元化，沛国谯(今安徽省亳州市)人。"
    hide 汉服微笑 at left
    show  汉服吃惊 at left
    with dissolve
    """
    原来他就是神医华佗，和古书里有几分神似呢。
    """
    hide 汉服吃惊 at left
    show  汉服微笑 at left
    with dissolve
    A "华佗神医，久仰久仰。"     
  
    B "这位小友谬赞了，神医称不上，我不过是一位普通医师罢了。"
    hide 汉服微笑 at left
    show  汉服正常 at left
    with dissolve
    A "您这是要......"
    play sound "music/叹气唉声音ID39094.wav" volume 0.5
    """
    神医长长地叹了口气。
    """
    B "近日来，此地百姓多发黄疸病，但是此病难治，众多大夫都对它束手无策。"
    stop sound
    B "看看这里的百姓，遭受了多少磨难呀。"
    hide 汉服正常 at left
    show 汉服劳累惶恐 at left
    with dissolve
    """
    听到这里，我的鼻子不禁一酸。
    """  
    """
    这一路走过来，荒芜的土地、奄奄一息的村民、痛苦的呻吟......这些无时无刻不刺激着我的神经。
    """
    """
    现世的人们有着先进的医疗手段都难逃病痛的折磨，更何谈是千百年前的古人。
    """
    B "我既然身为大夫，便立志要行医济世，解救百姓于水深火热之中。"
    B "于是我特地赶来此处，只为解救深受黄疸病折磨的病人们。"
    hide 汉服劳累惶恐 at left
    show 汉服吃惊 at left
    with dissolve
    A "此行定当万分艰难！"

    B "困难与挫折是必然的，但不能眼睁睁看着百姓受苦，总得有人去做。"
    """
    他的脸上虽然布满疲惫，却难以遮掩眼神中的坚定。
    """
    """
    我不由感叹道：医者仁心啊！
    """
    hide 汉服吃惊 at left
    show 汉服微笑 at left
    with dissolve
    A "先生胸怀天下，晚辈十分钦佩。"
    A "刚好我也略懂一些这方面的道理，不知是否能帮助到先生，为百姓摆脱疾苦献一份绵薄之力？"
    """
    神医没有立即答应，而是先对我上下打量一番。
    """
    B "治病行医万不得马虎，在此之前我得考你几个问题。"
    hide 汉服微笑 at left
    show 汉服正常 at left
    with dissolve
    A "先生请说。"
    hide 汉服正常 at left
    call 华佗出题
    scene 村路2
    show 汉服正常 at left
    show 华佗正常 at right
    hide 汉服正常 at left
    hide 华佗正常 at right
    show 汉服微笑 at left
    show 华佗微笑 at right
    B "不错，你通过了我的考验。"
    hide 汉服微笑 at left
    show 汉服正常 at left
    with dissolve
    A "晚辈受教了。"
    hide 华佗微笑 at right
    show 华佗正常 at right
    with dissolve
    B "实不相瞒，经过多次的寻找和实验，我终于找到了一种可以对黄疸病进行控制治疗的药材。"
    hide 汉服正常 at left
    show 汉服吃惊 at left
    with dissolve
    A "哦？"
    B "这味药材就是茵陈蒿。据我研究发现，茵陈蒿的嫩叶可以使得病人的病情得到快速地控制。"
    B "当病情得到控制后，再通过煮汤的方式每日几次对患者送服，那么患者的黄疸病就会明显好转。"
    B "但是由于材料有限，我前些时间获取的茵陈蒿已经用完了。"
    B "不知道能不能请这位小友帮忙上山采摘一些茵陈蒿的嫩叶来。"
    hide 汉服吃惊 at left
    show 汉服微笑 at left
    with dissolve
    A "您放心好了，包在我身上！"
    hide 华佗正常 at right
    hide 汉服微笑 at right
    with dissolve
    show 汉服劳累惶恐
    with dissolve
    A "虽然我一口答应下来帮神医去采药，但是对采药却没什么头绪。"
    
    #此处可插入视频
    E "茵陈蒿，菊科蒿属的半灌木状草本植物，植株有浓香；茎直立，基部木质化。"
    E "初时密生灰白色或灰黄色绢质柔毛，后渐稀疏或脱落无毛；花黄色；瘦果长圆形；花果期为秋季。"
    E "茵陈蒿经冬不死，春则因陈根而生，故名因陈或茵陈，至夏其苗则变为蒿，亦称茵陈蒿，故有“三月茵陈，四月蒿，五月当柴烧”的说法。"
    E "茵陈蒿生于路旁、河边、海滨沙地、低山坡较潮湿处；耐寒，喜光，生长强健；对土壤要求不高，尤耐盐碱。茵陈蒿繁殖采用播种繁殖或分株繁殖。"
    E "请帮助华佗找出以下植株中哪株是茵陈蒿吧。"
    call game1
   
    hide 汉服劳累惶恐
    with dissolve

    show 汉服正常 at left:
    with dissolve  
    A "先生，这些是我所采的茵陈蒿，您看看？"
    show  华佗正常 at right
    with dissolve
    B "正是。辛苦小友帮我采集茵陈蒿,在此特意谢过。"
    hide 汉服正常 at left
    show 汉服微笑 at left
    with dissolve
    A "先生不必客气，能帮到你我也很高兴！"
    A "当务之急，快嫩叶摘下来煮汤给患者服用吧。"
    """
    神医微微颔首。
    """
    scene hei
    with fade
    """
    在一番准备过后......
    """
    scene 村路2
    with fade
    hide 汉服微笑 at left
    with dissolve
    hide 华佗正常  right
    with dissolve    
    show 汉服正常 at left
    with dissolve
    "药汤煮好了。"
    A "前辈，药汤煮好了。"
    "我协助华佗将汤水盛到碗中"
    show 华佗正常 at right
    with dissolve
    B "小兄弟，与我一同去给病患送药吧。"
    hide 汉服正常 at left
    show 汉服微笑 at left
    with dissolve
    A "好~"
    scene 茅草屋
    with fade 
    play sound "music/男人呻吟声音ID39086.wav" volume 0.5
    """
    刚走到一个茅草屋门口，一阵呻吟声传入耳中。
    """
    stop sound
    show 汉服吃惊 at left
    with dissolve
    """
    透过半掩着的门，我看到一个老者躺在床上通身发黄，腹部微涨。时不时发出干呕的声音，看起来十分难受。
    """
    show  患者生病 at right
    with dissolve
    D "求求你们......救救我吧。"
    """
    听到这里，我们急忙走进屋去。
    """
    hide 汉服吃惊 at left
    scene 茅草屋内
    show 患者生病 at right
    show  华佗正常左  at left
    with dissolve
    B "你别担心，这是能缓解病症的药汤，快将它服下。"
    play sound "music/喝水声音ID13132.wav" volume 0.5
    """
    老人很快将汤药服下。
    """
    D "谢谢你们。"
    hide 患者生病 at right
    stop sound
    scene 茅草屋
    with dissolve
    """
    我们帮助他躺好，叮嘱他好好休息后，便去给其他村民分发汤药。
    """
    scene 村路2
    with fade
    """
    我已经全然忘记了饥饿和劳累，只希望这些药能减轻村民们的一丝痛苦。
    """
    show 汉服劳累惶恐 at left
    with dissolve
    A "由衷希望世间所有人不再受病痛困扰。"
    show 华佗正常 at right
    with dissolve
    B "我们也当为此努力，哪怕是只帮助一个人。"
    hide 汉服劳累惶恐 at left
    show 汉服微笑 at left
    with dissolve
    A "嗯！"
    scene 茅草屋
    with fade
    """
    接连发放了几天药汤后，我们又停留在了最开始那个茅草屋前。
    """
    show 汉服吃惊 at left
    with dissolve
    A "不知道那个爷爷好些了吗？"
    call 进屋探望

    scene 茅草屋内
    with fade
    show 汉服微笑 at left
    with dissolve
    A "老人家，有没有感觉舒服一点？"
    show 患者放松 at right
    with dissolve
    D "感觉好受多了，感谢两位的救命之恩呀！"
    hide 汉服微笑 at left
    show 华佗正常左 at left
    with dissolve
    B "接下来还需继续服用此药，这样你的病症才会慢慢消退。"
    B "你放心，我会将煮药汤的草药留下给你，你按我的方子去煎服即可。"
    hide 患者放松 at right
    show 患者热泪盈眶 at right
    with dissolve
    D "太感谢医士了！要不是您我恐怕已经..."
    """
    说着说着老人家眼角泛出了泪花。
    """
    B "不必多谢，治病救人是身为医者应该做的。"
 
    scene 村路2
    with fade
    """
    渐渐的，村子里的患者病症差不多都已经有了明显好转。
    """
    show 汉服正常 at left
    with dissolve
    """
    我在村庄里独自漫步，回想着这几日发生的一切，有震惊，有心酸，但更多的是感动。
    """
    """
    这时耳边响起了华佗的声音。
    """
    show 华佗正常  at right
    with dissolve
    B "小友，我正找你呢，原来你在这儿。"
    hide 汉服正常 at left
    show 汉服吃惊 at left
    with dissolve
    A "先生，是出什么事了吗，难道村民们的病严重了？"
    hide 华佗正常 at right
    show 华佗微笑 at right
    with dissolve
    B "小友不必紧张，我来寻你只是为了表达感谢！"
    B "这几日真的辛苦你采药，又协助我发放药汤，让这些患者得到及时治疗。"
    hide 汉服吃惊 at left
    show 汉服正常 at left
    with dissolve
    A "先生哪里的话！您夙夜不懈地为百姓治病，令小辈钦佩。"
    """
    先生~
    """
    """
    不远处传来了村民呼唤华佗的声音。
    """
    hide 华佗微笑 at right
    show 华佗正常 at right
    with dissolve
    B "我先去看看发生了什么，再会了小友。" 
    hide 汉服正常 at left
    show 汉服微笑 at left
    with dissolve
    A "好的"
    hide 华佗正常 at right
    with dissolve
    """
    华佗匆匆离开了。
    """
    scene village
    with fade
    """
    不知不觉中，已经走到了山坡处。
    """
    """
    俯瞰着之前死气沉沉的村庄，如今的道路上也有不少来来往往的行人。
    """
    show 汉服正常
    with dissolve
    """
    华佗前辈的仁心与医术拯救的是多少个家庭呀！
    """
    hide 汉服正常
    show 汉服微笑
    with dissolve
    """
    我闭上眼睛感受风拂过脸颊，全神贯注感受心底泛出的喜悦。
    """
    scene hei
    with eye_shut
    play sound "music/叮咚.wav" volume 0.5
    E "任务完成。" 
    """
    听到了<明溪>熟悉的声音，我赶快睁开了眼睛。
    """  
    scene 科技感列车
    with eye_open
    """
    眼前的情景让我有些猝不及防。
    """
    show 现代正常
    with dissolve
    A "我怎么一瞬间就在车上了？？？"
    E "恭喜你完成第一个任务。"
    hide 现代正常
    show 现代打哈欠
    with dissolve
    A "<明溪>，你倒是让我放松一下呀。"
    hide 现代打哈欠
    show 现代正常
    with dissolve
    E "南烛，很高兴你能对那些村民产生巨大的同情与关怀,也很感谢你不畏劳苦献出自己的一份力量！"
    A "嗯，下意识间就觉得应当如此。"
    E "南烛，善良是一个医者必不可少的品性，你很幸运。"
    E "好好休息一下吧，我们马上就要到下一站了。"
    A "欸？又不见了。"
    hide 现代正常
    scene 列车穿森林
    with fade
    """
    列车徐徐向前开动，穿过森林，不知通向何方。
    """
    scene 风景
    with fade
    """
    窗外的风景是如此动人。
    """
    """
    日光暖洋洋地洒在我的脸上，加上这几日的劳累。我的意识逐渐模糊起来。
    """
    scene hei
    with eye_shut
    """
    章节一，完成。
    """
#孙思邈篇
    scene 列车内部
    with fade   
    play sound "music/叮咚.wav" volume 0.5
    "不知道过了多久，列车播报声再次响起——列车已到站，请乘客收拾好随身物品，有序下车。"
    scene 农田
    with fade
    play music "music/bg_start_xiehou.mp3" volume 0.3
    play sound "music/列车关门声音ID_36981.wav" volume 0.5
    "一片生机勃勃的农田... ..."
    "果不其然，列车门已然关闭。那么，打起精神迎接下一个任务吧！"
    show 唐微笑
    "这里是哪里呀？居然有这么肥沃的农田！建筑很眼熟，唉，早知道历史课好好听了。"
    "哇塞，等等！我的衣服又变了？这件圆领袍像唐朝时期的衣服，这次不会到唐朝了吧。"
    call SFZ1
    stop music
    play music "music/唐代BGM.mp3" volume 0.2
    scene 常州街道#常州繁华街道
    with fade
    play sound "music/嘈杂.wav" volume 0.3
    "远处传来沸沸扬扬的人声，眼前的景象却令我大为惊叹，这里是一条繁华的街市，随处可见叫卖的商贩...正当我沉醉其中时......"
    scene 常州街道系统#科技感街道
    with fade
    stop sound
    play sound "music/叮咚.wav" volume 0.5
    show 唐惊讶 at left
    with dissolve
    "啊？这样大庭广众之下就弹出来了嘛？难道别人看不见？算了，不管这个，要说的话我出现在这本身就已经很荒谬了…"
    A "<明溪>，我已经看过这里的环境了，我记得没错的话是常州吧？好繁华啊！"
    E "是的，欢迎来到唐朝初年！这里是江南地区的常州。"
    call SFZ2
    show 唐微笑 at left
    with dissolve    
    A "<明溪><明溪>"
    scene 常州街道系统#科技感街道
    with fade
    show 唐微笑 at left
    with dissolve 
    E "在的在的"
    A "<明溪>，我这一关的任务是什么？"
    E "唐朝初年，南方时有瘟疫发生，孙思邈在常州这一带夙夜不息地抢救病人，潜心研制出《肘后备急方》中的‘屠苏酒’，才结束了这场瘟疫。"
    E "可是这也导致了人们对屠苏药酒的迷信，屠苏庵日日门庭若市。你的任务就是协助他解决这个问题。"
    hide 唐微笑 at left
    with dissolve  
    show 唐眯眼笑 at left
    with dissolve   
    A "原来如此"
    E "任务接取成功，祝你任务顺利南烛。"
    "孙思邈的事迹我从小就耳熟能详了，他是我很钦佩的古医家之一，上课的时候也只能在课本里看见他的画像，没想到现在我能见到啦！"
    hide 唐眯眼笑 at left
    with dissolve 
    show 唐疲惫  at left
    with dissolve 
    "屠苏药酒只是用来预防和治疗瘟疫的，可不包治百病啊，这样下去不是办法，我可得快点去帮助孙思邈解决这个问题"
    scene 人群屠苏庵 #屠苏庵门口挤满了人
    with fade
    "我穿越繁华的街市，快步向屠苏庵的方向走去。还没走到屠苏庵的门口，就看见门口已经挤满了人。"
    show 唐惊讶
    with dissolve
    "天呐！这么多人都是来要屠苏酒的嘛？这孙思邈神医能招架得住嘛？太可怕了…屠苏酒也不是神药呢，不治百病…怪不得系统把我整这来了。"
    E "这位便是我们要找的医者孙思邈。孙思邈，京兆华原人，唐代医药学家，道士。"
    hide 唐惊讶
    with dissolve
    show 孙思邈
    with dissolve
    "啊啊啊啊啊！对视了！好紧张好紧张，不行，不能这样！南烛啊南烛，你是来完成任务的，还想不想回家了？放松放松，镇定！"
    call SFZ3
    G "哈哈哈哈小友谬赞了，屠苏酒的事情实乃令我疲劳，小友可先等老夫安顿好前来寻求屠苏酒的百姓？"
    hide 唐眯眼笑 at left
    with dissolve
    show 唐微笑 at left
    with dissolve
    A "先生请。"
    scene 人群屠苏庵#屠苏庵门口挤满了人
    with fade
    "于是孙思邈走进屋内令屠苏庵里的伙计去应对前来讨要屠苏酒的百姓们，了了又出来寻到我。"
    show 孙思邈 as sunsimiao at right
    with dissolve
    show 唐微笑 at left
    with dissolve
    G "这位小友可愿随我到书房商议？"
    A "当然愿意，先生。"
    scene 屠苏庵#孙思邈的书房
    "屠苏庵的书房真精致，古色古香，布置妥帖，看得出先生是个精细之人，我得好好想办法为先生解决麻烦，才担得起先生的重视。"
    show 孙思邈 as sunsimiao at right
    with dissolve
    show 唐微笑 at left
    with dissolve
    G "前些时日我将屠苏酒给未得病的人喝，瘟疫便再未发生，屠苏药酒本是滋补保健，防病疗疾的，怎料百姓误会此药酒治疗百病，不管得病与否，日日前来屠苏庵讨要药酒的人数不胜数。"
    G "可我每日都需要外出采药行医,老夫实在分身乏术，不知小生可有办法？"
    A "老先生，我也是学中医药的，很能体会到老先生的心情！我有一个办法，只是可能会冒犯到老先生的药方，不知老先生可愿一听？"
    G "是吗？那小生快快请讲！我的药方当然不及百姓的健康安全重要，只要能解决现在的问题就好。"
    hide 唐微笑 at left
    with dissolve  
    show 唐疲惫 at left
    with dissolve 
    A "不知老先生可愿给出屠苏药酒的药方？如果人们也懂其中的药物知识，炮制先生的处方，便可自己配置出屠苏酒，也就不会为求屠苏酒将这里堵得水泄不通了。"
    A "只是，这样做，可能会将先生的药方公之于众，影响到先生的收益。"
    G "我从医的初心便是一心一意医治好病人，并不在意收益与否，小生说的确实是个好办法，让百姓也懂药物知识，不盲目从医服药。我这就把屠苏酒的配方告诉小友。"   
    G "但是，在这之前，我得考考小友。小友既也习医，想必对医学方面很有了解。"
    "学了中医药几年，既然先生要考，我得努力答对，不让先生失望，不能丢了我学校的脸，虽然先生不知道......"
    call SFZ4
    call SFZ5
    call SFZ6
    G "恭喜小友通过了我的考验，我现在将屠苏酒的配方告诉你。小友可愿帮我誊写一遍处方呢？我方才采完药回来，手实在疲劳，小友可愿代笔？"
    hide 唐眯眼笑 at left
    with dissolve
    show 唐疲惫 at left
    with dissolve
    A "啊，当然愿意，只是…"
    "这可怎么办呀，我只是在上课学习的时候见过一些古文，但是并不会写啊，系统系统快救我！听到我的心声了嘛<明溪>？"
    E "你尽管写，有我在，不用担心。"
    "<明溪>，你最好是说真的，别破我防…看来我只能硬着头皮写了…"
    G "小友？小友？你没事吧？怎么了？"
    hide 唐疲惫 at left
    with dissolve
    show 唐惊讶 at left
    with dissolve   
    play sound "music/震惊声音ID17779.wav"    volume 0.4
    A "啊没事的先生，我现在写，先生您说。"
    scene 屠苏庵#孙思邈书房
    with fade
    "孙思邈将屠苏药酒的配方向我娓娓道来，事无巨细，以及炮制和饮用的方法和注意事项全都告知于我，我将这些一一写下。"
    "此时，为孙思邈分发屠苏酒的伙计急匆匆地赶来，敲了敲我们所在屋子的门。"
    show eileen happy as huoji at left
    with dissolve
    show 孙思邈 as sunsimiao at right
    with dissolve
    H "老先生，屠苏药酒已无余量，可是来讨屠苏药酒的人络绎不绝，这可怎么办呀先生？"
    G "辛苦你了，无妨，我已托这位小生帮我写下药方方便人们传抄。"
    hide eileen happy as huoji at left
    with dissolve
    show 唐微笑 at left
    with dissolve
    G "多谢小生的帮忙，我现在要去和大家说明情况，抽不开身，小生可否再帮老夫将处方贴至屠苏庵外的柱子上呢？"
    A "好的，老先生先去忙，我这就去贴。"
    scene 屠苏庵屋外#屠苏庵门口
    with fade
    play sound "music/欢呼声.wav" volume 0.6
    "孙思邈走出屋内，告诉大家自己已将屠苏药酒的配方给出，将会粘贴在外面的柱子处。刚刚还一脸愁容的人们听了之后惊喜万分，纷纷向孙思邈道谢。"
    scene 屠苏庵#屠苏庵内
    with fade
    "我张贴完,回到屠苏庵，孙思邈看见我，便放下手中处理采回来草药的活。"
    show 唐微笑 at left
    with dissolve
    show 孙思邈 as sunsimiao at right
    with dissolve
    G "小友已经粘贴好配方了吗？"
    hide 唐微笑 at left
    with dissolve
    show 唐眯眼笑 at left
    with dissolve   
    A "是的。老先生体恤百姓，公而无私，不保守自己的医术，如此高尚的医德，令小生钦佩不已！"
    G "小友哪里的话！我以为，医生就应公而无私，谨慎谦虚，万不可恃己所长而专心细略财务！专心治疗病患才是医生的职责所在。"
    scene 屠苏庵#屠苏庵内
    with fade
    "这时一个妇人匆匆忙忙赶过来寻医，孙思邈没有多言，立即起身去问诊。恍惚间，周遭的景象开始变淡，渐渐的，屋舍的轮廓也变得模糊不清...我又回到了列车上。"
    stop music
    play sound "music/train01_4loop.mp3" volume 0.5
    scene 科技感列车
    with dissolve
    show 现代1 at left
    with dissolve
    E "恭喜你完成第二个任务，再完成一个你就可以回到原来的世界了"
    A "<明溪>，孙思邈先生对病人真的是无私奉献啊，没有一点点犹豫，我好像得到了一些指引，有点舍不得这里，但好期待下一个任务，我会遇见谁呢..."
    stop music
    play music "music/bg_start_wanan.mp3" volume 0.3
    scene 风景
    with dissolve
    "好累......眼皮变得重了起来，哎，我不会又要睡着了吧，每次想看清列车行驶的道路都会睡着......"
    "列车缓慢行驶，穿过唐朝，开向下一个医药时空......"
    scene hei
    with fade
    "章节二，完成"

    #李时珍篇开始
    scene 列车穿森林
    with fade
    "随着列车缓缓行驶，迷迷糊糊间列车到站的提示声又响起了。"
    play sound "music/叮咚.wav" volume 0.5
    "列车已到站，请乘客收拾好随身物品，有序下车。"
    "不知道为什么，回家的念头没有那么强烈了，或许是回家还要面对现实吧，我反而有些期待继续和古医师交流了。不管了，还是先下去看看吧。"
    play music "music/明代BGM.mp3" volume 0.5 
    scene 明代村庄
    with fade
    "车门缓缓打开，映入眼帘的是一座寺庙，往远了看去，是潺潺雨湖，烟柳画桥，风帘翠幕…只见绵延的长江水，弯曲地穿过这块土地，一块块牌坊接连着。"
    "这里的景色真好啊，古色古香…这条江…看着怎么这么像长江呢？"
    scene 明代村庄科技#景色嵌套系统
    with fade
    show 明笑容 at left
    with dissolve
    play sound "music/叮咚.wav" volume 0.5
    A "<明溪>，这里是哪里呢？"
    E "欢迎来到明朝！这里是湖北蕲州。"
    hide 明笑容 at left
    #with dissolve
    show 明惊讶 at left#惊讶
    with dissolve
    A "什么？！这里是湖北蕲州？！那不是李时珍的故乡吗？所以这一关的任务不会是帮助李时珍老先生吧？"
    E "是的，这里就是李时珍的故乡。"
    hide 明惊讶 at left
    #with dissolve
    show 明难过 at left#难过
    with dissolve  
    A "那<明溪>，我还要完成多少任务才能回去呢？我不是这个世界里的人啊，我还有我的父母，我的学业，我还得…看看是否从事中医药的工作…"
    "说到这里，我又开始有些难过，声音也不自觉弱了下去。"
    E "这一次的任务就是你的最后一次任务了，南烛，完成这最后一关，你就能找到自己的答案了。"
    hide 明难过 at left
    #with dissolve
    show 明笑容 at left#积极的表情
    with dissolve     
    "虽然系统只是我面前的一个弹窗，但我总觉得，站在它面前，它好像在坚定地注视着我，使我突然就有了继续的信心。"
    E "这一关的任务就是协助李时珍。李时珍，字东璧，晚年自号濒湖山人，湖北蕲州人，明代著名医药学家。与“医圣”万密斋齐名，古有“万密斋的方，李时珍的药”之说。"
    E "后为楚王府奉祠正、皇家太医院判，去世后明朝廷敕封为“文林郎”。"
    E "这便是李时珍的简介了，剩下的我就不提示你了，最后一关你只管前行，会有人指引你的。"
    scene 明代村庄#车外景色
    with fade
    play sound "music/震惊声音ID17779.wav"    volume 0.4
    show 明惊讶 #惊讶
    with dissolve    
    "什么？没有提示了？那我也不清楚该怎么走往哪走呀，救命呐！"
    A "系统？系统？别走啊！"
    hide 明惊讶
    show 明难过
    with dissolve
    "可恶的系统，居然把我丢下了？！唉，看来我只能靠自己了。"
    call LFZ1
    scene 江南水乡2#车外景色+村庄
    with fade
    "我没有办法，只得继续往前走了。一路向前，细看蕲州城，便会发现这里三面环水，临江靠湖，熙熙攘攘的人群，以及随处可见的水井。"
    "我继续往前走，顺着那些水井的方向，走进了一个小村庄。"
    call LFZ2
    "走上前，才发现大家都是在围着一个村民，只是这个村民似乎是喝醉了，站也不稳，东倒西歪的，时不时地手舞足蹈，或者哈哈大笑，引得众人也笑声一片。"
    hide 明疲惫 #疑惑
    #with dissolve
    show 明笑容 #笑
    with dissolve    
    "一个背着药箱的老者从我身旁经过，径直走向了人群中间那个喝醉的村民。只一眼，我便顿住了。"
    hide 明笑容 #笑
    #with dissolve
    show 明惊讶 #惊讶
    with dissolve   
    "等…等…等会！这这…这个人不是李时珍嘛？我去过湖北黄冈的蕲春县那里的李时珍纪念馆！简直一模一样！这肯定就是李时珍！天呐我就遇上啦？！"
    "我赶忙收住抬起的脚，转身，看向李时珍。只见李时珍来到那个村民面前，仔细观察他的举止，围观的人有了解的，便开口告诉李时珍是喝了用山茄子泡的药酒。"
    hide 明惊讶  #惊讶
    #with dissolve
    show 明笑容 #正常
    with dissolve 
    "之前学习了《医古文》，都说李时珍为编纂《本草纲目》，除“书考八百余家”，还寻医问药，跋山涉水，拜师学艺，谦虚地向各行各业的劳动人民学习。"
    # "村民此时就是一个醉汉，全然听不见旁人的言语，只是傻笑着。李时珍又耐心地询问了一遍。旁边围观的人有了解的，便开口告诉了李时珍是喝了用山茄子泡的药酒。"
    #"李时珍听闻，微微点头，道过一番谢，便转身就要离开了。"
    hide 明笑容 #正常
    #with dissolve
    show 明惊讶 #惊讶
    with dissolve   
    "哎，李时珍老先生这是要离开了吗？不行，我得跟上，具体要完成什么任务还不清楚呢。"
    "啊啊啊他老人家停下了！转过身来啦！我该不该直接询问哪里需要我帮忙来完成任务吗？会不会有些冒昧了呢？都怪系统！"
    hide 明惊讶#惊讶
    #with dissolve
    show 李时珍  as lsz at right#lishiz
    with dissolve    
    I "这位小生走过来是有什么事情吗？"
    show 明笑容 at left#正常
    with dissolve
    A "请问先生是医药学家李时珍李老先生吗？"
    I "是的。"
    hide 明笑容 at left
    show 明微笑 at left
    with dissolve
    A "先生好，我是南烛，早听闻先生格物明理，博采众长，锐意创新，济世寿民，四处游历搜集药物资料，虚心请教，不愧为“药圣”。"    
    A "小生也从医，现在还在学习中医阶段，特来向先生学习。" 
    hide 明微笑 at left
    show 明笑容 at left
    with dissolve
    I "小生谬赞了，我们世代从医，读下万卷书，行万里路，认真游历、行医，才得小成就。"
    I "既然小生也从医，正好刚才我又看见有喝下山茄子泡的药酒的村民，他的症状我之前并未见过，小生可愿前往东璧堂与我一同研究这山茄子？"
    hide 明笑容 at left#正常
    #with dissolve
    show 明微笑 at left#笑
    with dissolve   
    A "当然好啦，能与先生一同学习是我的荣幸！"
    "哇！太棒了！系统果然没有骗我！"
    scene 屋子#药堂
    with fade
    "我们不一会儿便抵达了药堂。这里很大，有种药草的园子、晾晒药草的空地、熬制药草的房屋，还有浓浓的草药香传来。走进厅内，李时珍便放下了药箱。"
    scene 药房#厅内
    with fade
    show 明笑容 at left #正常
    with dissolve
    show 李时珍 as lsz at right
    with dissolve
    I "小友，我的学识还不够渊博，并不知山茄子这味药的药性，不知小友可愿与我一起去书房翻阅医术查一查这味药？"
    A "当然是愿意的！只是先生谦虚了，先生对药物的了解可是无人能及，世间草药千千万，先生哪能全都认齐呢？"
    I "不是的小友，作为医者就是要大医精诚、实事求是、不懈探索，如果连药草都不识，又谈何救死扶伤？"
    hide 明笑容 at left #正常
    #with dissolve
    show 明微笑 at left #笑
    with dissolve
    A "先生说得是，小生受教了。"
    I "那我们先去查阅医书吧。"
    scene 药房 #书房
    with fade
    "李时珍老先生递给我好一些医书，医书上药物的药性用途记录得清清楚楚，就连配图都是精心画的。,我们便开始了查找。"
    show 李时珍 as lsz at right #正常
    with dissolve     
    I "原来这味药是曼陀罗，不过要研究它的药性，我们还得亲自实践，现下我们要先找到它，小友可愿与我一并去寻？"
    show 明微笑 at left
    with dissolve 
    A "愿意的先生！"
    scene 山林#武当山
    with fade
    "就这样，我与李时珍老先生踏上了寻药之途，最后，我们终于在武当山发现了曼陀罗的踪迹，我们高兴的手舞足蹈，先生全然没有任何架子的样子，让我觉得特别亲近。"
    scene 山林2#武当山
    with fade  
    "期间，先生的目光并不是只放在曼陀罗身上，遇见其它药草，先生会随时观察并记录，仔细分析它们的药性，我突然觉得大学上课是拿过的那本《本草纲目》是多么的沉重。"
    "先生与我小心搜集好曼陀罗的种子带回去种下，我们每天都细心照料。功夫不负有心人，我们终于等到了曼陀罗花开！"
    scene 屋子#随便一个李时珍家
    with fade   
    show 明微笑 at left#兴奋
    with dissolve
    A "太好了先生！它开花了！" 
    show 李时珍 as lsz at right #正常
    with dissolve
    I "是啊，开花啦，这段时间辛苦小友了，这本该是我自己该做的，却让小友与我劳累奔波。"
    hide 明微笑 at left
    #with dissolve
    show 明笑容 at left#正常
    with dissolve   
    A "先生哪里的话！我一心向先生学习，先生处处指点，我收益匪浅，应当是我谢谢先生了，先生为医学用心至此，倒让小生十分钦佩。"
    I "这样吧小友，我来考你个问题吧，看看你学习得如何了。"
    call LFZ3
    "李时珍取下曼陀罗的花按照村民说的方法泡了酒，过了几天，李时珍取出了曼陀罗酒来，打算亲身体验一下曼陀罗的功效。只见李时珍已经用碗盛了一些药酒出来。"
    hide 明微笑 at left
    #with dissolve
    show 明惊讶 at left #惊讶
    with dissolve
    "什么？先生要亲自尝一尝？这不是以身犯险吗？我得阻止先生这样做！"
    "虽然以前学习中药材的时候就对李时珍亲尝百草的事耳濡目染，但是现在先生就在我面前，我实在不忍心看下去啊。这酒也不知毒性，喝下去也不知道会不会…"
    call LFZ4
    scene 药房#随便一个房间
    with fade
    "先生连忙记下了曼陀罗的产地、形状、习性、生长期,写下了如何泡酒以及制成药后的作用、服法、功效、反应过程等。"
    play sound "music/叮咚.wav" volume 0.5
    "我正看着先生前忙后，一声机械声打断了我，那个蓝色系统界面显露出来。"
    scene 系统药房 #带系统随便一个房间
    with fade
    #插入系统音效
    E "南烛，恭喜你完成最后一个任务，半个小时后我会将你送返归程列车。"
    show 明惊讶 at left#惊讶
    with dissolve
    play sound "music/震惊声音ID17779.wav"    volume 0.4
    A "啊？！等会就可以回去吗？！"
    "我能回去啦？！不是在做梦吧？天呐！我还是有些懵…"
    scene 药房 #回到房间
    with fade
    "李时珍本来在记录，突然听见我大喊一声，赶紧回头看我。"
    show 李时珍 as lsz at right
    with dissolve
    I "怎么了小友？"
    show 明难过 at left#忧愁
    with dissolve
    "看着先生关心的目光，还有半个小时，我就要和先生分别了，是只能在古书上听闻的先生啊…我应该和先生好好道别的。"
    A "先生，我想，我该回去了，谢谢先生这段时间的教导和照顾，我收获了很多，真的很感激先生，先生是一个很好的医者。"
    I "小友要回去了吗？这么突然？啊…我也要谢谢小友这段时间的陪伴。"
    I "小友既学医，回去了也要好好从医，扎实医学基础，要记住观察和试验是本草药研究的基本方法，要会概括和综合药类，会批判继承和调查研究。"
    hide 明难过 at left#忧愁
    #with dissolve
    show 明笑容 at left#正常
    with dissolve  
    I "要有仁心仁术，躬体力行，不单要读万卷书，更要行万里路啊！"
    I "即使这条路不好走，很难，阻挠我们的人很多，那也不要紧，你不是一个人啊，我一直在，我们都在，做好自己就好。"
    hide 明笑容 at left
    #with dissolve
    scene 药房 #房间
    show 明难过 #忧愁
    with dissolve  
    "我愣住了，眼看着时间到了，李时珍先生的身影再看不见，我才愣愣地落下两行泪来。"
    "是了，是了，这就是我一直在找的答案啊。"
    scene 列车内部 #列车外景象
    with fade
    show 现代惊讶 
    with dissolve 
    stop music
    play music "music/bg_start_wanan.mp3" volume 0.3 
    "唔～我又回来啦。一时间，想回家的念头却没有之前那么强烈了，我的脑海里，华佗、孙思邈、李时珍的身影愈发清晰。"
    "我开始回味自己经历的一系列事情…华佗勤求博采，恪尽职守，不慕权势，更是有着生命至上、主动施治的服务精神。"
    "孙思邈不单有着渊博的医学知识和高超的医术，更有博大的仁爱之心和对贫民百姓的怜悯之情，平等用心对待每一位病人，李时珍先生更是身体力行，为病人尝遍每一种药，一心为病人解忧"
    scene bg_family #全家福
    with fade
    "回想起从小父母的教诲，大学生活......"
    scene 列车穿森林 #风景
    with fade
    "我看向窗外，是熟悉的景色，一排排高大的树木飞速地往后倒退着…"
    "是了，作为一个医者，医学知识的稳固扎实是基础，同时又要不断更新自己的专业知识，多积累治病救人的经验。"
    "有一颗仁心，更是医者的本分，对生命的宝贵怀有感恩之心，保持一颗治病救人的爱心，时刻将治病救人放在首位，同情患者的疾苦，对所有患者一视同仁…"
    scene bg_daxue #背影
    with fade
    "于是我坚定了走好中医药道路的决心，一开始我的背影是迷茫的，现在我的背影是坚毅的... ..."
    "<明溪>，谢谢"
    scene 风景
    with fade 
    '''到这里南烛的杏林之旅结束，感谢大家陪南烛走过这些路。
    一株小草改变世界，一枚银针联通中西，一缕药香穿越古今，一纸经方传承千载。中医药是中国古代科学的瑰宝，也是打开中华文明宝藏的钥匙。
    '''



    return 

label game1:
    menu:
        "请通过系统指示选择哪住药草是茵陈蒿。"
        "草药1。":
            $ X = 1
        "草药2。":
            $ X = 2
        "草药3。":
            $ X = 3

    if X == 1:
        hide 汉服劳累惶恐
        show 汉服微笑
        with dissolve
        E "恭喜你南烛，你的选择是正确的。"
        "现在快把采到的草药拿回村子里吧！"
        hide 汉服微笑
    elif X == 2:
        E "南烛，你再好好想想吧。"
        jump game1
    else:
        E "南烛，你再好好想想吧。"
        jump game1
return

label xuanze1:
    menu:
        "这时应该怎么办。"
        "四处转转":
            $ X = 1
        "待在原地":
            $ X = 2

    if X == 1:
        A "这样下去也不是办法，还是到处走走熟悉一下环境吧。"
    
    elif X == 2:
        A "先等等吧，万一列车开走就不好了。"
        jump xuanze1_情景1
return

label xuanze1_情景1:
    hide 汉服劳累惶恐
    """
    过了很久也没有动静......
    """
    show 汉服饿了
    with dissolve
    play audio  "music/肚子咕咕叫声音ID14591.wav" volume 0.7 
    A"好饿呀..."
    A"列车是坏了吗，那我怎么办？"
    stop audio
    A"不能坐以待毙。还是四处走走吧，要是附近有人的话就得救了！"
    hide 汉服饿了
    
return
label talk_xt_and_cz:
    menu:
        "请选择你的反应。"
        "掉头就跑":
            $ X = 1
        "问它问题":
            $ X = 2

    if X == 1:
        hide 汉服吃惊 at left
        show 汉服大惊失色 at left
        A "妈呀，这难道不是小说里才会出现的情节吗...我不是在做梦吧。"
        """
        我开始不由自主地向后退，仿佛在为下一秒拔腿就跑做准备。
        """
        C "南烛，你退半步的动作是认真的吗？你不会是想跑吧！"
        hide 汉服大惊失色 at left
        show 汉服尴尬 at left
        """
        看到它戳穿了我的想法，不由有些尴尬。
        """
        A "哪有......"
        C "那有什么需要我帮你的吗？"
        hide 汉服尴尬 at left 
        show 汉服劳累惶恐 at left
        hide 汉服劳累惶恐 at left
        show 汉服正常 at left
        """
        我清清嗓子，努力让自己镇静下来。
        """ 

    elif X == 2:
        hide 汉服吃惊 at left
        show 汉服正常 at left
        A "咳咳。"
        """
        我清清嗓子，努力让自己镇静下来。
        """     

return

label 进屋探望:
    menu:
        A "要进屋看看吗？"
        "扣门询问":
            $ X = 1
        "径直离开":
            $ X = 2
    if X == 1:
        """
        上前轻轻叩门。
        """
        hide 汉服吃惊 at left
        show 汉服正常 at left
        with dissolve
        A "老人家，我们能不能进来看看你？"
        D "嗯，快进来吧。"
        hide 汉服正常 at left
    if X == 2:
        show 华佗正常 at right
        with dissolve
        B "进去看看吧。"
        hide 汉服吃惊 at left
    show 汉服微笑 at left
    with dissolve
    A "好"
    
return

label 任务one_start:
    menu:
        "现在是该做出选择的时候了。"
        "进入村庄":
            $ X = 1
        "离开村庄":
            $ X = 2
    if X == 2:
        hide 汉服犹豫 
        show 汉服想跑 
        A "系统？做任务？这又是什么新的骗局吗。"
        A "古人有云:<三十六计走为上>,开溜！"
        scene hei
        """
        走了很久......
        """
        scene village
        with eye_open
        show 汉服吃惊
        with dissolve
        A "居然...又回到了原地！"
        """
        此时，<明溪>的声音出现在了耳边。
        """
        E "温馨提示，您需完成任务才可离开这里。"
        hide 汉服吃惊
        show 汉服劳累惶恐
        A "看来这是我的使命"
        hide 汉服劳累惶恐
return

label meethuatuo:
    menu:
        "遇到老人，你会？"
        "和他打招呼":
            $ X = 1
        "忽视他":
            $ X = 2
    if X ==1:
        hide 汉服劳累惶恐 at left
        show 汉服微笑 at left
        A "老先生，您好呀！"
        hide 汉服微笑 at left
        show 汉服吃惊 at left
        """
        话刚出口，我就意识到了一个问题。
        """
        """
        我说普通话他能听得懂吗？
        """
        B "嗯，你好"
        A "欸？！"
        E "南烛，有我在，你就不用担心交流的问题啦。"
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        """
        原来是<明溪>。也是，它这么厉害，让我们无障碍交流也是小菜一碟吧。
        """
    elif X == 2:
        B "小伙子，你不是本地人吧？"
        hide 汉服劳累惶恐 at left
        show 汉服吃惊 at left
        with dissolve
        A "欸？这么明显吗？"
        B "是的，从你的表情就不难看出。"
        """
        震惊之余，我突然意识到了一个问题。
        """
        """
        我说普通话他能听得懂吗？
        """
        B "嗯，你好"
        A "欸？！"
        E "南烛，有我在，你就不用担心交流的问题啦。"
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        """
        原来是<明溪>。也是，它这么厉害，让我们无障碍交流也是小菜一碟吧。
        """
return
label 华佗出题:
    show 汉服吃惊 at left
    with dissolve
    menu:
        B "最早应用脉诊来判断疾病,并且提出了相应的脉诊理论的医生是？"
        "张仲景":
            $ X = 1
        "扁鹊":
            $ X = 2
        "黄帝":
            $ X = 3
        "不清楚欸":
            $ X = 4
    if X ==1:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "应该是张仲景吧。"
        call 答题错误_1
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==3:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "应该是黄帝吧。"
        call 答题错误_1
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==4:
        hide 汉服吃惊 at left
        show 汉服尴尬 at left
        with dissolve
        A "我不知道......"
        call 不知道答案
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==2:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "应该是扁鹊。"
        B "嗯，下一题"
        hide 汉服微笑 at left
        call 华佗出题2
return

label 华佗出题2:
    show 汉服吃惊 at left
    with dissolve
    menu:
        B "被称为<医家之宗>的是？"
        "<神农本草经>":
            $ X = 1
        "<伤寒杂病论>":
            $ X = 2
        "<难经>":
            $ X = 3
        "<内经>":
            $ X = 4
    if X ==1:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "应该是<神农本草经>吧。"
        call 答题错误_2
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==2:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "或许是<伤寒杂病论>。"
        call 答题错误_2
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==3:
        hide 汉服吃惊 at left
        show 汉服尴尬 at left
        with dissolve
        A "难道是<难经>吗？"
        hide 汉服尴尬 at left
        call 答题错误_2
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==4:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "应该是<内经>。"
        B "没错，最后一题。"
        hide 汉服微笑 at left
        call 华佗出题3
return

label 华佗出题3:
    show 汉服吃惊 at left
    with dissolve
    menu:
        B "<中医四诊>指的是？"
        "望":
            $ X = 1
        "闻":
            $ X = 2
        "问":
            $ X = 3
        "切":
            $ X = 4
        "以上都是":
            $ X = 5
        
    if X ==1:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "应该是<望>吧。"
        call 答题错误_3
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==2:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "或许是<闻>。"
        call 答题错误_3
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==3:
        hide 汉服吃惊 at left
        show 汉服尴尬 at left
        with dissolve
        A "难道是<问>吗？"
        hide 汉服尴尬 at left
        call 答题错误_3
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==4:
        hide 汉服吃惊 at left
        show 汉服尴尬 at left
        with dissolve
        A "可能是<切>吧？"
        hide 汉服尴尬 at left
        call 答题错误_3
        B "好的。"
        hide 汉服劳累惶恐 at left
        jump 华佗出题
    elif X==5:
        hide 汉服吃惊 at left
        show 汉服微笑 at left
        with dissolve
        A "先生，中医中的<四诊>指得正是<望闻问切>。"
return



label 答题错误_1:
    hide 汉服微笑 at left
    show 汉服大惊失色 at left
    with dissolve
    B "不对呀小伙子，这方面的知识看来你还需要精进呀！"
    hide 汉服大惊失色 at left
    show 汉服劳累惶恐 at left
    with dissolve
    A "请先生再给我一次机会吧！"
    hide 汉服劳累惶恐 at left
return

label 答题错误_2:
    hide 汉服微笑 at left
    show 汉服大惊失色 at left
    with dissolve
    B "很遗憾，你答错了，这方面的知识看来还需要精进呀！"
    hide 汉服大惊失色 at left
    show 汉服劳累惶恐 at left
    with dissolve
    A "请先生再给我一次机会吧！"
    hide 汉服劳累惶恐 at left
return

label 答题错误_3:
    hide 汉服微笑 at left
    show 汉服大惊失色 at left
    with dissolve
    B "真可惜，不是这个答案"
    hide 汉服大惊失色 at left
    show 汉服劳累惶恐 at left
    with dissolve
    A "请先生再给我一次机会吧！"
    hide 汉服劳累惶恐 at left
return

label 不知道答案:
    hide 汉服尴尬at left
    B "小伙子，这方面的知识看来你还需要精进呀！"
    show 汉服劳累惶恐 at left
    with dissolve
    A "请先生再给我一次机会吧！"
    hide 汉服劳累惶恐 at left

return

label SFZ1:
    menu:
        "现在你打算？"

        "在原地摆烂一会儿":
            $ X = 1
            
        "继续往前走吧":
            $ X = 2

    if X == 1:
        "身旁的灌木丛发出悉悉索索的声音…"
        hide 现代_惊讶
        with dissolve
        scene 野猪农田 #有野猪
        play sound "music/震惊声音ID17779.wav"    volume 0.4
        show 唐惊讶 at left
        "“哗”地一下，一只野猪窜了出来，吓得我拔腿就跑，一直跑到有许多屋舍的地方才不见野猪。"
        #呼声
        "呼～得赶快离开这里了!"
    elif X == 2:
        scene 农田 #沿途风景
        "我在沿途路过许多农田，渐渐的出现屋舍。"
    return
    
label SFZ2:
    scene 常州街道#常州繁华街道
    with fade
    menu:
        "逛逛这里繁华的街市吧":
            $ X = 1
        "先问问系统我的任务吧":
            $ X = 2
    if X == 1:
        "这一整条街的景象让人啧啧称奇，有卖轻纱的，远处朱阁里有低吟浅唱的歌伎，有布置花灯的差人…"
        "这时有一位妇人步履匆忙，但是人太多了，一下就被撞倒，摔倒在了我脚边，我赶紧俯身扶住她。"
        show 唐眯眼笑 at left
        with dissolve
        show 老妇人 as furen at right
        with dissolve
        F "多谢这位好心人！"
        A "不碍事的大娘。不过大娘走路不要太急了，这里人多容易摔跤。"
        F "哎，这位公子有所不知，我家里的小孩不舒服，我得赶紧去向孙思邈神医讨屠苏酒了。"
        hide 老妇人 as furen at right
        with dissolve
        hide 唐眯眼笑 at left
        with dissolve
        show 唐惊讶 at left
        with dissolve
        "孙思邈神医？诶呦我才反应过来孙思邈唐初一直在常州行医,难不成这次的任务和孙思邈有关？"
        "叫叫系统吧"
        hide 唐惊讶 at left
        with dissolve       
    elif X == 2:
        "叫叫系统吧" 
    return


label SFZ3:
    scene 人群屠苏庵 #屠苏庵门口
    menu:
        "好慌，快走！":
            $ X = 1
        "快快快，假装淡定！":
            $ X = 2
    if X == 2:
        show 孙思邈 as sunsimiao at right
        with dissolve
        G "这位小生是？我常在这一带行医，倒是从没见过，是从外地来寻医的吗？"
        show 唐疲惫  at left
        with dissolve 
        "(这下走不了了，只能好好完成任务了.......)"
        hide 唐疲惫 at left
        with dissolve 
        show 唐眯眼笑 at left
        with dissolve         
        A "对的老先生，我是外地赶来的，不过我不是来寻医的，听闻先生为治瘟疫，夙夜不懈地研制药酒，这令小生十分钦佩。可此后便每每碰上今天这样的麻烦，我是来帮助先生解决这个麻烦的。"
    elif X == 1:
        show 孙思邈 as sunsimiao at right
        with dissolve
        G "哎这位小生，请留步，我常在这一带行医，倒是从没见过，是从外地来寻医的吗？"
        show 唐疲惫  at left
        with dissolve 
        "(这下走不了了，只能好好完成任务了.......)"
        hide 唐疲惫 at left
        with dissolve 
        show 唐眯眼笑 at left
        with dissolve   
        A "对的老先生，我是外地赶来的，不过我不是来寻医的，听闻先生为治瘟疫，夙夜不懈地研制药酒，这令小生十分钦佩。可此后便每每碰上今天这样的麻烦，我是来帮助先生解决这个麻烦的。"
    return


    label SFZ4:
    scene 屠苏庵
    with fade
    show 唐微笑 at left
    with dissolve
    show 孙思邈 as sunsimiao at right
    with dissolve
    menu:
        "屠苏药酒的配方不涉及下列哪一个？"
        "桂枝":
            $ X = 1
        "花椒":
            $ X = 2
        "乌头":
            $ X = 3
        "白芷":
            $ X = 4
    if X == 4:
        hide 唐微笑 at left
        with dissolve
        show 唐眯眼笑 at left
        with dissolve
        G "小友回答对啦，看来小友确实对中医药有研究呢，那我再来考考你吧。"
    else:
        hide 唐微笑 at left
        with dissolve
        show 唐疲惫 at left
        with dissolve
        G "选错啦，请小友再加把劲，不要气馁"
        jump SFZ4
    return


    label SFZ5:
    scene 屠苏庵
    with fade
    show 唐微笑 at left
    with dissolve
    show 孙思邈 as sunsimiao at right
    with dissolve
    menu:
        "将药包放在盛有黄酒的瓶中多久屠苏药酒才能饮用？"
        "三天左右":
            $ X = 1
        "一周左右":
            $ X = 2
        "一个月左右":
            $ X = 3
        "半年左右":
            $ X = 4
    if X == 1:
        hide 唐微笑 at left
        with dissolve
        show 唐眯眼笑 at left
        with dissolve
        G "是的，只要三天左右就可饮用。看来小友的知识很渊博呢，我再考你最后一个问题吧。"
    else:
        hide 唐微笑 at left
        with dissolve
        show 唐疲惫 at left
        with dissolve
        G "不是这么久的哦，你答错啦。"
        A "先生，再给我一次重新回答的机会吧。"
        
        jump SFZ5
    return


    label SFZ6:
    scene 屠苏庵
    with fade
    show 唐微笑 at left
    with dissolve
    show 孙思邈 as sunsimiao at right
    with dissolve
    menu:
        "屠苏酒有什么功效呢？"
        "益气温阳":
            $ X = 1
        "祛风散寒":
            $ X = 2
        "避除疫疾":
            $ X = 3
        "延年益寿":
            $ X = 4
    if X == 4:
        hide 唐微笑 at left
        with dissolve
        show 唐眯眼笑 at left
        with dissolve
        G "对的，屠苏酒的功效很多，这些时日爆发的瘟疫也是用它平息的。"
    else:
        hide 唐微笑 at left
        with dissolve
        show 唐疲惫 at left
        with dissolve
        G "“答错了，这也是屠苏酒的功效之一。再试试吧"
        jump SFZ6
    return

#李时珍篇分支开始
label LFZ1:
    menu:
        "就在这待着吧！":
            $ X = 1
        "算了算了，走吧！":
            $ X = 2
    if X == 1:
        scene 明代村庄科技 #风景系统
        with fade
        "我留在原地没有动，过了好一会，蓝色系统界面才终于弹出来。"
        show 明笑容 at left#得意
        with dissolve
        "呀！系统！嘿嘿被我拿捏了。"
        E "南烛，这是最后一关任务，你不想回去了吗？放心，任务并不难，需要细细体验和品味。为了你要找的答案，别放弃。"
        hide 明笑容 at left#得意
        with dissolve
        show 明微笑 at left#坚定
        with dissolve
        A "对的，完成这关任务我就能回家，看来不能不走了。"
    if X == 2:
        "赶路赶路！"
    return

    label LFZ2:
    menu:
        "坐下歇一会":
            $ X = 1
        "继续往前走":
            $ X = 2
    if X == 1:
        scene 人群 
        with fade
        #插入嘈杂音效
        play sound "music/嘈杂.wav" volume 0.3
        "我停了下来，微眯眼睛，正懒懒地享受微风，突然不远处传来了嘈杂地声音，隐隐约约传来男子哈哈大笑的声音…睁开眼睛，前面有一群人围在一起"
        show 明疲惫 
        with fade
        "好吵呀，奇怪了，前面发生了什么吗？我还是去看看吧。"
        stop sound
    if X == 2:
        scene 人群
        with fade
        #插入嘈杂音效
        play sound "music/嘈杂.wav" volume 0.3
        "前方有一群人围在一起，人群中间似乎还会间断地爆发出男子大笑的声音，其中的小孩子一直在“咯咯”地笑着，围圈的人们似也在接头接耳。"
        show 明疲惫 
        with fade
        A "他们怎么都围在一起呀？是发生了什么吗？在讨论什么呢？我还是也走上前去看看吧。"
        stop sound
    return

    label LFZ3:
    menu:
        "取曼陀罗的哪个部位入酒喝下便会和当初的村民一般？"
        "根":
            $ X = 1
        "茎":
            $ X = 2
        "叶":
            $ X = 3
        "花":
            $ X = 4
        "果":
            $ X = 5
    if X == 4:
        hide 明笑容 at left
        with dissolve
        show 明微笑 at left#xiao
        with dissolve
        I "小友回答对啦，看来小友最近确实有跟着我在好好学呢。"

    else :
        hide 明笑容 at left
        with dissolve
        show 明难过 at left#难过
        with dissolve
        I "小友答错啦，再仔细想想。"
        jump LFZ3
    return

    label LFZ4:
    menu:
        "拿过先生的酒碗，自己来尝":
            $ X = 1
        "在一旁备好解药":
            $ X = 2
    if X == 1:
        I "慢着！快放下！"
        hide 明惊讶 at left
        #with dissolve
        show 明疲惫 at left#晕难受
        with dissolve      
        "唔…味道很香嘛…啊呀呀…唔…我的舌头口腔怎么都麻了呀，好难受…好晕好晕…"
        "我喝下之后，意识开始模糊，不一会儿竟发出阵阵傻笑，手脚也不停地舞动着，最后，我完全失去知觉，摔倒在地。先生喂我吃下他自制的解药。过了好一会儿，我才慢慢转醒。"
        I "胡闹！你简直是在胡闹！你怎么自作主张就喝下了？你知不知道这有多危险！"
        hide 明疲惫 at left
        #with dissolve
        "就这样晕了一会儿... ..."
        show 明微笑 at left#惊喜
        with dissolve 
        "我还活着？！先生救了我！太好了！喝得值，先生厉害！不过刚刚真的太可怕了，药效太强了。"
        A "先生，我好好的呀，已经没有大碍了！先生会救我的，先生的医术实在精湛！"
        I "你现在感觉如何？好些了吗？刚刚太危险了！以后不许这么做！尝药有太多的未知性！"
        hide 明微笑 at left
        #with dissolve
        show 明笑容 at left#zhengchang
        with dissolve   
        A "我已经很好啦先生！可是先生尝也是在冒险啊。"
        hide 明笑容 at left
        #with dissolve
        show 明难过 at left#zhengchang
        with dissolve  
        I "我不尝，怎么断定它的功效？再说，总不能拿病人去做实验吧？医者医者，当然是要躬体力行。"
        I "小友既尝，那便同我细细描述这个反应过程吧，我好记录下来。"
        "我同先生细细描述，先生一字不落地详细记录了下来。"
    else :
        "怎么办呢？先生会不会有事啊？这个解药真的对这个药酒有效吗？好担心啊。"
        I "小友，不必担心，我游历行医如此之久，尝过许多药草，识得许多，特制了解药，不会有事的。"
        hide 明惊讶 at left
        #with dissolve
        show 明难过 at left
        with dissolve
        A "可是还是太危险了啊先生！"
        I "我不尝，怎么断定它的功效？再说，总不能拿病人去做实验吧？医者医者，当然是要躬体力行。"
        "说罢，李时珍抿了一口"
        I "味道很香"
        hide 明难过 at left
        #with dissolve
        hide 李时珍  as lsz at right
        #with dissolve
        show 明难过 #担心
        with dissolve
        "先生又抿了一口，这时他的身形已有些不稳，人昏昏沉沉的，我赶忙去扶住他，最后，他失去了知觉，直接晕过去了。我手忙脚乱地拿过解药便赶紧喂给先生。"
        "喂完解药，看着晕过去的先生，我难受地落了泪。过了好一会儿，先生才醒来。"
        hide 明难过
        #with dissolve
        show 明笑容 at left#开心
        with dissolve
        A "先生！您醒啦！太好了太好了！先生现在感觉如何？刚刚真的吓死我了，太危险了先生！"
        show 李时珍  as lsz at right
        with dissolve
        I "有劳小友担心了，多谢小友及时喂我解药。这味药药效很好，我得记录下来！小友快快取来纸笔，我要记下这反应过程。"
        "我匆忙取来纸笔，先生便开始记录。"
    return




    
label quit:
    "你结束了游戏。"
    return

label after_load:
    "你读档了。"
    return

label splashscreen:
    "logo" #show black scene logo with dissolve hide logo with dissolve
    return

label before_main_menu:
    scene fm
    #pause暂停
    #show logo
    #with dissolve
    #hide logo
    #with dissolve
    return
