# Poster Workflow

## 1. Intake

Collect only what is needed:

- 剧名: optional if the platform will add text later.
- 剧本/剧情梗概: prioritize conflict, relationship, reversal, and setting.
- 风格方向: urban, revenge, romance, CEO/power, ancient costume, fantasy, family, suspense, etc.
- 风格模式: realistic, semi-realistic illustration, anime/cartoon, or 3D anime.
- 画幅比例: default to 2:3 vertical poster for normal poster bases unless the user specifies another ratio or platform format.
- 角色三视图: primary character-design references; ask which turnaround belongs to which role.
- 风格/构图参考图: visual language references only; use for framing and finish, not for copying text or people.
- 动作/关系参考图: pose, motion, impact, force direction, and hierarchy references only; use for staging, not for copying identity or visual design.
- Output need: pure poster base, title-safe base, title rendered image, or redraw instructions.

If information is missing, proceed with a labeled assumption instead of blocking. Ask only when identity mapping or output type is impossible to infer.

If the user asks for a complete poster, determine whether they mean:

- clean title-free base
- title-safe base for later design
- directly rendered title poster

When the user says "偏卡通", "动漫", "二次元", "类 3D 动漫", "像游戏 key visual", or "不要写实", switch out of realistic mode explicitly instead of silently keeping cinematic realism.

### Output Routing

Before writing directions, classify the request into one of three routes:

- `无字底图`: no visible text in the image, but keep a clean title-safe area
- `带字成图`: title rendered in-image, usually only the main title unless the user asks for more copy
- `整图重绘`: preserve identity/relationship/composition logic from an existing poster and rebuild the whole image
- `扩图/改比例`: preserve the subject and extend the canvas/environment to a target ratio

If the user says "出封面", "做成品图", or "直接发平台", do not guess. Briefly judge whether they mean `带字成图` or just a cleaner `无字底图`.

If the user asks for outpainting, aspect-ratio conversion, horizontal/vertical expansion, or canvas extension, route to `扩图/改比例`:

- preserve the existing subject, pose, expression, identity design, lighting, and composition center
- extend only edge environment, background, atmosphere, and negative space unless the user explicitly asks to redraw the subject
- state the target ratio explicitly
- forbid new main subjects, face redesign, costume redesign, pose change, and center shift unless requested

For normal poster-base generation, use `2:3 竖版海报比例` by default:

- state the ratio in the complete prompt and platform-ready prompt
- do not state pixel dimensions unless the user asks for exact size
- if the user specifies 7:10, 3:4, 4:3, 9:16, 16:9, banner, platform-specific cover, or another ratio, use the specified ratio instead
- avoid ultra-narrow vertical frames, phone long-screenshot proportions, or ratios taller than 1:2 unless explicitly requested

If character turnarounds are provided, add a short role-binding block before directions:

- 三视图 A -> 女主
- 三视图 B -> 男主
- 三视图 C -> 反派长辈

If style/composition references are provided, add a short extraction block before directions:

- 风格参考图 1：只继承<构图 / 景别 / 光影 / 色调 / 标题安全区位置>
- 明确排除：<剧名文字 / 人物长相 / 服装细节 / 原海报道具 / logo / 水印 / 平台元素>

If action/relationship references are provided, add a short extraction block before directions:

- 动作参考图 1：只继承<姿态 / 动线 / 受力方向 / 接触关系 / 镜头角度 / 前后层级>
- 明确排除：<角色身份 / 物种或类型 / 配色 / 材质 / 文字 / 道具 / 原图剧情>

In multi-turn revision, keep an explicit latest-correction note when the user overwrites prior rules:

- 最新覆盖：<旧设定> -> <新设定>
- 后续平台词只保留新设定，不混写旧称呼、旧姿态、旧材质或旧构图。

If any critical information is missing but inferable, write one short assumption block:

- 假设风格模式：写实电影感
- 假设标题处理：先出无字底图
- 假设主视觉关系：女主主中心，男主后压迫

## 2. Story Hook Analysis

Extract:

- Core relationship: who pressures whom, who hides information, who reverses power.
- Visual conflict: confrontation, separation, pursuit, reveal, protection, betrayal, revenge, family bond.
- Market hook: why a viewer stops scrolling.
- Emotional temperature: cold revenge, warm romance, oppressive power, suspense, epic fantasy, light comedy.

Rewrite the hook into one visual sentence, for example:

> 女主在雨夜发现男主隐藏身份，两人隔着车窗与冷光对峙，关系从暧昧转为压迫。

## 3. Visual Dominance Routing

Before writing directions, decide what drives the poster image.

Allowed drivers only:

- `人物主导`: the selling point is face, identity, expression, status, or role appeal.
- `关系主导`: the selling point is tension between two or more roles.
- `道具主导`: the selling point is a concrete object, clue, or story device.
- `空间主导`: the selling point is location, architecture, vehicle, room, city, disaster space, or environmental pressure.
- `符号主导`: the selling point is an abstract sign, screen, projection, shadow, split, halo, countdown, fate mark, or visual metaphor.
- `动作主导`: the selling point is combat, chase, fall, impact, collision, escape, or protection.

Output a compact routing block before directions:

```markdown
画面主导关系判断：
- 第一主导：<人物主导 / 关系主导 / 道具主导 / 空间主导 / 符号主导 / 动作主导>
- 第二主导：<人物主导 / 关系主导 / 道具主导 / 空间主导 / 符号主导 / 动作主导>
- 禁用误读：<最容易跑偏的理解>
```

Routing behavior:

- If the task is a main poster or group poster, do not interpret interaction as physical action by default. Use gaze, facing direction, distance, overlap, foreground/background hierarchy, and shared narrative focus first.
- If `道具主导` is selected, decide whether the prop is the first narrative focus or a supporting clue. Show structure, state, position, scale, and lighting, but do not turn it into a product shot.
- If `空间主导` is selected, make the space serve as pressure, identity, action field, scale reference, or light source. Do not let it become empty scenery.
- If `符号主导` is selected, keep the symbol as background pressure or connective structure unless the user explicitly makes it the main subject. Protect face readability.
- Use `动作主导` only when the user explicitly asks for action-first scenes.
- Do not create topic-specific motif categories. Keep routing abstract so it can generalize across genres and reference sets.

## 4. Generate Three Directions

Always make directions different. Recommended set:

1. One direction should follow the primary dominance route.
2. One direction should combine the primary and secondary drivers differently.
3. One direction may test a safer commercial alternative, but it must not violate the forbidden misread.

Also vary style mode when useful:

- keep one safe commercial option
- use one more stylized option if the user allows animation/cartoon language
- use one stronger group-staging option when cast size is 3+

Each direction must include:

- Dominance logic.
- Style mode.
- Composition type.
- Character scale and shot size.
- Relationship staging.
- Scene and props.
- Lighting and atmosphere.
- Title-safe area position, defaulting to lower-center unless a special composition requires another placement.
- If relevant, title rendering suitability.
- Forbidden misread for that direction.
- Why this direction sells the drama.

Even if the user finally wants only one prompt, generate three directions first internally. Show all three unless the user explicitly asks for concise output. The three directions should not be the same composition with different adjectives.

## 5. Build Poster Base Prompt

The prompt must describe visible image content, not abstract adjectives. Include:

- Format: Chinese short-drama commercial poster base, plus the chosen style mode.
- Aspect ratio: default 2:3 vertical poster ratio unless user-specified.
- Characters: role count, hierarchy, posture, expression, reference-lock rule, face readability.
- Composition: shot size, camera angle, foreground/midground/background.
- Scene: location, time, props, spatial pressure.
- Lighting: key light, rim light, color temperature, contrast, reflections.
- Commercial polish: high-end film poster, clean layers, strong visual focus.
- Title-safe area: clean lower-center area by default; use upper, side, or other areas only when the composition, platform format, title-rendered design, or supplied style reference clearly requires it.
- No text: no Chinese/English characters, logos, subtitles, watermarks.

When character turnarounds exist, change the writing strategy:

- write the prompt as a **turnaround-driven poster staging instruction**
- do not redesign the approved character with extra beauty or anatomy invention
- avoid adding feature descriptors that are not required for design preservation
- do not "optimize" the character into different facial proportions, body proportions, species traits, materials, color blocking, clothing design, age feel, or hairstyle
- only describe appearance when it is already visible in the turnaround and necessary for role binding
- prefer `表情 / 视线 / 姿态 / 景别 / 光影 / 站位 / 关系张力`
- for platform-ready prompts, do not write concrete clothing style, color, material, era, jewelry, headwear, armor, robe, uniform, or silhouette by default; use `服装造型按角色参考图，不重新设计服装`
- if the user explicitly wants clothing identifiers in the text, keep them short and preservation-focused, and add `不重新设计 / 不额外改造 / 不升级服装`
- avoid replacing the approved design with generic beauty or realism tags unless the user explicitly requested such a transformation

Useful turnaround-safe phrasing:

- 按角色三视图设定生成
- 保持角色三视图中的轮廓、比例、材质、配色、发型和整体气质不变
- 服装造型按角色参考图，不重新设计服装
- 强调海报构图、关系、动作和光影，不额外改写角色设定
- 以角色三视图一致性为最高优先级

When style/composition references exist, change the writing strategy again:

- treat them as **abstract visual references**, not content references
- extract only reusable visual structure: framing, layout density, near-mid-far layering, title-safe area shape, lighting logic, and finish level
- do not reverse-engineer the sample's title text, character look, wardrobe story, prop story, or exact scene narrative into the new prompt
- if the sample contains people, describe them only as `前景主角占位 / 双人对峙关系 / 群像层级` rather than as specific faces or costumes
- if the sample contains text, explicitly exclude it unless the user asked to inherit that exact title treatment

Useful style-reference phrasing:

- 参考该图的构图节奏与光影组织，不继承图中文字和人物形象
- 只借鉴版式、镜头距离、留白位置和商业完成度
- 不反推参考图中的剧名、标题文案、角色长相和剧情道具

When action/relationship references exist, change the writing strategy:

- treat them as **staging references**, not design references
- inherit pose, line of action, force direction, contact/impact relationship, rhythm, camera angle, and near-mid-far hierarchy
- do not inherit identity, species/type, temperament, era feel, profession feel, style finish, face, costume, colors, materials, props, title text, or plot content from the reference
- rewrite meta phrases like `参考动作图` into direct result-state staging
- for high-motion poses, specify camera angle, center of gravity, limb/edge positions, motion direction, expression state, and motion-blur boundary

Useful action-reference phrasing:

- 主体沿<动线方向>形成<动作张力>
- <角色A>位于<位置>，<角色B>位于<位置>，两者形成<受力/追逐/压迫/保护/击中>关系
- 镜头沿<角度>捕捉<冲刺 / 回望 / 撞击 / 拉扯 / 护住>瞬间
- 不继承动作参考图中的角色外形、颜色、道具和文字信息
- 不继承动作参考图中的人物气质、年代感、职业感和风格质感

If style mode is not realistic:

- describe line quality, shape language, rendering mode, cel shading, painterly shading, or 3D anime material polish
- remove realism-only skin language unless the user wants semi-realistic treatment
- keep character hierarchy readable at thumbnail size
- keep the poster commercial, not like a random fan art screenshot

## 4b. Build Title-Rendered Version

Use this only when the user explicitly wants title text inside the final poster.

Include:

- title glyph family
- title material treatment
- exact title placement
- title size hierarchy
- font style direction
- subtitle rule if needed
- avoidance rules so title does not block faces
- anti-garbled-character language

Recommended practice:

- first write a clean poster-base prompt
- then write a short title-rendering extension
- if possible, treat title as a separate compositing layer
- select the title glyph family before selecting material effects
- keep glyph family stable and let material change with poster tone

## 5. Character Consistency

When character turnarounds exist:

- Bind each turnaround to a named role before prompt writing.
- State that design consistency outranks style creativity.
- Ask for 1 strongest approved turnaround set per key role if too many versions are supplied.
- Require consistent silhouette, proportions, materials, color blocking, hairstyle, and general temperament.
- Do not add decorative anatomy or beauty wording that can pull the model away from the turnaround.
- Prefer staging descriptors over appearance-rewrite descriptors: expression, gaze direction, chin lift, shoulder angle, hand action, body orientation, camera distance, and light hierarchy.
- If a role turnaround is weak or ambiguous, say that explicitly and keep the appearance description even shorter rather than compensating with invented traits.
- For anime/cartoon/3D anime, keep identity consistency through silhouette, face structure, eye spacing, palette, material language, and temperament rather than forcing realism.
- If the poster has many characters, prioritize must-appear roles and allow secondary figures to be less detailed.

For non-human, creature, mechanical, object, or heavily designed characters:

- preserve the approved design's silhouette, structural proportions, category-defining markers, material language, palette, and temperament
- lock visible high-drift local identifiers: face markings, color-block boundaries, eye area, nose/mouth or front structure, ear/horn/tail/limb tips, special marks, and other approved local features
- use scene, posture, lighting, and expression/attitude to create drama instead of redesigning anatomy or type
- add negative constraints only against adjacent archetypes that the model is likely to confuse with the approved design
- keep this branch conditional; do not apply creature/object-specific constraints to ordinary human-cast posters

When the story defines identity links between roles:

- true form / avatar / incarnation / companion form / summoned form / mirror form / spirit counterpart describe relationship, not automatic appearance mutation
- keep each role's referenced design intact unless the user explicitly asks for hybridization or transformation
- express the relationship through staging: gaze, distance, blocking, shared light, shadow overlap, reflection, echoing pose, or composition hierarchy
- avoid inventing master-pet, guardian, romantic, hostile, or ownership dynamics unless the user states that relationship

## 5a. Style/Composition Reference Handling

When style/composition references exist:

- label them separately from character references
- write what is allowed to inherit and what is forbidden to inherit
- allowed: composition, cropping, shot size, hierarchy, negative space, color mood, lighting logic, texture polish
- forbidden: visible text, title wording, character identity specifics from the sample, face traits, costume specifics, jewelry specifics, logo, watermark, QR code, platform marks, reference-plot props
- if the sample poster is very specific, abstract it one level up before prompt writing
- prefer phrases like `上中留白压标题`, `双人中近景对峙`, `冷暖对冲布光`, `群像阶梯层级`

## 5b. Multi-Turn Override And Material State

When the user corrects a prior rule, the latest correction wins:

- replace old names, object types, poses, colors, material states, title rules, and focus hierarchy in the next platform prompt
- do not keep both versions for safety
- if the user says the older version should return, treat that as a new latest correction

When the user requests a material-state transformation, specify both preserved identity and transformed state:

- Solid body: physical volume, surface material, contact shadows, scene lighting integration.
- Hologram/projection: opacity level, scan/light texture, edge glow, internal transparency, no physical mass unless requested.
- Energy/spirit form: preserved silhouette or palette if requested, translucent body, luminous edge, inner flow, partial dissipation, non-solid material.
- Shadow/silhouette form: visible volume cues, occlusion, rim reflection, atmospheric depth, not a flat black cutout unless requested.

Setting elements such as UI panels, projections, symbols, props, and background threats are focus-controlled:

- if the user specifies a main subject, secondary setting elements must be smaller, dimmer, softer, lower contrast, or spatially behind/around it
- if the user specifies the setting element as the main visual, then it may become larger, brighter, sharper, or centered

## 5c. Multi-Character Strategy

When cast size is 3+:

- decide who owns the visual center before prompt writing
- set strict role priority: must-read, support-read, atmosphere-only
- keep character binding and identity consistency above crowd energy, comedy business, exaggerated motion, and background density
- if more than one role is a commercial selling point, state their shared or relative shot size before prompt writing
- do not push a selling character into background blur, tiny face scale, or vague second-focus language unless the user explicitly wants that hierarchy
- avoid equal spacing and equal brightness
- use depth, overlap, and light hierarchy to prevent "all characters lined up"
- use one shared light source or clearly related light logic across all roles
- keep color temperature, atmospheric perspective, shadow direction, contact/occlusion, and edge softness consistent across layers
- when adding a new role behind or around existing subjects, state how that role integrates into the same scene space instead of reading like a pasted cutout
- simplify minor faces before sacrificing the lead role readability

## 6. Whole-Image Redraw

Use for "改这张图", "基于这张海报重做", "保留人物换氛围", or "整图重绘".

Structure:

- Preserve: identity, number of people, main relationship, rough composition, title-safe area.
- Change: atmosphere, location, lighting, staging, shot distance, emotion, visual cleanliness.
- If style conversion is requested, name both the source style and target style clearly.
- Generate 3 variants when useful: stable version, stronger emotion version, more cinematic space version.
- Do not promise local edits unless the user asks for mask/region editing and the tool supports it.

## 7. Title Layer

Default recommendation: keep image generation title-free and add title later in the platform or design tool.

If title rendering is required:

- Keep text short and readable.
- Avoid over-complex metallic effects that harm legibility.
- Separate title prompt from poster base prompt where possible.
- Recompose title and base after selecting the best base.
- Auto-match the base glyph family first from the font library.
- Then choose material treatment according to the poster look.
- Specify whether the title belongs to a hard-edged metallic family, power-calligraphy family, palace gold family, blade-written emotional family, elegant display family, or rounded comedy family.
- Explicitly forbid乱码, broken strokes, wrong Chinese characters, and face overlap.

### 7a. Automatic Glyph-Family Matching

When the user asks for a title-rendered poster and does not name a font directly, match automatically:

- hard urban revenge / dragon king / bodyguard / war-god stories:
  - prefer `Hard-Edge Battle-Damaged Metallic Display`
- authority / king-return / overpowering male lead / mythic dominance:
  - prefer `Power-Calligraphy Stone-Metal Title`
- palace intrigue / aristocratic costume / royal heroine rise:
  - prefer `Palace Gold Vertical Title` or the palace branch of the power-calligraphy family
- dark romance / blackening / chase-wife crematorium / emotional reversal:
  - prefer `Blade-Written Emotional Hand Title`
- luxury suspense / cold high-end female drama / fate-heavy elegant stories:
  - prefer `High-Contrast Elegant Display`
- light comedy / anti-trope romance / rounded sweet urban stories:
  - prefer `Retro Rounded Urban Comedy Display`

Then assign material by poster finish:

- cold realistic action: silver metal, scratched steel, restrained bevel
- premium costume: warm gold foil, shallow emboss, refined highlight
- emotional hand-written posters: mostly dry-brush white or ink-like bright title, not heavy metal
- luxury cool-tone drama: thin silver edge, cold glow, restrained high-end finish
- comedy and light romance: cream, enamel, soft gloss, retro sign-paint feeling
- stylized 3D anime: premium highlight, layered glow, controlled dimensional finish, never toy-like
