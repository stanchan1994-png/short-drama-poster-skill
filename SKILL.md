---
name: short-drama-poster
description: End-to-end Chinese short-drama poster workflow for AI agents. Use when creating or reviewing short-drama, web drama, micro drama, romance/revenge/urban/fantasy poster directions, multi-character compositions, realistic/anime/cartoon/3D-anime poster styles, title-rendered poster versions, image-generation prompts, JSON prompt structures, character-consistency rules, title-safe-area guidance, whole-image redraw instructions, or poster quality checklists for Chinese users and AI image platforms.
---

# Short Drama Poster

Use this skill to turn a short-drama brief, script, style direction, character turnarounds, or an existing poster into a practical AI poster workflow. Default to Chinese output unless the user asks otherwise.

If the user asks to `复盘`, `总结这次使用`, `整理这次对话`, `输出 case summary`, `输出复盘文件`, or anything similar, switch into **case-summary mode** instead of generating a new poster prompt.

The default mode is commercial short-drama realism, but this skill also supports:

- multi-character posters with clear hierarchy and role priority
- semi-realistic illustration posters
- anime/cartoon posters
- stylized 3D anime posters with commercial key-art polish
- title-rendered poster versions with Chinese typography guidance

## Core Workflow

1. Identify the strongest hook: relationship, power gap, reversal, revenge, identity reveal, forbidden love, family secret, or fantasy destiny.
2. Extract visual roles: protagonist, opponent/love interest, supporting power figure, child/family member, hidden antagonist.
3. Decide the visual mode first: realistic, semi-realistic illustration, anime/cartoon, or 3D anime.
4. Produce **3 distinct poster directions** before writing final prompts. Make the directions meaningfully different in composition, emotional temperature, commercial hook, and if useful, style execution.
5. Decide whether the output is a title-free base or a title-rendered final poster.
6. After a direction is chosen, produce a **Chinese complete prompt** and a **JSON structured prompt** for image platforms.
7. Before the final prompt, state a short **task judgment**: normal poster base, title-rendered poster, or whole-image redraw. If you made assumptions, label them explicitly instead of hiding them.
8. If references are provided, classify them first: **character turnaround reference**, **style/composition reference**, or **action/relationship reference**.
9. If character turnarounds are provided, output a short **reference-role binding** block before writing prompts so each image is tied to a named role.
10. Keep the image title-free by default: no rendered title text, no logo, no watermark, and a clean title-safe area.
11. If the user explicitly wants a poster with title text, generate both the poster-base prompt and a title-layer or title-rendered version with typography guidance. The default title-rendered version should contain only the main drama title unless the user explicitly asks for subtitle, slogan, platform line, or extra copy.
12. If title rendering is requested, auto-match a title glyph family from `references/font-library.md` based on genre, relationship tone, and style mode before assigning material treatment.
13. Material treatment for title-rendered posters must be derived from the poster look itself: same glyph family can render as silver metal, warm gold foil, dry-brush white, enamel, glow, or premium 3D highlight depending on story type.
14. If the user provides an existing poster, treat the task as whole-image redraw unless they explicitly ask for local masking. Preserve the requested identity/composition/style constraints and generate new redraw instructions.
15. Keep every prompt-like output block within **1900 Chinese characters** by default, because many image platforms have prompt-length limits.
16. Finish with a short quality checklist and concrete fixes.

## What To Read

- For the full staged process, read `references/poster-workflow.md`.
- For exact output formats, read `references/prompt-spec.md`.
- For review and acceptance criteria, read `references/quality-checklist.md`.
- For style branching, read `references/style-modes.md`.
- For title rendering rules, read `references/title-design.md`.
- For title glyph-family auto-matching, read `references/font-library.md`.
- For stable rendered-title output patterns, read `references/title-fewshots.md`.

## Default Output Shape

For a "复盘 / 总结 / case summary / 复盘文件" request, output:

1. Choose the smallest useful recap scope:
   - If the user says `轻量复盘`, `只复盘最近这一轮`, or the conversation is long and no final recap is requested, output **Light Recap** only.
   - If the user says `阶段复盘`, output **Stage Recap** for the current stage only.
   - If the user says `最终复盘`, `合并复盘`, `输出复盘文件`, or `Case Summary`, output the full **Case Summary**, preferably by merging existing light/stage recaps instead of rereading the whole conversation.
2. Never reread or summarize the entire long conversation unless the user explicitly asks for a full final summary.
3. For Light Recap, output one fenced markdown code block with only:
   - `## 轻量复盘`
   - `- 跑偏：`
   - `- 用户纠正：`
   - `- 后续状态：`
   - `- 可提炼问题：`
4. For Stage Recap, output one fenced markdown code block with only:
   - `## 阶段复盘`
   - `- 本阶段目标：`
   - `- 关键跑偏：`
   - `- 用户纠正：`
   - `- 后续状态：`
   - `- 最终有效约束：`
   - `- 可提炼问题：`
5. For full Case Summary, output a single fenced markdown code block.
6. Inside the full Case Summary code block, use this exact structure:
   - `# Case Summary`
   - `## 1. 本次任务`
   - `## 2. 原始输入关键信息`
   - `## 3. Skill 原始输出摘要`
   - `## 4. 用户关键纠正与回退点`
   - `## 5. 暴露出的具体问题`
   - `## 6. 结果判断`
   - `## 7. 可供规则迭代的结论`
7. Write only factual summary from the current conversation or current skill-use context.
8. Do not continue image creation or propose a new poster direction in recap mode.
9. Do not write greetings, encouragement, or extra explanation outside the code block.
10. Do not record every sentence from a long conversation. Record only skill-relevant failures, user corrections, later regressions, final effective constraints, and generated-result feedback.
11. In `## 4. 用户关键纠正与回退点`, use compact records such as `跑偏：... / 用户纠正：... / 后续状态：已修好|后续又回退|未验证 / 可提炼问题：...`.
12. In `## 5. 暴露出的具体问题`, list concrete observable failures only, not abstract taste judgments.
13. In `## 7. 可供规则迭代的结论`, separate conclusions into universal rules, conditional branch rules, and case-only notes. Do not directly turn case-specific details into global skill rules.
14. In `## 7. 可供规则迭代的结论`, write short actionable lines under:
   - `应新增的硬规则`
   - `应新增的条件分支规则`
   - `应补充的负面示例`
   - `应修改的默认输出方式`
   - `应删除或弱化的旧规则`
   - `仅作为案例备注，不应写入通用规则`

For a normal "make a poster prompt" request, output:

1. **Task judgment**: confirm this is a title-free base, title-rendered poster, or redraw task.
2. **Assumptions**: only when information is missing.
3. **Reference-role binding**: only when character turnarounds are provided.
4. **3 poster directions**: title, hook, style mode, composition, characters, scene, lighting, title-safe area.
5. **Recommended direction**: one concise reason.
6. **Chinese complete prompt** for the recommended direction.
7. **Platform-ready prompt**: a clean feed-ready prompt made only of image-generation instructions, with no workflow metadata, capped at **1900 Chinese characters**.
8. **Workflow JSON (collapsed by default)**: structured metadata for humans/agents; keep it compact, avoid unnecessary prose, and treat it as optional supporting info for advanced users.
9. **Negative constraints** and quality checklist.

For a "带标题成品图" or "直接做带字海报" request, output:

1. **Task judgment**.
2. **Assumptions**: only when needed.
3. **Reference-role binding**: only when references exist.
4. **3 poster directions** with title-safe-area reasoning.
5. **Recommended direction**.
6. **Poster-base Chinese prompt**.
7. **Title-rendered version** or title-layer instructions.
8. **Platform-ready prompt**: a clean feed-ready prompt made only of image-generation instructions, capped at **1900 Chinese characters**.
9. **Workflow JSON (collapsed by default)**: structured metadata for humans/agents; mark it clearly as not for direct image-platform input.
10. **Typography notes**: glyph family, material treatment, title style, placement, subtitle, billing, and avoidance rules.
11. **Quality checklist**.

For an "edit/redraw this poster" request, output:

1. **Task judgment**.
2. **What to preserve**.
3. **What to change**.
4. **Reference-role binding**: only when the user also supplies character turnarounds.
5. **Complete whole-image redraw prompt**.
6. **Platform-ready redraw prompt**: a clean feed-ready redraw prompt with no workflow metadata, capped at **1900 Chinese characters**.
7. **Workflow JSON (collapsed by default)**: structured metadata for humans/agents; mark it clearly as not for direct image-platform input.
8. **Failure risks and quality checks**.

## Hard Rules

- Put characters first. Short-drama posters must make faces, posture, and relationship readable at thumbnail size.
- Avoid empty scenic posters unless the story is landscape-driven. In most cases, people should occupy 60%-85% of the poster height depending on cast size.
- For multi-character posters, do not distribute attention evenly. The main role must stay largest, clearest, and visually brightest.
- If multiple characters are selling points, write their relative visual weight directly: shared shot size, face clarity, foreground/midground position, brightness, and focus. Do not imply an important selling character only through vague "behind" or "second focus" wording if their face and appeal must read clearly.
- Do not generate visible text inside the image unless the user explicitly requests title rendering.
- Preserve a title-safe area even when no title will be added by the image model.
- If title rendering is requested, title readability must never destroy face readability or relationship clarity.
- If title rendering is requested, do not leave the title family unspecified. Always choose a base glyph family first, then assign a surface treatment that matches the poster style.
- Avoid cheap cover aesthetics: collage clutter, random neon gradients, over-smoothed AI skin, tiny faces, bad hands, unreadable relationships, platform UI marks, fake logos, and watermark-like artifacts.
- If character turnarounds are provided, prioritize turnaround consistency over style creativity.
- If character turnarounds are provided, treat this skill as **turnaround-driven generation first**, not free character invention.
- With character turnarounds, do not invent or over-specify facial features, body proportions, species traits, materials, colors, silhouette markers, or hairstyle changes unless the user explicitly asks for those changes.
- With character turnarounds, keep appearance language minimal and identity-safe: describe only role hierarchy, expression, gaze, posture, wardrobe, shot size, and lighting that help the poster read better without changing the approved design.
- If the story contains identity links such as true form, avatar, incarnation, companion form, summoned form, mirror form, or spirit counterpart, do not translate that relationship into appearance mutation unless the user explicitly asks. Preserve each referenced design as shown and express the link through staging, gaze, proximity, light, shadow, or composition.
- If a style/composition reference is provided, use it only for composition, camera distance, cropping rhythm, negative space, color tendency, lighting logic, and poster finish.
- Never copy visible text, title wording, font content, character identity details, face description, clothing specifics, props, jewelry, logos, watermarks, or plot-specific visual clues from a style/composition reference unless the user explicitly asks to inherit that exact element.
- If an action/relationship reference is provided, inherit only pose, motion path, force direction, contact/impact relationship, camera angle, and foreground/background hierarchy; do not inherit character identity, species/type, temperament, era feel, profession feel, style finish, colors, materials, text, props, or story content from that reference.
- For high-motion action, specify camera angle, center of gravity, limb/edge positions, motion direction, expression state, and whether motion blur is allowed or limited.
- In multi-turn revision, the latest explicit user correction overrides older prompt rules. The next platform-ready prompt must remove old names, old states, old poses, and old material assumptions that conflict with the latest correction.
- For non-human, creature, mechanical, object, or heavily designed characters, preserve the approved design's recognizable silhouette, structural proportions, material language, color blocking, and category-defining markers; do not drift into adjacent archetypes unless the user explicitly asks.
- For non-human, creature, mechanical, object, or heavily designed characters, lock high-drift local identifiers when visible: face markings, color-block boundaries, eye area, nose/mouth or front structure, ear/horn/tail/limb tips, special marks, and other approved local features.
- For material-state transformations such as solid, hologram, energy form, spirit form, shadow form, silhouette, projection, or translucent body, state both what is preserved and what changes: color retention or removal, opacity, edge behavior, internal structure, dissipation, and whether the body is physically solid.
- Setting elements such as UI panels, projections, magic circles, props, background threats, and symbolic objects must not steal the user-specified first visual focus unless the user explicitly makes them the main subject.
- Platform-ready prompts must be pure image instructions, not dialogue, explanation, or assistant commentary.
- Show the `Platform-ready prompt` first. Treat `Workflow JSON` as secondary supporting information for revision control, not the main user-facing result.
- Assume many users are beginners. By default, keep `Workflow JSON` folded/collapsed or clearly separated as optional advanced information.
- In platform-ready prompts, forbid phrases like `你给的`, `你提供的`, `参考你提供的`, `如果你要`, `我可以`, `下面给你`, `应该改成`, `这一版`, `再给你一版`, `视觉上让人一眼明白`, `这是XX设定`, `改为`, `改成`, `保持为`, `参考示例图`, `按示例图`.
- In platform-ready prompts, never include image filenames, attachment names, local paths, numbered file references, or raw reference labels. Convert them into visible scene descriptions or keep them only in workflow/reference-binding notes.
- In platform-ready prompts, replace supervisory or explanatory wording with direct visible constraints.
- In revision mode, write the final image as an already-decided result state. Do not write edit instructions such as `把A改为B`, `保持为`, `改成`, or `参考示例图中的关系`.
- Translate user wording into visual language before writing the platform-ready prompt. Do not paste casual user phrasing, relationship labels, or abstract intent directly when it can be rendered as pose, gaze, distance, contact, blocking, lighting, or hierarchy.
- For multi-character or layered compositions, specify shared light source, shared color temperature, atmospheric perspective, contact/occlusion, scale relationship, and edge integration so characters do not look pasted together.
- If the task is outpainting, aspect-ratio conversion, or canvas expansion, preserve the subject, pose, expression, design, lighting, and composition center; extend only the edge environment unless the user explicitly asks to redraw the subject.
- Platform-ready prompts must stay within **1900 Chinese characters** unless the user explicitly asks for a longer version.
- If the prompt is too long, compress in this order: remove repeated style adjectives, merge similar negative constraints, shorten explanatory transitions, keep visual weight, shot size, face clarity, reference locks, composition, lighting, and title-safe-area first.
- If the requested style is anime, cartoon, or 3D anime, replace realism-specific language with line, shape, material, rendering, and silhouette language instead of forcing photo-real skin rules.
