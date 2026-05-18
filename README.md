# Short Drama Poster Skill

[中文说明](./README.zh-CN.md)

Chinese short-drama poster workflow for AI agents.

This skill is designed for:

- short-drama poster direction planning
- Chinese complete prompt generation
- JSON structured prompt generation
- whole-image redraw instructions
- realistic, semi-realistic illustration, anime/cartoon, and stylized 3D anime poster styles
- single-character, dual-character, triangle, and multi-character cast staging

## What It Solves

Most generic image-prompt skills are weak at Chinese short-drama posters because they miss:

- scroll-stopping commercial hooks
- relationship readability at thumbnail size
- title-safe-area planning
- cast hierarchy in multi-character posters
- short-drama-specific negative constraints
- style branching between realism, cartoon, and 3D anime looks

This skill turns a script, synopsis, character references, or an existing poster into a practical poster workflow that fits Chinese AI image-generation use.

## Core Capabilities

- Generate 3 distinct poster directions before final prompt writing
- Choose between realistic, semi-realistic, anime/cartoon, and 3D anime modes
- Support 1-person, 2-person, 3-person, 4-6 person, and large-cast poster logic
- Produce Chinese complete prompts and JSON structured prompts
- Handle whole-image redraw requests while preserving identity and composition constraints
- Run a final quality pass using commercial poster checks

## Repository Structure

- [SKILL.md](/Users/edy/Documents/GitHub/short-drama-poster/SKILL.md): main skill instructions
- [agents/openai.yaml](/Users/edy/Documents/GitHub/short-drama-poster/agents/openai.yaml): agent metadata
- [references/poster-workflow.md](/Users/edy/Documents/GitHub/short-drama-poster/references/poster-workflow.md): step-by-step workflow
- [references/prompt-spec.md](/Users/edy/Documents/GitHub/short-drama-poster/references/prompt-spec.md): output format spec
- [references/quality-checklist.md](/Users/edy/Documents/GitHub/short-drama-poster/references/quality-checklist.md): review rules
- [references/style-modes.md](/Users/edy/Documents/GitHub/short-drama-poster/references/style-modes.md): style branching rules
- [examples/realistic-urban-revenge.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/realistic-urban-revenge.md): realistic example
- [examples/semi-realistic-fantasy-romance.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/semi-realistic-fantasy-romance.md): semi-realistic example
- [examples/anime-family-secret.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/anime-family-secret.md): anime/cartoon example
- [examples/3d-anime-ensemble.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/3d-anime-ensemble.md): stylized 3D anime example

## Installation

If you use Codex local skills, copy this repository into your skills directory:

```bash
cp -R short-drama-poster ~/.codex/skills/short-drama-poster
```

If you are already inside this repository:

```bash
cp -R /absolute/path/to/short-drama-poster ~/.codex/skills/short-drama-poster
```

## Recommended Invocation

Use the skill when asking for:

- short-drama poster directions
- poster prompt optimization
- multi-character poster staging
- Chinese poster JSON prompt structures
- anime or 3D anime short-drama poster treatment
- whole-image redraw instructions for an existing poster

Typical request:

```text
Use short-drama-poster to turn this script into 3 poster directions, then give me one Chinese complete prompt and one JSON structured prompt.
```

For stylized output:

```text
Use short-drama-poster. Make it a 3D anime commercial poster with a strong two-person confrontation and a clean upper title-safe area.
```

## Output Shape

Standard output should include:

1. 3 poster directions
2. recommended direction
3. Chinese complete prompt
4. JSON structured prompt
5. negative constraints
6. quality checklist

## Style Modes

Supported modes:

- realistic commercial poster
- semi-realistic illustration
- anime/cartoon poster
- stylized 3D anime poster

The style branch matters because the skill should not force realistic skin or film-lighting language when the user explicitly wants anime or stylized 3D output.

## Notes

- Default language is Chinese
- Default image assumption is title-free poster base
- Actor identity consistency takes priority over visual experimentation when reference photos exist
- In multi-character posters, not every face should receive equal attention
