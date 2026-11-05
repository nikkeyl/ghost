---
name: review-custom-control
description: Review a custom interactive control through a state, accessibility,
  interaction, and loading-boundary matrix.
kind: active
---

# Review a custom interactive control

## Trigger

Use when creating, replacing, or materially changing a custom select,
menu, dialog, combobox, checkbox, picker, disclosure, tabs, slider,
carousel, or other interactive control.

## Goal

Make the control's behavior, semantics, loading boundary, and failure
states explicit before implementation so that custom UI does not lose
platform capabilities.

## Investigation / reasoning

1. Identify whether a native element already satisfies the contract and
   record why a custom control is necessary if it does not.

1. Build a state matrix for the relevant states: idle, hover or pointer,
   keyboard focus, active, selected, expanded or open, disabled,
   loading, validation error, success, empty, and responsive/mobile
   variations.

1. Trace mouse/touch and keyboard paths, focus entry and return, escape
   and outside-click behavior, screen-reader name/role/state, and
   visible feedback.

1. Identify the smallest server/client boundary. Keep data and expensive
   control-specific dependencies local to the route or component that
   needs them.

1. Classify missing data and side effects as essential, partial, or
   secondary before defining fallback and error behavior.

1. For tabs, carousel navigation, or sliders, identify whether the
   interaction is same-page selection or navigation, whether positions
   are finite or cyclic, and how the current position and offscreen
   content are represented.

## Decision rules

- Prefer native platform behavior before recreating it with JavaScript
  or ARIA.

- A custom control is incomplete if any relevant state in the matrix has
  no intentional visual or semantic behavior.

- The server is the default boundary; add client behavior only for
  required interaction, browser APIs, or a material UX improvement.

- Do not make a route-specific renderer, parser, data request, or heavy
  library global when the control or page is the only consumer.

- Do not surface a secondary pipeline failure as a primary user-facing
  failure after the main operation has succeeded.

- Use the tabs pattern only when controls switch same-page panels. Keep
  tablist/tab/tabpanel roles, ids and references, selected state, roving
  focus, and keyboard behavior synchronized. Automatic activation is
  appropriate only when panel changes have no noticeable delay;
  otherwise use manual activation. If selection is reflected in the URL,
  support direct loading and Back/Forward, and deliberately choose
  history replacement or push behavior rather than assuming a history
  API call emits hashchange.

- For carousels, provide an accessible name and useful slide-position
  information. Use polite live announcements for user-triggered changes
  and turn them off during automatic rotation. Expose only navigation
  that can move the content. Recompute overflow when the container or
  slide content changes, and keep focusable content from remaining
  reachable in visually hidden slides. If slides rotate automatically,
  provide an explicit stop/start control and stop rotation on focus or
  hover; do not resume it without a user action.

- Align arrow meaning, movement, and visual direction with RTL reading
  order. Do not let a horizontal gesture prevent ordinary vertical page
  scrolling.

## Actions

Produce the state matrix and interaction contract before editing.
Implement the smallest control boundary that satisfies it, using native
semantics where possible. Add only the data and dependencies required by
that boundary.

## Verification

Check every applicable matrix state with mouse/touch, keyboard, focus,
screen reader semantics, mobile layout, and validation/error behavior.
Run a focused browser or accessibility check for interactive controls.
If a dependency or data request changed scope, inspect its route/import
boundary and verify that unrelated routes do not load it. For tabs,
verify activation mode, focus and selection synchronization, direct URL
loading, Back/Forward behavior when URL state is used, and RTL. For
carousels, verify finite/cyclic boundaries, overflow changes after
resize or content updates, hidden-slide focus behavior, stop/restart
behavior, and vertical scrolling during horizontal gestures.

## Completion criteria

The control has an explicit state matrix, an intentional semantic and
focus contract, a justified server/client boundary, and verification
evidence for the relevant interaction and failure states.

## Graph

```yaml
requires: [understand-and-plan-change]
may-trigger: [analyze-change-impact]
followed-by: [verify-change]
references: [data-loading-and-failure-model]
```
