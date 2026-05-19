# Title Few-Shots

Use this file to stabilize title-rendered poster generation.

This file is not a theory document. It is a small set of reusable output patterns.

When the user asks for a rendered-title poster and does not provide a precise font reference:

1. match the title family from `references/font-library.md`
2. match the material treatment from poster finish
3. follow the closest few-shot below
4. then adapt title placement and exact wording to the current composition

Default rule still applies:

- render only the main title unless the user explicitly asks for subtitle, slogan, episode tag, or platform copy

## Few-Shot 1: Hard-Edge Battle-Damaged Metallic Display

Input pattern:

- genre: 龙王 / 战神 / 都市硬复仇 / 保镖
- style mode: 写实电影感
- relationship: 权力压制 / 正面对峙
- title need: 直接带字成图

Recommended title-layer output:

```markdown
标题层说明：
- 主标题：龙王归来
- 字形家族：硬核战损金属切角字
- 自动匹配依据：都市硬复仇、强压迫男主、写实动作商业海报
- 标题位置：上中
- 字体风格：现代硬朗黑体式切角海报字
- 字体效果：银灰战损金属、轻微裂纹、克制高光、极浅阴影
- 副标题：无
- 避让要求：不要遮挡主角眼睛、鼻梁、握拳和武器/文件类主道具
- 字符要求：中文正确、边缘硬朗、缩略图冲击力强、不能像低端游戏UI
```

Useful title sentence:

```text
在保留上中标题安全区的前提下，直接渲染中文剧名“龙王归来”。根据都市硬复仇与绝对压迫男主气质，自动匹配“硬核战损金属切角字”，字形厚重锋利，表面使用银灰战损金属与克制裂纹高光，保持动作商业海报冲击力。默认只渲染剧名，不额外添加副标题、平台角标或卖点文案。
```

## Few-Shot 2: Power-Calligraphy Stone-Metal Title

Input pattern:

- genre: 称王回归 / 身份揭晓 / 权势碾压
- style mode: 写实电影感 或 半写实插画
- relationship: 上位压迫 / 王权回归
- title need: 直接带字成图

Recommended title-layer output:

```markdown
标题层说明：
- 主标题：代号龙主
- 字形家族：权谋金石书法字
- 自动匹配依据：称王回归、身份碾压、男主王权感强
- 标题位置：上中
- 字体风格：霸气行草海报化展示字
- 字体效果：银白矿石质感、金石刮擦、轻雕刻边缘
- 副标题：无
- 避让要求：不要压住人物眼睛、王冠轮廓、手势和主视觉轮廓线
- 字符要求：笔势完整、不可乱码、不可弱化成普通书法海报字
```

Useful title sentence:

```text
在保留上中标题安全区的前提下，直接渲染中文剧名“代号龙主”。根据称王回归与身份压迫感，自动匹配“权谋金石书法字”，字形有王权书写势能和商业海报可读性，表面使用银白矿石与轻雕刻刮擦质感，保持霸气、命运感和高识别度。
```

## Few-Shot 3: Palace Gold Vertical Title

Input pattern:

- genre: 宫斗 / 古言 / 王妃 / 贵女逆袭
- style mode: 半写实插画 或 写实古装
- relationship: 后宫压迫 / 贵族上位 / 女性权谋
- title need: 直接带字成图

Recommended title-layer output:

```markdown
标题层说明：
- 主标题：贵妃掌局
- 字形家族：宫廷暖金竖排字
- 自动匹配依据：古言权谋、贵气宫廷、女性上位
- 标题位置：右侧竖排
- 字体风格：宫廷书写感展示字
- 字体效果：暖金浅浮雕、细砂金属纹理、边缘提亮
- 副标题：无
- 避让要求：不要遮挡发冠、凤钗、眼睛和宫廷礼服关键纹样
- 字符要求：竖排节奏稳定、贵气、不可廉价镀金
```

Useful title sentence:

```text
在画面右侧保留竖排标题区，直接渲染中文剧名“贵妃掌局”。根据宫廷权谋与贵女上位气质，自动匹配“宫廷暖金竖排字”，字形稳定庄重，表面使用暖金浅浮雕和细砂金属纹理，强调贵气和宫廷封面感。默认只渲染剧名，不额外添加副标题。
```

## Few-Shot 4: Blade-Written Emotional Hand Title

Input pattern:

- genre: 疯批虐恋 / 黑化追妻 / 高情绪反转
- style mode: 写实电影感 或 半写实插画
- relationship: 强情绪撕扯 / 爱恨失控
- title need: 直接带字成图

Recommended title-layer output:

```markdown
标题层说明：
- 主标题：野玫瑰从不低头
- 字形家族：疯批刀锋手写字
- 自动匹配依据：疯批虐恋、黑化反击、情绪爆发
- 标题位置：上左到中部斜向展开
- 字体风格：刀锋爆写手写字
- 字体效果：干刷白字、飞白边缘、少量擦笔纹理、不做重金属
- 副标题：无
- 避让要求：不要遮挡嘴部、眼神对视区、掐手腕等冲突动作
- 字符要求：笔势必须有失控张力，但仍可读，不要写成随意草稿
```

Useful title sentence:

```text
在保留人物脸部可读性的前提下，直接渲染中文剧名“野玫瑰从不低头”。根据疯批虐恋和黑化反击气质，自动匹配“疯批刀锋手写字”，使用干刷白字与飞白边缘，强化情绪爆发感，不要做沉重金属，也不要变成普通温柔手写体。
```

## Few-Shot 5: High-Contrast Elegant Display

Input pattern:

- genre: 高奢悬疑 / 冷欲都市 / 宿命感女频
- style mode: 半写实插画 或 高级写实
- relationship: 冷对峙 / 禁欲拉扯 / 命运纠缠
- title need: 直接带字成图

Recommended title-layer output:

```markdown
标题层说明：
- 主标题：月色不驯
- 字形家族：高奢细锋展示字
- 自动匹配依据：冷欲高奢、宿命感、女频高级悬疑
- 标题位置：上中
- 字体风格：高反差都市展示字
- 字体效果：冷光银边、极浅辉光、干净高级分离，不做厚重立体
- 副标题：无
- 避让要求：不要压住睫毛、珠宝、锁骨和面部轮廓线
- 字符要求：线条优雅、缩略图可读、不能显得软弱无力
```

Useful title sentence:

```text
在上中区域直接渲染中文剧名“月色不驯”。根据冷欲高奢和宿命悬疑气质，自动匹配“高奢细锋展示字”，字形高反差、细锋利落，表面使用冷光银边和极浅高级分离辉光，保持疏离、贵气和高级封面感。
```

## Few-Shot 6: Retro Rounded Urban Comedy Display

Input pattern:

- genre: 甜喜 / 沙雕 / 反套路总裁 / 后妈文学
- style mode: 动漫卡通 / 轻商业写实 / 轻插画
- relationship: 反差萌 / 轻松互怼 / 家庭喜感
- title need: 直接带字成图

Recommended title-layer output:

```markdown
标题层说明：
- 主标题：不霸气总裁与咸鱼后妈
- 字形家族：复古甜喜圆润字
- 自动匹配依据：反套路轻喜剧、都会甜感、轻松反差关系
- 标题位置：上中
- 字体风格：圆润复古都会展示字
- 字体效果：奶油珐琅、柔和高光、轻招牌感，不要幼儿贴纸感
- 副标题：无
- 避让要求：不要压住夸张表情、搞笑手势和核心互动动作
- 字符要求：饱满圆润、轻松好读、有都市甜喜节奏
```

Useful title sentence:

```text
在保留上中标题安全区的前提下，直接渲染中文剧名“不霸气总裁与咸鱼后妈”。根据反套路总裁轻喜剧气质，自动匹配“复古甜喜圆润字”，字形饱满圆润，表面使用奶油珐琅与轻微招牌感高光，保持轻松、都会、可爱但不低幼的商业封面感。
```

## Stability Rule

If the agent is uncertain between two families:

- prioritize story hook over random aesthetics
- prioritize relationship tone over generic genre labels
- prioritize readability over special effects
- use the plainer material option first

Wrong priority order:

- special effect first
- material first
- random “酷炫字体” first

Correct priority order:

- story
- relationship
- glyph family
- placement
- material
- optional subtitle
