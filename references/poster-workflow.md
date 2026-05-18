# Poster Workflow

## 1. Intake

Collect only what is needed:

- 剧名: optional if the platform will add text later.
- 剧本/剧情梗概: prioritize conflict, relationship, reversal, and setting.
- 风格方向: urban, revenge, romance, CEO/power, ancient costume, fantasy, family, suspense, etc.
- 角色照片: actor identity references; ask which role each photo belongs to.
- 参考图: visual language only. Do not copy unrelated people, text, logos, or platform layout.
- Output need: pure poster base, title-safe base, title rendered image, or redraw instructions.

If information is missing, proceed with a labeled assumption instead of blocking. Ask only when identity mapping or output type is impossible to infer.

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

Each direction must include:

- Composition type.
- Character scale and shot size.
- Relationship staging.
- Scene and props.
- Lighting and atmosphere.
- Title-safe area position.
- Why this direction sells the drama.

## 4. Build Poster Base Prompt

The prompt must describe visible image content, not abstract adjectives. Include:

- Format: Chinese short-drama commercial poster base, cinematic realism.
- Characters: role count, hierarchy, posture, expression, wardrobe, face readability.
- Composition: shot size, camera angle, foreground/midground/background.
- Scene: location, time, props, spatial pressure.
- Lighting: key light, rim light, color temperature, contrast, reflections.
- Commercial polish: high-end film poster, clean layers, strong visual focus.
- Title-safe area: clean upper/side/bottom area depending on direction.
- No text: no Chinese/English characters, logos, subtitles, watermarks.

## 5. Character Consistency

When actor/reference photos exist:

- Bind each photo to a named role before prompt writing.
- State that identity consistency outranks style creativity.
- Ask for 1-2 strongest reference photos per key role if too many are supplied.
- Require consistent face shape, age, hairstyle, expression type, and general temperament.
- If the poster has many characters, prioritize must-appear roles and allow secondary figures to be less detailed.

## 6. Whole-Image Redraw

Use for "改这张图", "基于这张海报重做", "保留人物换氛围", or "整图重绘".

Structure:

- Preserve: identity, number of people, main relationship, rough composition, title-safe area.
- Change: atmosphere, location, lighting, wardrobe, shot distance, emotion, visual cleanliness.
- Generate 3 variants when useful: stable version, stronger emotion version, more cinematic space version.
- Do not promise local edits unless the user asks for mask/region editing and the tool supports it.

## 7. Title Layer

Default recommendation: keep image generation title-free and add title later in the platform or design tool.

If title rendering is required:

- Keep text short and readable.
- Avoid over-complex metallic effects that harm legibility.
- Separate title prompt from poster base prompt where possible.
- Recompose title and base after selecting the best base.
