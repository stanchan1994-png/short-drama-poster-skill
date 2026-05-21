# Example: Case Summary Template

Use this example when the user asks to summarize a completed skill-use session for later iteration of `short-drama-poster`.

The goal is not to make a new poster prompt. The goal is to extract:

- what the user was trying to do
- what the skill originally produced
- what the user changed by hand
- what specific failures were exposed
- what rules or examples should be updated next

## Trigger Phrases

- `复盘`
- `总结这次使用`
- `整理这次对话`
- `输出 case summary`
- `输出复盘文件`

## Required Output Form

Return a single markdown code block and nothing else outside it.

## Example Output

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

## 4. 用户后续修改
- `终极进化形态改为主角身后偏上方的大型虚影` -> `终极进化形态位于主角身后偏上方，形成大型虚影层`
- `背景威胁保持为后景上半部的巨大正面巨骨舌鱼黑影` -> `背景威胁为后景上半部的巨大正面巨骨舌鱼黑影`
- `动作关系参考示例图` -> `本体前冲，后方虚影顺势上扬，形成前低后高的冲势关系`

## 5. 暴露出的具体问题
- 平台投喂词混入了 `改为`、`保持为` 这类修订态表述
- 平台投喂词混入了 `参考示例图` 这类流程指代
- 改词场景下，输出仍然在描述修改动作，而不是直接描述最终画面结果

## 6. 结果判断
- 哪些部分可用：角色层级、环境设定、负向约束大体可用
- 哪些部分不可用：平台投喂词中的修订态表述不可直接投喂
- 最终是否能直接生图：不能直接用原样版本
- 如果不能，卡点是什么：语言没有完全收成结果态的纯画面指令

## 7. 可供规则迭代的结论
- 应新增的硬规则：改词模式下禁止出现 `改为/改成/保持为/参考示例图`
- 应补充的负面示例：补一组修订态句子改写为结果态句子的 few-shot
- 应修改的默认输出方式：改词模式优先输出最终平台词，不强化流程说明
- 应删除或弱化的旧规则：弱化容易诱发“修改态语言”的整图重绘模板措辞
```
