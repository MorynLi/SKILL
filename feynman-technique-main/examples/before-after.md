# Before and after

Same question, same model. The only difference is whether the skill is loaded.

---

## Example 1 — "What is a race condition?"

### Without the skill

> A race condition is a situation in concurrent computing where the behaviour of a
> software system depends on the relative timing of events, such as the order in which
> threads are scheduled. It occurs when multiple threads access shared mutable state
> without proper synchronisation, leading to non-deterministic outcomes. Race conditions
> are typically mitigated using synchronisation primitives such as mutexes, semaphores,
> or atomic operations.

Accurate. Also useless to anyone who didn't already know.

Count what it asks you to already have: *concurrent computing, relative timing, thread
scheduling, shared mutable state, synchronisation, non-deterministic, primitives, mutex,
semaphore, atomic operations*. Ten terms, none explained. And it never once says what
actually goes wrong. This is the bird: you now have the name, in three languages.

### With the skill

> **In one sentence:** Two things change the same value at the same time, each working
> from a copy that went stale the instant the other one moved, and one of the changes
> silently disappears.
>
> **The picture to hold:** a shared notebook with a number written in it, and two people
> who each want to add one to it.
>
> **0 · Kitchen table**
>
> The notebook says **5**. You and I both want to add one.
>
> I read it: five. You read it: five — I haven't written yet. I cross out the 5 and write
> **6**. You cross out my 6 and write **6**, because five plus one is six and five is what
> *you* read.
>
> Two people each added one to five. The notebook says six. One of the additions is simply
> gone, and here is the ugly part: nothing looks broken. There's no scribble, no error, no
> torn page. Just a number that's quietly wrong.
>
> Do it a hundred times and the notebook is wrong by some unpredictable amount — depending
> entirely on how the two of you happened to interleave.
>
> **1 · Newcomer**
>
> The notebook is a piece of memory both parts of your program can reach — a counter, a
> balance, a cache entry. The two people are **threads** (two sequences of instructions
> running at once, sharing the same memory).
>
> What looked like one step — "add one" — is really three: *read* the value, *add* one,
> *write* it back. Between your read and your write, the other thread can do all three of
> its own. That gap is the whole bug.
>
> ```python
> counter = counter + 1   # reads, adds, writes — three steps, interruptible between any two
> ```
>
> When the result depends on which thread happens to get there first, and nothing in your
> program decides that, you have a **race condition**. It's a race because they're racing,
> and nobody appointed a referee.
>
> **2 · Practitioner**
>
> The fix is to make those three steps **atomic** — indivisible, so nobody can slip in
> between them. Two ways:
>
> - A **mutex** (mutual exclusion) — the rule that only whoever holds the pen may write in
>   the notebook. Everyone else waits their turn.
> - An **atomic operation** — a single machine instruction that reads-adds-writes in one
>   indivisible go. Faster, but only available for simple operations.
>
> The trade-off is real. A mutex is a queue, and a queue is throughput you gave up on
> purpose. Guard too much and your threads spend their lives waiting; guard too little and
> the bug survives. Two mutexes taken in inconsistent order gives you a **deadlock** — each
> holding the pen the other is waiting for, both waiting forever.
>
> **3 · Maintainer**
>
> What makes these vicious is that **they usually pass their tests**. The bad interleaving
> needs two threads in a specific window a few nanoseconds wide. On your laptop, with two
> threads and light load, you may never see it. In production, with 64 cores and real
> traffic, you see it hourly.
>
> Symptoms, roughly in order of how you'll meet them: counters drifting slightly low;
> "impossible" states in the database; a bug that vanishes whenever you add logging (the
> log call changed the timing — this is a **Heisenbug**, and it is a strong tell); failures
> that only ever happen under load.
>
> [...continues through level 4]
>
> **Where the picture breaks**
>
> The notebook holds up well, with two lies in it. First, real threads may not even see
> each other's writes when they happen — the CPU keeps values in per-core caches, so it can
> be less like *"you overwrote my number"* and more like *"you were reading a different
> notebook entirely, and neither of us knew."* Second, in the notebook picture the two
> writes are clearly ordered — one happened before the other. On real hardware, with
> instruction reordering, "before" stops being a simple question.

---

## Example 2 — "Why is my Postgres query slow?"

### Without the skill

> Query performance issues in PostgreSQL typically stem from missing indexes, suboptimal
> query plans, or inefficient joins. Run `EXPLAIN ANALYZE` on your query to inspect the
> execution plan. Look for sequential scans on large tables, high row estimates versus
> actuals, and nested loop joins over large row counts. Consider adding appropriate indexes,
> running `VACUUM ANALYZE` to update statistics, and reviewing your `work_mem` setting.

A checklist. It tells you which levers exist and nothing about why any of them moves.
If you already knew what a nested loop join costs, you didn't need this; if you didn't,
you still don't.

### With the skill

> **In one sentence:** Almost always, the database is reading far more rows than your query
> actually needs — either because it has no shortcut to the ones you want, or because it
> has one and decided, on out-of-date information, not to use it.
>
> **The picture to hold:** a filing cabinet of a million receipts in the order they arrived,
> and a card box beside it holding the same receipts' shop names in alphabetical order.
>
> **0 · Kitchen table**
>
> You want every receipt from one shop. Without the card box, you have exactly one option:
> pull out receipt number one, look at it, put it back. Then number two. A million times —
> and you can't stop early, because the last receipt might be a match.
>
> With the card box, you flip to the right letter and go straight to three drawers.
>
> So "why is it slow" almost always means one of two things: **there is no card box**, or
> **there is one and it isn't being used.** The second is more common than people expect,
> and it's the interesting case.
>
> [...continues]

---

## What changed

Neither "after" is longer for the sake of it, and neither is less accurate. Three
differences do the work:

1. **The mechanism arrives before the name.** You watch the number get lost *before* you
   are told it's called a race condition. The name becomes a label for something you
   already understand, which is the only order in which a name is worth anything.

2. **Nothing appears undefined.** Thread, atomic, mutex, deadlock, Heisenbug — each is
   explained at the moment it first appears, and each is tied back to the notebook.

3. **The analogy's limits are stated.** The "before" answers have no analogy, so they can't
   mislead — but they also can't help. The "after" answers hand you a picture *and* tell
   you the two places it will lie to you, so you don't carry it somewhere it breaks.

And the thing neither "before" answer does at all: say what it *feels like* when this
happens to you. Counters drifting low. A bug that disappears when you add logging. That is
the "look at the water" test — an explanation you can only reach by already knowing the
term is an explanation you'll never reach in the wild.
