# Example: Prompt Cleanliness Bad vs Good

Use this example to keep `Platform-Ready Prompt` clean when the story, references, and revision requests are already correct, but the final wording becomes polluted by dialogue residue or explanation language.

## What This Example Solves

Common failure:

- the direction is correct
- the role design lock is correct
- the composition is correct
- but the final feed-ready prompt contains assistant wording, user-facing explanation, or revision chatter

This example teaches the difference between:

- workflow talk
- visual instruction

## Bad vs Good Rule

Bad platform-ready prompts often contain:

- `你给的`
- `你提供的`
- `参考你提供的`
- `如果你要`
- `我可以`
- `下面给你`
- `应该改成`
- `视觉上让人一眼明白这是……`
- `这是XX设定`
- `这一版`
- `再给你一版`

Good platform-ready prompts contain only:

- visible subject description
- composition
- lens distance
- staging
- lighting
- material language
- explicit negative constraints

## Scenario

- 类型：男频重生复仇 / 异兽进化 / 系统爽文
- 主角：普通刀疤鲤鱼本体
- 终极投影：鲤族大帝完全体透明全息投影
- 环境：大型猛鱼缸内部视角
- 风格：高级类3D动漫商业海报
- 需求：直接给生图平台的最终投喂词

## Bad Platform-Ready Prompt

```text
中文短剧竖版商业海报成品，剧名题材为男频重生复仇、异兽进化、系统爽文，整体为高级类3D动漫商业海报风格。前景主体是林川重生后的普通刀疤鲤鱼本体，必须严格参考普通刀疤鲤角色卡。主角背后悬浮巨大系统全息界面，系统必须明确可见，视觉上让人一眼明白“这是系统爽文设定”。系统核心区域投射出林川最终升级形态“鲤族大帝完全体”的巨大透明全息影像，严格参考终极体角色卡，但不能直接把你给的图照搬。环境必须结合你给的猛鱼缸设定图来做。整张图不出现任何其他可见文字。如果你要，我可以再给你一版更适合即梦出图的压缩版。
```

### Why It Is Bad

- contains `必须严格参考` supervisory language
- contains `视觉上让人一眼明白这是……` explanation language
- contains `你给的` dialogue residue
- contains `如果你要，我可以再给你一版` assistant chatter
- mixes workflow talk into the final feed-ready prompt

## Good Platform-Ready Prompt

```text
中文短剧竖版商业海报，男频重生复仇与异兽进化题材，高级类3D动漫商业海报风格。前景主体为普通刀疤鲤鱼本体，严格保持角色三视图中的灰黑轮廓、普通鲤鱼体型、伤疤识别点和非红金锦鲤特征。主角位于画面下半区偏前，体积较小但迎面压上来，形成前景弱体逆袭张力。主角背后悬浮巨大的系统全息界面与透明终极形态投影，构成前实后虚双层主角关系。终极投影为“鲤族大帝完全体”透明全息巨像，体积远大于前景主体，位于中后景核心区，轮廓威压、信息感强，但不替代前景本体。背景威胁为猛鱼缸深处一团巨大化黑色生物阴影，不出现清晰黑龙实体鱼。环境为大型猛鱼缸内部视角，不是自然海底，也不是普通水族箱，带玻璃反光、冷蓝水下主调、局部系统冷光与体积雾。镜头采用中近景低机位仰视，突出小体型主角向前压上的逆袭感。保留中下或下方偏中标题区，不遮挡主角眼睛、嘴部、伤疤识别点和主视觉轮廓。不要出现除剧名外的其他可见文字、汉字、英文、数字、logo、水印、字幕、二维码、平台标识；不要把主角画成红金锦鲤，不要过度华丽美型，不要丢失灰黑普通鲤鱼本体特征，不要把终极投影画成前景实体本体。
```

### Why It Is Good

- all sentences describe visible content
- no user-facing or assistant-facing language
- no revision chatter
- no meta explanation about the workflow
- system setting is expressed as visible staging, not commentary

## Rewrite Pattern

Use this conversion rule during revisions:

1. Delete dialogue residue.
2. Delete explanation residue.
3. Delete assistant chatter.
4. Convert abstract explanation into visible staging.

Examples:

- `视觉上让人一眼明白这是系统爽文设定`
  -> `主角背后悬浮巨大的系统全息界面与透明终极形态投影，构成前实后虚双层主角关系`

- `必须严格参考你给的角色卡`
  -> `严格保持角色三视图中的轮廓、比例、材质、配色和识别点`

- `环境必须结合你给的设定图来做`
  -> `环境为大型猛鱼缸内部视角，不是自然海底，也不是普通水族箱`

- `如果你要，我可以再给你一版压缩版`
  -> delete entirely

## Revision Instruction

When the user asks to tweak wording only, keep:

- output block order
- chosen direction
- staging logic
- reference hierarchy

Change only:

- contaminated phrases
- over-explanation
- platform-unsafe wording

Do not:

- regenerate a new concept
- reshuffle output structure
- rewrite the whole direction set unless the user explicitly asks
