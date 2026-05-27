# Prompt Spec

## Direction Output Template

```markdown
### 方向 1：<方向名>
- 核心钩子：<一句话>
- 风格模式：<写实电影感 / 半写实插画 / 动漫卡通 / 类3D动漫>
- 构图：<单人权力肖像 / 双人对峙 / 群像金字塔 / 豪门空间压迫等>
- 人物：<角色数量、主次关系、姿态、表情>
- 场景：<空间、时间、关键道具>
- 光影：<冷暖、主光、轮廓光、背景层次>
- 标题安全区：<上方 / 左上 / 右下 / 中下等>
- 带字适配：<适合直接带字 / 更适合无字底图后二次排版>
- 适合原因：<为什么这个方向更能卖剧>
```

## Task Judgment and Assumptions

Use this block before directions when it improves execution stability.

```markdown
任务判断：
- 输出类型：<无字底图 / 带字成图 / 整图重绘>
- 风格模式：<写实电影感 / 半写实插画 / 动漫卡通 / 类3D动漫>

假设：
- <只写必要假设；若无可省略>
```

If character turnarounds exist, add:

```markdown
参考图绑定：
- <三视图A> -> <角色名>
- <三视图B> -> <角色名>
```

If style/composition references exist, also add:

```markdown
风格参考提取：
- <风格参考图1>：继承<构图 / 景别 / 光影 / 色调 / 留白位置>
- 排除继承：<图中文字 / 人物长相 / 服装细节 / 道具剧情 / logo / 水印>
```

If action/relationship references exist, also add:

```markdown
动作参考提取：
- <动作参考图1>：继承<姿态 / 动线 / 受力方向 / 接触关系 / 镜头角度 / 前后层级>
- 排除继承：<角色身份 / 类型或物种 / 配色 / 材质 / 道具 / 文字 / 原图剧情>
```

If the user has corrected an earlier rule in the same thread, add:

```markdown
最新覆盖：
- <旧设定> -> <新设定>
- 后续平台词只保留新设定
```

## Chinese Complete Prompt

Use one paragraph. Example structure:

```text
中文短剧竖版商业海报底图，<风格模式>，人物关系一眼可读。画面为<构图类型>，<主角>占据画面<比例>，<对手/恋人/配角>位于<位置>形成<关系张力>。场景设置在<地点/时间>，可见<关键道具/空间元素>，背景只保留服务剧情的元素。镜头为<景别和角度>，人物脸部清晰，表情体现<情绪>。光影采用<光线方案>，整体氛围<情绪词>。如果是写实或半写实，材质细节包括<服装/皮肤/玻璃/雨水/金属/布料>；如果是动漫卡通或类3D动漫，则强调<线条 / 赛璐璐明暗 / 发丝块面 / 眼神设计 / 三维材质高光 / 角色轮廓层次>。保留<标题安全区位置>干净留白，方便后期添加剧名。不要生成任何可见文字、汉字、英文、logo、水印、字幕、平台标识；不要廉价拼贴、不要网红滤镜、不要低清模糊、不要畸形手指、不要重复人物。
```

Length rule:

- `Chinese Complete Prompt` should normally stay within **1900 Chinese characters**.
- If both `Chinese Complete Prompt` and `Platform-Ready Prompt` are present, the `Platform-Ready Prompt` has higher priority for strict length control.

If character turnarounds exist, prepend a short design-lock sentence and simplify appearance language:

```text
按角色三视图设定生成，保持角色三视图中的轮廓、比例、材质、配色、发型和整体气质不变，不额外改写角色设定。重点强化<构图 / 关系 / 表情 / 姿态 / 服装 / 光影>。
```

Turnaround writing rules:

- Do not add beautification tags unless explicitly requested.
- Do not add invented anatomy, species correction, material replacement, age reduction, or face-shape rewrite keywords.
- Use expression, posture, wardrobe, props, and lighting to create drama instead of rewriting the design.
- Do not turn design constraints into assistant commentary. Write the constraint directly into the scene description.
- If two roles have an identity link such as true form, avatar, incarnation, companion form, summoned form, mirror form, or spirit counterpart, preserve both role designs independently unless the user asks for a hybrid or transformed appearance.
- Express identity links through staging and composition instead of appearance mutation.

Style/composition reference writing rules:

- Extract only layout and finish, not sample content.
- Do not reverse-engineer title words, face traits, costume specifics, or sample props into the new prompt.
- If needed, mention the borrow explicitly: `参考其双人对峙构图与上方留白，不继承原图人物与文字内容。`
- When that borrow is merged into the final platform-ready prompt, rewrite it as pure visual instruction instead of meta-commentary.

Action/relationship reference writing rules:

- Extract only pose, motion path, force direction, contact/impact relationship, camera angle, and foreground/background hierarchy.
- Do not inherit character identity, species/type, face, costume, color, material, props, title text, or original plot content.
- Convert `参考动作图` into a direct result-state sentence.
- For high-motion poses, include camera angle, center of gravity, limb/edge positions, motion direction, expression state, and whether motion blur is allowed or limited.

Outpainting/aspect-ratio conversion writing rules:

- State the target ratio explicitly.
- Preserve subject identity, pose, expression, design, lighting, and composition center.
- Extend only edge environment, background, atmosphere, and negative space unless subject redraw is requested.
- Forbid new main subjects, face redesign, costume redesign, pose change, and center shift unless requested.

Non-human/designed-character local-lock rules:

- When visible, lock high-drift local identifiers such as face markings, color-block boundaries, eye area, nose/mouth or front structure, ear/horn/tail/limb tips, special marks, and other approved local features.
- Use local-lock language only when the role is non-human, creature, mechanical, object-like, or heavily designed; do not apply it to ordinary human portraits unless the user identifies a specific local mark.

Multi-turn override writing rules:

- The latest explicit user correction overrides older prompt rules.
- Remove old names, object types, poses, colors, material states, title rules, and focus hierarchy that conflict with the latest correction.
- Do not keep both old and new versions in the same platform-ready prompt.

Material-state writing rules:

- For hologram/projection/energy/spirit/shadow/silhouette states, say what is preserved and what changes.
- Specify color retention or removal, opacity, edge behavior, internal structure, dissipation, and whether the body is physically solid.
- If the user asks to preserve original color while changing material state, state both constraints in one sentence.

## Platform-Ready Prompt

This is the only block intended for direct use on image-generation platforms.

Rules:

- Keep only image-generation instructions.
- Do not include workflow labels, versioning, task names, direction names, routing judgments, or reference-strategy metadata.
- Do not include JSON keys or explanatory headers.
- Merge the useful parts of `Chinese Complete Prompt`, title instructions if needed, and negative constraints into one clean prompt block.
- Do not include assistant/user dialogue residue or explanation language.
- Ban phrases like `你给的`, `你提供的`, `参考你提供的`, `如果你要`, `我可以`, `下面给你`, `应该改成`, `视觉上让人一眼明白`, `这是XX设定`, `这一版`, `再给你一版`, `改为`, `改成`, `保持为`, `参考示例图`, `按示例图`.
- Avoid supervisory phrasing such as `必须严格参考`, `需要让人看出`, `必须明确可见`. Convert them into direct scene constraints.
- Hard limit: keep the final `Platform-Ready Prompt` within **1900 Chinese characters** unless the user explicitly asks for a longer platform version.
- In revision mode, output the final desired picture directly. Do not describe the act of modifying from an old version to a new version.

Language shape for platform-ready prompts:

- Use declarative image instructions.
- Each sentence should describe visible content, composition, lighting, material, or explicit negative constraint.
- Do not explain why a choice exists.
- Do not mention the user, the assistant, the workflow, the revision process, or the reference handoff.
- Do not paste casual user phrasing directly. Convert it into visible pose, gaze, distance, contact, motion, blocking, lighting, or hierarchy.

Multi-character integration rules:

- For layered or multi-character scenes, state shared light source, color temperature, atmospheric perspective, contact/occlusion, scale relationship, and edge softness.
- Newly added background or side characters must belong to the same scene space through light, shadow, occlusion, and depth cues.
- If a character is emotionally distant, supportive, threatening, curious, or detached, express it through gaze, posture, distance, and lighting instead of abstract labels alone.

Compression priority when over limit:

1. Remove repeated emotional adjectives.
2. Merge repeated negative constraints.
3. Shorten transition words and helper phrases.
4. Keep visual weight, shot size, face clarity, reference locks, character hierarchy, composition, lighting, scene, and title-safe-area before secondary polish language.
5. Keep identity-lock, selling-character readability, and key conflict information even in compressed form.

Visual-weight writing rules:

- If the user says a role is a selling point, make that role readable through shot size, face clarity, focus, light, and foreground/midground placement.
- If two roles must share visual importance, state that they are in the same or comparable shot size and neither is pushed into background blur.
- Keep small foreground mascots, props, or memory points readable without stealing the main human-character focus unless the user says otherwise.

Bad example:

```text
必须严格参考你给的角色卡，视觉上让人一眼明白这是系统爽文设定，如果你要我可以再给你一版压缩版。
```

Good example:

```text
前景主体为<主角本体>，保持角色三视图中的轮廓、比例、材质、配色和关键识别点。<辅助设定元素>位于主角后方或侧后方，亮度与清晰度低于主角，形成前实后虚的主次关系。
```

Revision-state conversion examples:

```text
<辅助形态>改为主角身后偏上方的大型虚影
-> <辅助形态>位于主角身后偏上方，形成大型虚影层

<背景威胁>保持为后景上半部的巨大正面黑影
-> <背景威胁>位于后景上半部，呈巨大正面黑影，并保留体积、厚度、边缘反光和空间遮挡

动作关系参考示例图
-> <主体A>沿前方动线冲出，<主体B>在后上方顺势上扬，形成前低后高的冲势关系
```

Recommended note above the block:

```markdown
平台投喂版 Prompt：
- 可直接用于生图平台
- 不包含工作流元信息
```

## Workflow JSON

This block is for humans and agents, not for direct image-platform input.
For beginner-facing output, it should be treated as optional advanced info and collapsed/folded by default whenever the surface supports that behavior.

Always put a warning label immediately above it:

```markdown
工作流 JSON（不要直接用于生图平台）：
```

Recommended display note:

```markdown
工作流 JSON（默认折叠，可选查看）：
- 仅用于复盘、定向改词、agent 续改
- 不要直接用于生图平台
```

Keep JSON keys stable; values should be Chinese.

```json
{
  "_workflow_only": {
    "用途": "工作流元信息，不要直接用于生图平台",
    "版本": "short-drama-poster-v1",
    "任务": "短剧海报底图",
    "方向名": "",
    "输入判断": {
      "输出类型": "",
      "风格模式": "",
      "是否带标题": ""
    },
    "参考图策略": {
      "角色三视图": [],
      "风格参考图": [],
      "风格图可继承": [],
      "风格图禁止继承": []
    }
  },
  "平台可用内容": {
    "任务": "短剧海报底图",
    "风格模式": "",
    "构图类型": "",
    "情绪温度": "",
    "人物": {
      "出镜人数": "",
      "主次关系": "",
      "人物占比": "",
      "身份一致性": "",
      "外貌描述策略": ""
    },
    "画面": {
      "景别": "",
      "镜头": "",
      "场景": "",
      "关键道具": "",
      "前中后景": ""
    },
    "光影": {
      "主光": "",
      "轮廓光": "",
      "色调": "",
      "材质细节": [],
      "渲染特征": []
    },
    "标题安全区": {
      "位置": "",
      "要求": "保持干净，不生成文字"
    },
    "参考图绑定": [],
    "负向约束": []
  }
}
```

Recommended value for `外貌描述策略` when character turnarounds exist:

```text
以角色三视图一致性为最高优先级，只描述表情、姿态、服装、景别和光影，不补充会改变设定的外貌或材质细节。
```

Recommended values when style/composition references exist:

```text
风格图可继承：构图、景别、留白、光影、色调、商业完成度。
风格图禁止继承：剧名文字、人物脸、服装细节、剧情道具、logo、水印、平台元素。
```

Suggested output note after JSON:

```markdown
使用说明：
- 直接投喂生图平台时，只使用“平台投喂版 Prompt”
- “工作流 JSON”默认折叠，仅用于存档、复盘、二次编辑或 agent 间传递
- 平台投喂版 Prompt 默认控制在 1900 字以内
```

## Title-Rendered Extension

Use when the user explicitly wants a poster with title text.

```markdown
标题层说明：
- 主标题：<剧名>
- 字形家族：<硬核战损金属切角字 / 权谋金石书法字 / 宫廷暖金竖排字 / 疯批刀锋手写字 / 高奢细锋展示字 / 复古甜喜圆润字>
- 自动匹配依据：<题材 / 情绪温度 / 风格模式 / 角色关系>
- 标题位置：<上中 / 左上 / 右上 / 中下>
- 字体风格：<在选中字形家族下的具体风格桶>
- 字体效果：<银灰战损金属 / 暖金浅浮雕 / 干刷白字 / 冷光银边 / 奶油珐琅 / 轻立体高光>
- 副标题：<默认无；只有用户明确要求时再填写文案内容>
- 避让要求：<不要遮挡眼睛、嘴部、关键手势、主道具>
- 字符要求：<中文正确、无乱码、边缘清晰、缩略图可读>
```

Example extension:

```text
在保留上方标题安全区的前提下，直接渲染中文剧名“隐婚继承”。根据都市权力、隐婚压迫和冷感商业海报气质，先自动匹配“硬核战损金属切角字”或“权谋金石书法字”中更合适的一支，并明确匹配依据；再在该字形家族内选择现代硬朗黑体式或霸气行草式的海报化风格桶，表面使用轻微银灰冷金属边缘和克制高光，字重明显但不过厚，保持高级商业海报感。默认只渲染剧名，不额外添加副标题、卖点文案、平台角标或集数信息。标题不要遮挡人物眼睛、嘴部和关键手势，不要出现乱码、错字、破碎笔画、平台标识或二维码。
```

## Whole-Image Redraw Template

```markdown
保留：
- 保留主要人物身份、人数和人物关系。
- 保留大致构图和标题安全区。
- 保留海报商业质感。
- 保留原图的人数层级和标题安全区逻辑。

改变：
- 目标氛围为<目标氛围>。
- 光线方案为<光线方案>。
- 场景设置为<目标场景>。
- 重点突出<情绪/冲突/道具/空间>。

完整改图提示词：
基于参考海报进行整图重绘，保留角色身份、人数、主要站位和关系张力，不改变核心角色三视图设定中的轮廓、比例、材质、配色、发型和气质。整体风格为<目标风格>，同时保留商业海报构图可读性。画面呈现<目标变化>……
```

Recommended redraw JSON additions:

```json
{
  "输入判断": {
    "输出类型": "整图重绘",
    "风格模式": "",
    "是否带标题": ""
  },
  "保留项": [],
  "改动项": [],
  "参考图绑定": []
}
```

## Negative Constraints

Use negative constraints only when they prevent common failures. Recommended default:

```text
不要生成任何可见文字、汉字、英文、logo、水印、字幕、平台标识；不要廉价拼贴、不要普通自拍照、不要PPT封面感、不要人物过小、不要背景压过人物、不要低清模糊、不要过曝、不要脏色块、不要畸形手指、不要重复人物、不要五官错乱。写实模式额外避免AI塑料皮肤；动漫/卡通模式额外避免崩脸、比例失衡、低幼廉价感；类3D动漫模式额外避免塑料玩偶感、手游登录页感、过度廉价特效。
```

If character turnarounds exist, add:

```text
不要擅自改变角色三视图中的轮廓、比例、种族特征、材质、配色、发型和整体气质；不要自动美化换设、不要过度磨皮、不要把原设角色改成陌生设计。
```

If style/composition references exist, add:

```text
不要照搬参考图中的剧名文字、标题文案、角色脸、服装细节、珠宝道具、logo、水印、二维码、平台角标；不要把风格参考图里的具体人物和剧情元素直接反推到新海报里。
```

If rendering title text directly in-image, add:

```text
不要乱码、不要错别字、不要断裂笔画、不要让标题压住人物眼睛和嘴部、不要过度发光、不要低端手游UI感。
```
