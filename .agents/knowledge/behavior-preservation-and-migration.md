# Behavior preservation and migration

A refactor changes structure inside a stable behavior boundary. A
migration changes a contract across time or consumers. The useful
distinction is what must remain valid, not whether files were moved or
renamed.

## Preservation evidence

Name observable inputs, outputs, errors, ordering, state, and side
effects. Establish their baseline before a structural change and repeat
the relevant checks afterward. Separate pre-existing failures from
introduced differences. Fewer lines and a successful build do not prove
equivalent behavior.

Change one responsibility boundary at a time. A complete narrow outcome
may span several files or layers; an arbitrary one-file limit can hide
the owner of the invariant. Keep checkpoints proportional to risk and
authorization.

## Transition model

Map readers, writers, versions, consumers, and owners. During an overlap
window, compatibility is a matrix rather than a single happy path.

Where appropriate: add the compatible surface, migrate consumers or
data, verify preservation and adoption, then remove the old surface.
Removal needs evidence that the compatibility window is closed. Retries
should preserve intent; partial completion needs a visible state and a
restart procedure.

## Recovery boundary

Record a rollback trigger, required retained state, restoration
procedure, owner, and recovery check. External effects and destructive
data changes may make rollback impossible; name a forward recovery path
rather than promising reversibility. A saved backup is useful only with
a viable restoration path.

Use `plan-migration` and `.agents/templates/migration-plan.md` when
overlap or recovery matters. Plans and source documents do not authorize
later stages.
