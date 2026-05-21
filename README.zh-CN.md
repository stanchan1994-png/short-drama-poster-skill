# Short Drama Poster Skill

[English README](./README.md)

面向 AI agent 的中文短剧海报工作流 skill。

这个 skill 主要解决：

- 短剧海报方向策划
- 中文完整提示词生成
- JSON 结构化提示词生成
- 基于现有海报的整图重绘指令
- 写实、半写实插画、动漫卡通、类 3D 动漫等风格分支
- 支持带标题成图与中文字体排版规则
- 单人、双人、三人、多角色群像的构图与主次控制

## 它解决什么问题

普通图片提示词工具在短剧海报上经常不够用，主要缺少这些能力：

- 不会抓短剧商业钩子
- 人物关系在缩略图尺寸下不够清楚
- 不会预留标题安全区
- 多人海报容易做成“合照”或“毕业照”
- 缺少短剧平台常见失败项的负向约束
- 用户要卡通或类 3D 动漫时，仍然被默认写实规则带偏

这个 skill 的目标，是把剧本、梗概、角色参考图或现有海报，转成真正可执行的短剧海报工作流。

## 核心能力

- 先产出 3 个明显不同的海报方向，再写最终 prompt
- 支持 `写实电影感 / 半写实插画 / 动漫卡通 / 类3D动漫`
- 支持“无字底图”和“直接带标题成图”两种输出方式
- 支持 `1人 / 2人 / 3人 / 4-6人 / 大群像` 的不同构图逻辑
- 输出中文完整提示词和 JSON 结构化提示词
- 支持“保留人物关系，整图重做”的改图型需求
- 内置短剧海报质检规则，方便最后做验收

## 仓库结构

- [SKILL.md](/Users/edy/Documents/GitHub/short-drama-poster/SKILL.md)：主 skill 入口
- [agents/openai.yaml](/Users/edy/Documents/GitHub/short-drama-poster/agents/openai.yaml)：agent 元数据
- [references/poster-workflow.md](/Users/edy/Documents/GitHub/short-drama-poster/references/poster-workflow.md)：完整工作流
- [references/prompt-spec.md](/Users/edy/Documents/GitHub/short-drama-poster/references/prompt-spec.md)：输出格式规范
- [references/quality-checklist.md](/Users/edy/Documents/GitHub/short-drama-poster/references/quality-checklist.md)：验收与质检规则
- [references/style-modes.md](/Users/edy/Documents/GitHub/short-drama-poster/references/style-modes.md)：风格模式与多人规则
- [references/title-design.md](/Users/edy/Documents/GitHub/short-drama-poster/references/title-design.md)：带标题成图与字体规则
- [references/font-library.md](/Users/edy/Documents/GitHub/short-drama-poster/references/font-library.md)：中文标题字体家族、字形分类与材质方向
- [references/title-fewshots.md](/Users/edy/Documents/GitHub/short-drama-poster/references/title-fewshots.md)：带字海报稳定输出样板
- [examples/realistic-urban-revenge.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/realistic-urban-revenge.md)：写实示例
- [examples/semi-realistic-fantasy-romance.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/semi-realistic-fantasy-romance.md)：半写实插画示例
- [examples/anime-family-secret.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/anime-family-secret.md)：动漫卡通示例
- [examples/3d-anime-ensemble.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/3d-anime-ensemble.md)：类 3D 动漫示例
- [examples/title-rendered-urban-power.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/title-rendered-urban-power.md)：带标题成图示例
- [examples/prompt-cleanliness-bad-vs-good.md](/Users/edy/Documents/GitHub/short-drama-poster/examples/prompt-cleanliness-bad-vs-good.md)：坏词与干净投喂词对照示例

## 安装方式

如果你在本地使用 Codex skills，可以直接复制到 skills 目录：

```bash
cp -R short-drama-poster ~/.codex/skills/short-drama-poster
```

如果你当前就在仓库目录外，也可以直接用绝对路径：

```bash
cp -R /absolute/path/to/short-drama-poster ~/.codex/skills/short-drama-poster
```

## 适用场景

适合这些请求：

- “给我做 3 个短剧海报方向”
- “把这个剧情梗概转成海报 prompt”
- “这个短剧要做双人/三人/群像海报”
- “我要卡通版 / 动漫版 / 类 3D 动漫版”
- “我要直接带字的短剧封面”
- “根据这张海报整图重绘，保留人物关系”
- “给我一个中文完整 prompt 和 JSON”

典型调用方式：

```text
Use short-drama-poster to turn this script into 3 poster directions, then give me one Chinese complete prompt and one JSON structured prompt.
```

如果想直接指定风格：

```text
Use short-drama-poster. Make it a 3D anime commercial poster with a strong two-person confrontation and a clean upper title-safe area.
```

## 默认输出结构

标准输出应包含：

1. 3 个海报方向
2. 推荐方向及理由
3. 中文完整提示词
4. 平台投喂版 Prompt
5. 工作流 JSON（默认折叠，不要直接用于生图平台）
6. 负向约束
7. 质检清单

如果用户明确要“带标题成图”，输出里还应包含标题层说明或直接带字版本扩展。

如果用户说 `复盘`、`总结这次使用`、`整理这次对话` 或 `输出复盘文件`，skill 应切换为 `Case Summary` 模式，输出一份统一结构的复盘记录，而不是继续出图。

## 支持的风格模式

- 写实商业海报
- 半写实插画
- 动漫卡通海报
- 类 3D 动漫海报

风格分支很重要，因为用户明确说“不要写实”时，skill 不应该继续套用真实皮肤、电影布光、真人五官逻辑。

## 说明

- 默认输出语言为中文
- 默认目标图像是“无标题文字的海报底图”
- 用户明确要求时，也支持直接输出带标题成图规则，且默认只放剧名，副标题等附加文字需要主动要求
- 如果有角色三视图，设定一致性优先于风格创意
- 多人海报里不应该让每张脸都拥有同等视觉权重
- 面向小白用户时，优先展示“平台投喂版 Prompt”；工作流 JSON 应作为默认折叠的附加信息
- 平台投喂版 Prompt 必须是纯画面指令，不能混入“你给的”“如果你要”“我可以再给你一版”这类对话污染
- 复盘模式下必须只输出统一格式的 Case Summary，不继续生成新海报方案
