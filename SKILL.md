---
name: short-drama-poster
description: End-to-end Chinese short-drama poster workflow for AI agents. Use when creating or reviewing short-drama, web drama, micro drama, romance/revenge/urban/fantasy poster directions, multi-character compositions, realistic/anime/cartoon/3D-anime poster styles, image-generation prompts, JSON prompt structures, character-consistency rules, title-safe-area guidance, whole-image redraw instructions, or poster quality checklists for Chinese users and AI image platforms.
---

# Short Drama Poster

Use this skill to turn a short-drama brief, script, style direction, character photos, or an existing poster into a practical AI poster workflow. Default to Chinese output unless the user asks otherwise.

The default mode is commercial short-drama realism, but this skill also supports:

- multi-character posters with clear hierarchy and role priority
- semi-realistic illustration posters
- anime/cartoon posters
- stylized 3D anime posters with commercial key-art polish

## Core Workflow

1. Identify the strongest hook: relationship, power gap, reversal, revenge, identity reveal, forbidden love, family secret, or fantasy destiny.
2. Extract visual roles: protagonist, opponent/love interest, supporting power figure, child/family member, hidden antagonist.
3. Decide the visual mode first: realistic, semi-realistic illustration, anime/cartoon, or 3D anime.
4. Produce **3 distinct poster directions** before writing final prompts. Make the directions meaningfully different in composition, emotional temperature, commercial hook, and if useful, style execution.
5. After a direction is chosen, produce a **Chinese complete prompt** and a **JSON structured prompt** for image platforms.
6. Keep the image as a poster base: no rendered title text, no logo, no watermark, and a clean title-safe area.
7. If the user provides an existing poster, treat the task as whole-image redraw unless they explicitly ask for local masking. Preserve the requested identity/composition/style constraints and generate new redraw instructions.
8. Finish with a short quality checklist and concrete fixes.

## What To Read

- For the full staged process, read `references/poster-workflow.md`.
- For exact output formats, read `references/prompt-spec.md`.
- For review and acceptance criteria, read `references/quality-checklist.md`.
- For style branching, read `references/style-modes.md`.

## Default Output Shape

For a normal "make a poster prompt" request, output:

1. **3 poster directions**: title, hook, style mode, composition, characters, scene, lighting, title-safe area.
2. **Recommended direction**: one concise reason.
3. **Chinese complete prompt** for the recommended direction.
4. **JSON structured prompt** using Chinese values while preserving JSON syntax.
5. **Negative constraints** and quality checklist.

For an "edit/redraw this poster" request, output:

1. What to preserve.
2. What to change.
3. Complete whole-image redraw prompt.
4. JSON structured redraw prompt.
5. Failure risks and quality checks.

## Hard Rules

- Put characters first. Short-drama posters must make faces, posture, and relationship readable at thumbnail size.
- Avoid empty scenic posters unless the story is landscape-driven. In most cases, people should occupy 60%-85% of the poster height depending on cast size.
- For multi-character posters, do not distribute attention evenly. The main role must stay largest, clearest, and visually brightest.
- Do not generate visible text inside the image unless the user explicitly requests title rendering.
- Preserve a title-safe area even when no title will be added by the image model.
- Avoid cheap cover aesthetics: collage clutter, random neon gradients, over-smoothed AI skin, tiny faces, bad hands, unreadable relationships, platform UI marks, fake logos, and watermark-like artifacts.
- If character photos are provided, prioritize identity consistency over style creativity.
- If the requested style is anime, cartoon, or 3D anime, replace realism-specific language with line, shape, material, rendering, and silhouette language instead of forcing photo-real skin rules.
