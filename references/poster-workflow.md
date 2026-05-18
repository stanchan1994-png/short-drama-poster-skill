# Poster Workflow

## 1. Intake

Collect only what is needed:

- 剧名: optional if the platform will add text later.
- 剧本/剧情梗概: prioritize conflict, relationship, reversal, and setting.
- 风格方向: urban, revenge, romance, CEO/power, ancient costume, fantasy, family, suspense, etc.
- 风格模式: realistic, semi-realistic illustration, anime/cartoon, or 3D anime.
- 角色照片: actor identity references; ask which role each photo belongs to.
- 参考图: visual language only. Do not copy unrelated people, text, logos, or platform layout.
- Output need: pure poster base, title-safe base, title rendered image, or redraw instructions.

If information is missing, proceed with a labeled assumption instead of blocking. Ask only when identity mapping or output type is impossible to infer.

When the user says "偏卡通", "动漫", "二次元", "类 3D 动漫", "像游戏 key visual", or "不要写实", switch out of realistic mode explicitly instead of silently keeping cinematic realism.

## 2. Story Hook Analysis

Extract:

- Core relationship: who pressures whom, who hides information, who reverses power.
- Visual conflict: confrontation, separation, pursuit, reveal, protection, betrayal, revenge, family bond.
- Market hook: why a viewer stops scrolling.
- Emotional temperature: cold revenge, warm romance, oppressive power, suspense, epic fantasy, light comedy.

Rewrite the hook into one visual sentence, for example:

> 女主在雨夜发现男主隐藏身份，两人隔着车窗与冷光对峙，关系从暧昧转为压迫。

## 3. Generate Three Directions

Always make directions different. Recommended set:

1. **Power portrait**: one protagonist dominates the frame; best for revenge, identity reversal, CEO/power stories.
2. **Relationship confrontation**: two people in opposing positions; best for romance, betrayal, pursuit, coercion.
3. **Group/pyramid composition**: hierarchy and hidden relationships; best for family, palace, team, fantasy, multi-character drama.

Also vary style mode when useful:

- keep one safe commercial option
- use one more stylized option if the user allows animation/cartoon language
- use one stronger group-staging option when cast size is 3+

Each direction must include:

- Style mode.
- Composition type.
- Character scale and shot size.
- Relationship staging.
- Scene and props.
- Lighting and atmosphere.
- Title-safe area position.
- Why this direction sells the drama.

## 4. Build Poster Base Prompt

The prompt must describe visible image content, not abstract adjectives. Include:

- Format: Chinese short-drama commercial poster base, plus the chosen style mode.
- Characters: role count, hierarchy, posture, expression, wardrobe, face readability.
- Composition: shot size, camera angle, foreground/midground/background.
- Scene: location, time, props, spatial pressure.
- Lighting: key light, rim light, color temperature, contrast, reflections.
- Commercial polish: high-end film poster, clean layers, strong visual focus.
- Title-safe area: clean upper/side/bottom area depending on direction.
- No text: no Chinese/English characters, logos, subtitles, watermarks.

If style mode is not realistic:

- describe line quality, shape language, rendering mode, cel shading, painterly shading, or 3D anime material polish
- remove realism-only skin language unless the user wants semi-realistic treatment
- keep character hierarchy readable at thumbnail size
- keep the poster commercial, not like a random fan art screenshot

## 5. Character Consistency

When actor/reference photos exist:

- Bind each photo to a named role before prompt writing.
- State that identity consistency outranks style creativity.
- Ask for 1-2 strongest reference photos per key role if too many are supplied.
- Require consistent face shape, age, hairstyle, expression type, and general temperament.
- For anime/cartoon/3D anime, keep identity consistency through hairstyle, face shape, eye spacing, color palette, and temperament rather than forcing full photo likeness.
- If the poster has many characters, prioritize must-appear roles and allow secondary figures to be less detailed.

## 5b. Multi-Character Strategy

When cast size is 3+:

- decide who owns the visual center before prompt writing
- set strict role priority: must-read, support-read, atmosphere-only
- avoid equal spacing and equal brightness
- use depth, overlap, and light hierarchy to prevent "all characters lined up"
- simplify minor faces before sacrificing the lead role readability

## 6. Whole-Image Redraw

Use for "改这张图", "基于这张海报重做", "保留人物换氛围", or "整图重绘".

Structure:

- Preserve: identity, number of people, main relationship, rough composition, title-safe area.
- Change: atmosphere, location, lighting, wardrobe, shot distance, emotion, visual cleanliness.
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
