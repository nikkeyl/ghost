<!-- Preserve the supplied blueprint heading structure. -->
<!-- lint disable no-multiple-toplevel-headings -->

# AI Engineering Skills / Neural Blueprint

## 1. Базовый принцип

Основу архитектуры, ключевые решения и направление развития проекта определяет
инженер.

AI-агент используется прежде всего для:

- рутинных задач;
- реализации в рамках уже заданного направления;
- повторяемых изменений;
- анализа;
- проверки;
- ускорения работы с существующей кодовой базой.

AI не должен становиться заменой инженерного мышления.

Полагаться на AI во всём под предположением, что это автоматически сильно повышает
продуктивность — ошибка. AI действительно ускоряет часть работы, но выигрыш
ограничен, если инженер перестаёт понимать систему и проверять результат.

---

# 2. Проблема дешёвых идей

Генеративный AI резко снизил стоимость создания:

- идей;
- кода;
- вариантов решений;
- архитектурных предложений;
- текстовых объяснений.

Количество идей растёт быстрее, чем их среднее качество.

Поэтому главным дефицитом становится не генерация, а:

- фильтрация;
- проверка;
- инженерное суждение;
- понимание последствий;
- способность отказаться от плохого решения.

Возникает проблема «мясных прокси»: человек передаёт запрос AI и его ответ дальше
практически без интеллектуальной проверки.

Такой workflow масштабирует не только производительность, но и ошибки.

---

# 3. Организация изменений

Изменения, сделанные AI, желательно группировать по смысловым категориям.

Например:

```text
form-validation
authentication
error-handling
performance
accessibility
state-management
api
refactoring
testing
```

Это упрощает:

- review;
- понимание blast radius;
- откат;
- тестирование;
- анализ истории изменений.

---

# 4. Commits

Коммиты создавать по Conventional Commits.

```text
feat(validation): add client-side email validation

- add schema validation
- display field-level errors
- prevent invalid submission
- add regression tests
```

Коммит должен описывать не только факт изменения, но и содержательный scope
выполненной работы.

---

# 5. Pull Requests

Избегать огромных PR.

Большой PR:

- повышает cognitive load reviewer'а;
- сложнее качественно проверить;
- скрывает ошибки среди большого diff;
- затрудняет оценку архитектурных последствий;
- ухудшает качество обратной связи;
- повышает вероятность формального review.

Предпочтительны небольшие coherent changes с одной понятной целью и ограниченным
blast radius.

---

# 6. Rules, Passive Skills и Active Skills

Не всё должно быть skill.

Нужно разделять:

```text
Rules
Passive Skills
Active Skills
```

Они работают на разных уровнях.

---

# 7. Rules

`Rule` — постоянное ограничение или инженерный принцип.

Rule не нужно специально «вызывать».

Он должен влиять на поведение агента практически во всех релевантных задачах.

Примеры:

```text
Prefer the smallest coherent change.

Do not modify unrelated code.

Do not create unnecessary abstractions.

Preserve existing public contracts unless explicitly asked otherwise.

Do not claim verification unless verification was actually performed.

Measure before optimizing.

Do not hide uncertainty.

Follow repository conventions.

Avoid large unrelated diffs.
```

Для Git:

```text
Use Conventional Commits.

Keep commits semantically coherent.

Do not mix refactoring and behavior changes unnecessarily.
```

Для PR:

```text
Prefer small reviewable changes.

Avoid combining unrelated concerns into one PR.
```

Это не skills.

Агент не должен думать:

```text
Should I invoke prefer-small-pr?
```

Это просто часть его operating policy.

Концептуально:

```text
Rules
  ↓
constrain every relevant decision
```

---

# 8. Passive Skills

Passive skill — способность, которая работает в фоне и активируется как часть другой
работы, но обычно не становится основной задачей.

Примеры:

```text
detect-unnecessary-complexity
detect-breaking-change
detect-security-risk
detect-accessibility-regression
detect-large-blast-radius
detect-unrelated-diff
detect-missing-tests
detect-architecture-drift
detect-effect-misuse
detect-unsafe-type-assertion
detect-hidden-assumption
```

Например, агент реализует feature.

Основной workflow:

```text
implement-feature
```

Но в процессе пассивно работают:

```text
detect-breaking-change
detect-unnecessary-complexity
detect-missing-tests
detect-security-risk
```

Они не должны превращать каждую задачу в отдельный audit.

Их задача — поднять сигнал только если обнаружено что-то существенное.

Модель:

```text
Active task
    │
    ├── passive check
    ├── passive check
    ├── passive check
    │
    ▼
continue normally
```

Если passive skill обнаружил значимую проблему:

```text
passive detector
      ↓
significant finding
      ↓
activate dedicated skill
```

Например:

```text
detect-performance-risk
        ↓
possible expensive rerender
        ↓
diagnose-react-rendering-performance
```

Таким образом passive skill — это скорее detector / guard / observer.

---

# 9. Active Skills

Active skill — полноценная инженерная процедура.

Он имеет:

```text
Trigger
→ Goal
→ Investigation
→ Reasoning
→ Decision
→ Action
→ Verification
→ Completion Criteria
```

Например:

```text
debug-systematically
```

Workflow:

```text
reproduce
→ collect evidence
→ separate facts from assumptions
→ formulate hypotheses
→ test hypotheses
→ identify root cause
→ implement fix
→ verify
```

Другие active skills:

```text
understand-codebase
analyze-change-impact
trace-data-flow
plan-code-change
debug-systematically
review-architecture
diagnose-performance-problem
design-public-api
implement-minimal-change
verify-change
```

Active skills стоят дорого относительно passive skills, потому что запускают
полноценный reasoning workflow.

Поэтому их нужно активировать только когда это действительно необходимо.

---

# 10. Разница между тремя уровнями

```text
RULE
"Prefer the smallest coherent change."

PASSIVE SKILL
"Detect whether the current change has unnecessary scope."

ACTIVE SKILL
"Analyze the change and redesign it to minimize blast radius."
```

Ещё пример:

```text
RULE
"Do not optimize without evidence."

PASSIVE SKILL
"Detect suspicious performance-sensitive code."

ACTIVE SKILL
"Profile and diagnose the performance bottleneck."
```

Ещё:

```text
RULE
"Preserve backward compatibility unless explicitly allowed to break it."

PASSIVE SKILL
"Detect a potential breaking API change."

ACTIVE SKILL
"Analyze API compatibility and design a safe migration."
```

Это важное архитектурное разделение.

---

# 11. Skills

Skill — это не просто knowledge и не общий prompt.

Skill описывает повторяемую инженерную процедуру.

Хорошая структура:

```text
Trigger
→ Goal
→ Investigation / Reasoning
→ Decision Rules
→ Actions
→ Verification
→ Completion Criteria
```

Плохой skill:

```text
understand-event-loop
```

если внутри просто лекция про event loop.

Лучше:

```text
diagnose-async-ordering-bug
```

с процедурой:

```text
observe ordering
→ reconstruct task/microtask scheduling
→ create hypothesis
→ reproduce
→ compare expected vs actual
→ identify violated assumption
→ verify fix
```

---

# 12. Файловая структура

Reusable agent capabilities лучше хранить отдельно от конкретного runtime.

```text
project/
│
├── AGENTS.md
│
├── .agents/
│   ├── rules/
│   ├── skills/
│   └── knowledge/
│
└── .codex/
```

Например:

```text
.agents/
  rules/
    engineering.md
    git.md
    reviews.md

  skills/
    active/
      debug-systematically/
        SKILL.md

      analyze-change-impact/
        SKILL.md

      verify-change/
        SKILL.md

    passive/
      detect-breaking-change/
        SKILL.md

      detect-unnecessary-complexity/
        SKILL.md

      detect-security-risk/
        SKILL.md

  knowledge/
    javascript-event-loop.md
    browser-rendering.md
    react-rendering.md
```

Не обязательно буквально использовать именно такую файловую структуру, но
концептуальное разделение полезно.

---

# 13. `.agents` для переиспользования

`.agents` стоит рассматривать как слой reusable agent capabilities.

```text
             .agents/
                │
       ┌────────┼────────┐
       │        │        │
     Codex   Agent B   Agent C
```

Skill не должен быть привязан к Codex, если его логика универсальна.

Например:

```text
debug-systematically
analyze-change-impact
review-api-design
verify-change
```

могут использоваться разными coding agents.

А `.codex` остаётся местом для Codex-specific configuration.

Концептуально:

```text
AGENTS.md
    ↓
project-level behavior

.agents/
    ↓
reusable cognition and capabilities

.codex/
    ↓
Codex-specific runtime configuration
```

---

# 14. Engineering Neural Blueprint

Система не должна загружать все skills одновременно.

Она должна работать как сеть связанных когнитивных возможностей.

```text
                              trace-data-flow
                                    ▲
                                    │
Task
 │
 ▼
understand-problem
 │
 ▼
skill router
 │
 ▼
debug-systematically ───────► analyze-event-loop
 │
 ├──────────────────────────► analyze-next-caching
 │
 ▼
find-root-cause
 │
 ▼
implement-minimal-change
 │
 ▼
verify-change
```

При этом Rules находятся над всей системой:

```text
                    RULES
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   reasoning      skill routing    actions
```

Passive skills работают сбоку:

```text
                   Active workflow
                        │
              ┌─────────┼─────────┐
              │         │         │
            detect    detect    detect
            risk      scope     regression
              │
              └──────► signal
```

---

# 15. Skill graph

Skills могут иметь связи:

```text
requires
may_trigger
followed_by
delegates_to
conflicts_with
references
```

Пример:

```yaml
name: debug-systematically

requires:
  - understand-problem

may-trigger:
  - trace-data-flow
  - trace-control-flow
  - analyze-event-loop
  - analyze-cache-behavior

followed-by:
  - implement-minimal-change
  - verify-change
```

Связь не означает автоматический запуск.

Нельзя:

```text
A related to B
→ always run B
```

Нужно:

```text
A
+
observed condition X
+
relationship with B
→ activate B
```

---

# 16. Progressive Activation

```text
200 total capabilities
        ↓
10–20 relevant candidates
        ↓
2–5 active skills loaded
        ↓
1–4 active workflows executed
```

Параллельно могут работать лёгкие passive checks.

```text
Active skills: expensive
Passive skills: lightweight
Rules: always available
```

Количество skills в репозитории не является главной проблемой.

Главные факторы стоимости:

```text
number of loaded active skills
×
skill size
×
reasoning depth
×
number of transitions
```

---

# 17. Ограничение распространения

Чтобы избежать graph explosion:

```text
max active skills: 5
max traversal depth: 2
```

Также полезно ограничивать passive escalation:

```text
passive finding
    ↓
severity threshold
    ↓
activate active skill only if justified
```

Не каждый warning должен запускать полноценный reasoning workflow.

---

# 18. Слои инженерного слепка

Полная модель:

```text
engineering-mind/
│
├── rules/
├── knowledge/
├── mental-models/
├── heuristics/
├── passive-skills/
└── active-skills/
```

## Rules

Постоянные ограничения поведения.

```text
Don't modify unrelated code.
Prefer small coherent changes.
Verify before claiming success.
```

## Knowledge

Что инженер знает.

```text
HTTP caching semantics
JavaScript event loop
React reconciliation
browser rendering pipeline
```

## Mental Models

Как инженер представляет работу системы.

```text
browser rendering pipeline
React state propagation
network request lifecycle
Next.js caching model
```

## Heuristics

Правила принятия решений, которые не всегда абсолютны.

```text
Prefer local state until sharing is required.

Measure before optimizing.

Prefer explicit ownership.

Avoid abstraction before variation is understood.
```

Разница между rule и heuristic:

```text
Rule:
Do not claim tests passed if they were not run.

Heuristic:
Prefer integration tests over excessive mocking.
```

Rule почти абсолютен.

Heuristic зависит от контекста.

## Passive Skills

Что агент умеет замечать во время другой работы.

```text
detect-breaking-change
detect-architecture-drift
detect-performance-risk
detect-unnecessary-complexity
```

## Active Skills

Что агент умеет целенаправленно делать.

```text
debug-systematically
analyze-change-impact
plan-code-change
review-architecture
verify-change
```

---

# 19. Общая когнитивная архитектура

```text
                         Rules
                           │
                           ▼
Knowledge ───────► Mental Models
                         │
                         ▼
Task ─────────────► Context Model
                         │
                         ▼
                      Router
                         │
                  ┌──────┴──────┐
                  │             │
             Active Skill   Passive Skills
                  │             │
                  │        detect signals
                  │             │
                  └──────┬──────┘
                         ▼
                      Action
                         │
                         ▼
                    Verification
                         │
                         ▼
                    Self-Critique
                         │
                         ▼
                 Updated Context
```

---

# 20. Основная идея

Цель — не создать AI, который генерирует больше кода.

Цель — создать инженерную cognitive architecture, которая определяет:

```text
что считать фактом
что является предположением
что исследовать
когда нужен отдельный skill
что проверять пассивно
что запрещено rules
какие риски учитывать
что менять
что не менять
как оценивать blast radius
когда эскалировать проблему
как проверять результат
когда считать задачу законченной
```

Именно эта система ближе всего к «нейрослепку» инженерной части мышления.

Короткая формула:

```text
Rules       = как нельзя / как всегда следует работать
Heuristics  = как обычно лучше принимать решения
Passive     = что замечать
Active      = что целенаправленно делать
Knowledge   = что знать
Mental Model = как понимать систему
```
