# Example: Case Summary Template

Use this example when the user asks to summarize a completed skill-use session for later iteration of `short-drama-poster`.

The goal is not to make a new poster prompt. The goal is to extract:

- what the user was trying to do
- what the skill originally produced
- what the user corrected because the skill went wrong
- what was fixed and later regressed
- what specific failures were exposed
- what rules or examples should be updated next

Do not summarize every sentence in a long conversation. Keep only skill-relevant errors, corrections, regressions, final effective constraints, and generated-result feedback.

## Trigger Phrases

- `轻量复盘`
- `只复盘最近这一轮`
- `阶段复盘`
- `复盘`
- `总结这次使用`
- `整理这次对话`
- `输出 case summary`
- `输出复盘文件`
- `最终复盘`
- `合并复盘`

## Required Output Form

Return a single markdown code block and nothing else outside it.

Choose the smallest useful recap scope:

- Use `轻量复盘` for the latest turn or latest correction only.
- Use `阶段复盘` for one working phase.
- Use full `Case Summary` only when the user asks for final recap, output file, or merged summary.
- In long conversations, prefer merging existing light/stage recaps instead of rereading and restating the entire conversation.

## Light Recap Example

```md
## 轻量复盘
- 跑偏：平台投喂词又出现 `改为`、`保持为` 这类修改过程词。
- 用户纠正：平台词必须写最终画面结果，不能写改稿说明。
- 后续状态：已修好。
- 可提炼问题：改词模式需要稳定的结果态输出规则。
```

## Stage Recap Example

```md
## 阶段复盘
- 本阶段目标：修正平台投喂词中的语言污染。
- 关键跑偏：输出混入对话指代、修改过程词和流程指代。
- 用户纠正：删除 `你给的`、`改为`、`保持为`、`参考示例图`，改成最终画面结果。
- 后续状态：已修好，但长对话中存在回退风险。
- 最终有效约束：平台投喂词只保留画面指令、构图、光影、材质和负向约束。
- 可提炼问题：长对话复盘应记录回退点，不逐句记录全部过程。
```

## Full Case Summary Example

```md
# Case Summary

## 1. 本次任务
- 用户目标：生成一张可直接生图的中文短剧海报底图
- 任务类型：改词
- 是否有角色三视图：有
- 是否有风格/构图参考图：有
- 是否有旧海报或旧 prompt：有旧 prompt

## 2. 原始输入关键信息
- 剧情/题材：男频重生复仇、异兽进化、系统爽文
- 角色设定：普通刀疤鲤鱼本体、终极进化虚影、黑龙威胁
- 风格要求：高级类3D动漫商业海报
- 构图要求：前实后虚双层主角关系，标题安全区清晰
- 其他硬约束：角色三视图一致，不抄风格图里的文字和人物

## 3. Skill 原始输出摘要
- 平台投喂词的核心内容：保留主角本体、终极进化虚影、系统前置面板和猛鱼缸环境
- Workflow JSON 的核心内容：任务判断为普通无标题海报底图，参考绑定清晰，视觉主次分为主角本体、终极虚影、系统层、背景威胁
- 负向约束的核心内容：不出现额外文字、不要把主角画成红金锦鲤、不要把终极投影画成前景实体
- 如果有多个方向，分别概括：本轮为改词，没有重新出三套方向

## 4. 用户关键纠正与回退点
- 跑偏：平台投喂词写成修改过程，出现 `改为`、`保持为`、`参考示例图`
  用户纠正：平台词必须写最终画面结果，不写改稿说明
  后续状态：已修好
  可提炼问题：改词模式需要结果态输出规则

- 跑偏：终极形态被写成去固有色的蓝白全息投影
  用户纠正：虚影需要保留角色原有配色，但材质是半透明能量态
  后续状态：后续又回退过
  可提炼问题：多轮修改中，最新用户纠正必须覆盖旧设定

## 5. 暴露出的具体问题
- 平台投喂词混入了 `改为`、`保持为` 这类修订态表述
- 平台投喂词混入了 `参考示例图` 这类流程指代
- 改词场景下，输出仍然在描述修改动作，而不是直接描述最终画面结果
- 长对话中已修正的信息可能被后续输出改回旧版本

## 6. 结果判断
- 哪些部分可用：角色层级、环境设定、负向约束大体可用
- 哪些部分不可用：平台投喂词中的修订态表述不可直接投喂
- 最终是否能直接生图：不能直接用原样版本
- 如果不能，卡点是什么：语言没有完全收成结果态的纯画面指令

## 7. 可供规则迭代的结论
- 应新增的硬规则：改词模式下禁止出现 `改为/改成/保持为/参考示例图`
- 应新增的条件分支规则：当用户要求“保留原有配色但改为非实体/能量态/全息态”时，同时约束颜色保留与材质非实体化
- 应补充的负面示例：补一组修订态句子改写为结果态句子的 few-shot
- 应修改的默认输出方式：改词模式优先输出最终平台词，不强化流程说明
- 应删除或弱化的旧规则：弱化容易诱发“修改态语言”的整图重绘模板措辞
- 仅作为案例备注，不应写入通用规则：本案例里的具体物种名、角色名、剧情名只保留在案例记录中，不直接写成全局规则
```
