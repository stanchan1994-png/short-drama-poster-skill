# Title Design

Use this file when the user explicitly wants a poster with rendered title text, subtitle, or tagline.

For reverse-engineering title references and font-family classification, also read `references/font-library.md`.
For stable rendered-title output patterns, also read `references/title-fewshots.md`.

## 1. Default Recommendation

Default to a title-free poster base.

Only render title text when:

- the user explicitly asks for 带字海报 / 带标题成图 / 直接出封面
- the target platform requires a complete ready-to-publish poster
- the title treatment itself is part of the style request

Default title policy:

- render only the main drama title
- do not add subtitle, hook line, slogan, episode tag, platform label, or corner copy unless the user explicitly asks for them

## 2. Title Layer Strategy

When title rendering is requested, split the thinking into two layers:

- poster base: characters, scene, lighting, conflict
- title layer: title, and only optional subtitle/tagline/corner labels/billing when explicitly requested

If the tool or platform supports compositing, recommend generating the title-free base first and adding title later.
If the user still wants direct rendered text in one image, keep title instructions short and strict.

## 3. Placement Rules

Choose title placement based on composition:

- upper center: best for dual-character confrontation and centered protagonists
- upper left / upper right: best when one side has clean dark or light negative space
- lower center: usable when upper half is crowded and lower area is clean
- side vertical layout: only for specific suspense, costume, or art-poster treatment

Never place title text:

- across eyes
- across mouths
- across key hand props
- inside bright noisy textures
- over detailed hair or jewelry clusters

## 4. Hierarchy Rules

For Chinese short-drama posters, title hierarchy should usually be:

- main title only by default
- optional short hook or subtitle only when explicitly requested
- optional small platform or episode line only when explicitly required

The main title must dominate.
Do not let subtitle size compete with the main title.
Avoid too many lines.
If there is no strong reason, use only one title line.

Recommended:

- main title: 2-6 Chinese characters preferred, 7-10 acceptable if layout allows
- subtitle / hook: off by default; if used, only 1 short line
- billing / platform line: off by default; if used, very small and low priority

## 5. Font Style Direction

Before selecting any specific font bucket, do this in order:

1. choose the base glyph family from `references/font-library.md`
2. confirm that the family matches genre, emotional temperature, and relationship type
3. only then choose the specific bucket and surface material

The same story should not randomly jump between unrelated glyph families.
Material can change more freely than structure.

## 5a. Automatic Family Matching

When the user asks for a rendered-title poster and does not provide a font reference, auto-match as follows:

- 龙王 / 战神 / 兵王 / 保镖 / 都市硬复仇:
  - default family: `硬核战损金属切角字`
- 权势碾压 / 回归称王 / 身份反转压迫 / 帝王感男主:
  - default family: `权谋金石书法字`
- 宫斗 / 古言 / 王妃 / 贵女上位 / 皇室权谋:
  - default family: `宫廷暖金竖排字`
- 疯批 / 虐恋 / 黑化 / 追妻火葬场 / 高情绪反转:
  - default family: `疯批刀锋手写字`
- 高奢悬疑 / 宿命感 / 冷欲 / 都市高级女频:
  - default family: `高奢细锋展示字`
- 甜喜 / 沙雕 / 反套路总裁 / 后妈文学 / 轻松都会:
  - default family: `复古甜喜圆润字`

If the sample and story conflict, prioritize the story unless the user explicitly says to follow the reference style exactly.

## 5b. Material Matching

After the base family is chosen, match the material to the poster finish:

- realistic cold action:
  - silver metal, scratches, restrained bevel, stone-steel wear
- premium costume:
  - warm gold foil, sandy metallic grain, shallow emboss
- dark emotional posters:
  - mostly plain bright strokes, dry-brush edge, little or no metal
- luxury cool-tone stories:
  - thin silver edge, cold glow, refined elegant separation
- light comedy:
  - cream gloss, enamel, soft retro sign-paint feeling
- stylized 3D anime:
  - premium key-visual highlight, controlled dimensional sheen, no toy-plastic look

### Realistic Commercial

Recommended font buckets:

- 现代硬朗黑体
- 高对比都市黑体
- 冷峻压迫感窄黑体
- 极简高级无衬线展示字

- modern bold Chinese sans
- sharp contrast, clean edges
- subtle bevel, glow, emboss, or metallic finish only when it fits the genre

Good for:

- revenge
- CEO/power
- urban suspense

Avoid:

- cute rounded fonts
- excessive chrome effects

### Semi-Realistic Illustration

Recommended font buckets:

- 浪漫衬线展示字
- 轻复古宋韵标题字
- 幻想感书卷衬线字
- 柔性高定风标题字

- elegant serif or stylized songti-like display font
- soft glow, ink edge, brushed metal, or painterly texture

Good for:

- romance
- fantasy
- costume

Avoid:

- overly modern tech fonts unless the story is futuristic

### Anime / Cartoon

Recommended font buckets:

- 漫画冲击标题字
- 青春恋爱番标题字
- 轻喜剧圆角展示字
- 悬疑番硬边标题字

- strong hand-drawn or comic-display Chinese title style
- clean silhouette, high readability, fewer texture layers
- energetic contour or sticker-like edge can work

Good for:

- youth
- comedy
- light suspense

Avoid:

- fake childish fonts
- too many sticker effects that cheapen the poster

### Stylized 3D Anime

Recommended font buckets:

- 高级 key visual 展示字
- 轻立体高光标题字
- 偶像企划感时尚展示字
- 幻想冒险 3D 动漫标题字

- premium game-key-art style Chinese display font
- dimensional but controlled
- layered glow or bevel allowed, but title must still feel premium

Good for:

- fantasy romance
- idol entertainment
- premium commercial stylized posters

Avoid:

- low-end mobile-game UI feel
- too much neon bloom
- thick toy-like extrusion

## 6. Prompt Language for Title Rendering

Useful language:

- 保留上方干净标题区并渲染中文剧名
- 剧名字体清晰醒目，商业海报感强
- 标题不要遮挡人物五官
- 标题边缘干净，不要乱码和错字
- 默认只渲染剧名，不额外添加副标题或卖点文案
- 如果明确需要副标题，副标题小一号，放在主标题下方
- 字体风格与题材一致
- 不要平台UI，不要二维码，不要水印

If generating the title directly in-image, always include:

- glyph family
- why the family was selected
- material treatment
- title placement
- title size relationship
- title style
- title avoidance rules
- no garbled characters

## 7. Failure Patterns

Common failures:

- base glyph family does not match genre
- title material fights the poster finish
- title covers the face
- Chinese characters rendered as乱码 or wrong strokes
- unnecessary subtitle added by default
- subtitle too large
- too many decorative effects
- title and background merge together with no separation
- font style conflicts with genre

## 8. Acceptance Checks

- title is readable at thumbnail size
- title does not block the lead face
- glyph family matches the story hook and role energy
- material treatment matches the poster finish
- font style matches the story
- default output contains only the main title unless extra text was explicitly requested
- main title dominates subtitle when subtitle exists
- no garbled Chinese characters
- title edge is clean and commercially usable
