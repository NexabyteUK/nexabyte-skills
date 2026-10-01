# Mobile and touch

Guidance for iOS, iPadOS and Android apps, including React Native and Expo apps that target both, and for any touch-first surface. Apple's HIG is the baseline. Android has its own system behaviours that must be respected even when an app deliberately avoids Material's visual style. Platform guidance changes yearly (iOS 26 in 2025, iOS 27 and Android 17 in 2026), so check `sources.md` links when a detail matters.

## Contents

1. The mobile context
2. Touch targets and reach
3. Layout: safe areas, size classes, resizing
4. Navigation: tab bars, toolbars, hierarchy, search
5. Sheets, alerts, action sheets and menus
6. Buttons, toggles and segmented controls
7. Lists, swipe actions and pull to refresh
8. Text input, keyboards and accounts
9. Type and Dynamic Type
10. Feedback: haptics, motion, sound
11. Liquid Glass (iOS 26 and later)
12. Launch, onboarding, permissions and settings
13. Android behaviours to keep
14. Platform details side by side
15. React Native and Expo notes

## 1. The mobile context

People use phones in short bursts, one-handed, while walking, in sunlight, on poor signal, and while being interrupted. Design for that, not for a calm desk:

- **One main job per screen,** with the primary action obvious and reachable.
- **Glanceable:** the key status readable in a second, without reading sentences.
- **Interruption-proof:** state survives backgrounding, calls and app switches. Restore where people were on relaunch, and keep drafts.
- **Connection-tolerant:** see the offline section in `patterns.md`.
- **Fat-finger tolerant:** generous targets, space between destructive and safe actions, and undo.

## 2. Touch targets and reach

- **Hit area:** 44 × 44 pt on iOS (Apple states 28 × 28 pt as the absolute minimum for dense cases), and 48 × 48 dp on Android. A shared cross-platform codebase should design to 48. The visible element can be smaller if padding extends the hit area. NN/G's research suggests about 1 cm square, larger for primary actions or use on the move.
- **Spacing:** Apple suggests about 12 pt around bezelled controls and 24 pt around borderless ones. Keep more space between destructive and safe actions.
- **Reach:** NN/G found the popular claim that the bottom of the screen is easiest to reach largely incorrect. People hold phones in many ways, and the middle is easiest to tap. Apple recommends putting frequent controls in the middle or bottom area. Keep rare or destructive actions away from the easiest spots.
- **One pinned primary action** (Book, Pay) above the home indicator works well in a focused flow. Keep it clear of the home indicator and the keyboard.

## 3. Layout: safe areas, size classes, resizing

- **Respect safe areas and the system layout margins.** Content and controls stay clear of the status bar, Dynamic Island, home indicator, rounded corners and Android system bars. Use the system's margins and readable-width guides rather than hard-coded insets. Backgrounds and scrolling content run full-bleed underneath.
- **Lay out by size class** (compact or regular width and height), not by device or orientation. Keep the same functionality at every size, revealing more in wider layouts (a tab bar becoming a sidebar, list plus detail side by side).
- **Build to resize fluidly.** Avoid fixed widths. Apple's iPhone Duo (2026) has two displays, and Android 16 and 17 ignore orientation and resizability locks on screens at least 600 dp wide. Assume any width.
- **Most important content goes top and leading.** Use alignment and indentation for hierarchy, and spacing or containers for grouping.
- **Plan for the largest text size:** side-by-side arrangements stack vertically at accessibility sizes.

## 4. Navigation: tab bars, toolbars, hierarchy, search

**Tab bar** for flat, top-level sections people switch between:
- Navigation only, never actions. A "Checkout" or "+" tab is wrong; put actions in the toolbar or content.
- Five or fewer tabs. Avoid the overflow "More" tab.
- Always visible except under a modal or in a focused flow. Never hide or disable tabs. If a section is empty, explain that inside it.
- Single-word labels with filled symbols. Badges only for things that need action.
- Each tab keeps its own navigation stack and scroll position.
- From iOS 26 the tab bar floats on Liquid Glass, can minimise on scroll, and can end with a search tab. On iPad it sits at the top and can become a sidebar.

**Hierarchical navigation** (push and pop):
- The standard Back control and swipe from the leading edge. Never block either. The system back button is a chevron, followed by the previous screen's title where it fits (never the literal word "Back"). Keep that title for less confident audiences, because a bare chevron is easy to miss.
- Title the screen briefly (under about 15 characters) and never with the app name. Large titles on top-level screens collapse on scroll.

**Toolbars** (Apple now covers navigation bars under Toolbars):
- At most one prominent primary action, on the trailing edge (Done as a tinted checkmark).
- Up to three groups of controls, organised by function and frequency. Overflow goes into a More (ellipsis) menu.
- Prefer borderless symbols to text, and don't put a text button directly beside a symbol button.
- Let content scroll under bars with the system's scroll edge effect, rather than adding solid backgrounds or hairline dividers.

**Search:** give search a primary place: a search tab or a bottom toolbar field on iOS 26 and later, a search bar at the top on Android, and a field at the top where content below must stay visible. Search as people type, show recents (clearable) and suggestions, default to the broadest scope, and when nothing matches, repeat the query and suggest what to try.

**Avoid hamburger menus** for primary navigation on phones. Hidden navigation is used less.

## 5. Sheets, alerts, action sheets and menus

| Use | iOS | Android |
| --- | --- | --- |
| A short focused task or more detail | Sheet: medium detent (about half height) for quick options, large for longer tasks. A grabber when resizable. Swipe down to dismiss. | Bottom sheet, or a full-screen dialog for a long task |
| A decision about something unexpected or risky | Alert | Dialog |
| Choices about an action the person started (discard or save a draft) | Action sheet | Bottom sheet or dialog |
| Actions on an object | Context menu (long-press) or a menu from a button | Menu or long-press contextual menu |
| Brief confirmation, optionally with undo | An inline state or subtle banner (iOS has no system toast) | Snackbar |

**Sheets:**
- Cancel on the leading edge and Done (or the action) on the trailing edge. Always pair Done with Cancel or Back, and never show all three.
- One sheet at a time, never stacked.
- Use a medium detent for progressive disclosure, not for composing.
- Swipe-down dismisses. If there are unsaved changes, confirm with an action sheet that offers to discard or keep editing (or save).
- Title the sheet with its task.

**Alerts** are rare and actionable:
- Not for purely informational messages, not for common deletions people can undo, and not at launch.
- A specific title of up to two lines (never "Error"), with a message only if it adds something.
- At most three buttons, labelled with verbs. Use exactly "Cancel" for cancel. "OK" only for a purely informational alert, and never "Yes" or "No".
- The likely button goes on the trailing side in a row, or at the top of a stack. Cancel goes leading or at the bottom, and is never the default.
- Apple uses the red destructive style for destructive actions the person *didn't* deliberately choose (Discard, in an alert after tapping Cancel). When the alert confirms an action they did choose (Delete), the button still names the action, and many products style it red. Follow the project's convention, and never make a destructive button the default.

**Action sheets:** up to four buttons including Cancel. The destructive option goes at the top and Cancel at the bottom. Use a one-line title, with no scrolling.

**Menus and context menus:**
- Verb labels with no articles, adding an ellipsis when more input will follow. Most frequent items first, grouped with separators. Submenus at most one level deep.
- Use icons sparingly, either on every item in a group or on none.
- In context menus, show only the most relevant items, in about three groups. Hide unavailable items rather than dimming them. Put destructive items last, in red. Every item must also be reachable elsewhere in the interface.

## 6. Buttons, toggles and segmented controls

- **Buttons:** at least a 44 pt hit area with a visible pressed state. One or two prominent buttons per view, with the preferred one marked by style, not size. Roles: primary (accent), cancel, destructive (red). Never make a destructive button primary. For slow actions, show an activity indicator in the button and block repeat presses.
- **Switches** go inside list rows. Elsewhere use a button or a toggle-style control. Never show on and off by colour alone.
- **Segmented controls** switch between closely related views or filters, never between app sections (use a tab bar). Use up to about five equal-width segments on iPhone, with text or icons but not both mixed.

## 7. Lists, swipe actions and pull to refresh

- **Rows:** at least 44 pt high and text-first. The whole row is tappable when it opens detail, with a disclosure chevron on iOS. Use the grouped style for settings-like screens.
- **Swipe actions** speed up frequent actions (archive, delete, mark done). Because gestures are invisible, mirror them in a context menu, edit mode or the detail view. A full-swipe destructive action needs undo.
- **Pull to refresh** for content that changes. Show the last-updated time if freshness matters.
- **Long alphabetical lists** get sections and an index scrubber, unless rows have trailing accessories.
- **Empty lists** get a proper empty state with the next step and a button for it.

## 8. Text input, keyboards and accounts

- **Get data from the system where possible:** contacts, location, camera, autofill. Prefer pickers, steppers and segmented controls to typing for bounded values. Let people type long or distant values like birth dates and amounts.
- **The right keyboard:** email, number pad, decimal pad, phone, URL.
- **Autofill:** `textContentType` on iOS and `autoComplete` on Android and React Native, for names, emails, addresses, one-time codes and new passwords, so passkeys and password managers work.
- **Turn off autocorrect and auto-capitalisation** for names, emails, usernames and codes.
- **Return key** named for the action (Next, Search, Send, Done). Next moves to the following field.
- **Keep the focused field visible** above the keyboard, the form scrollable, and the submit control reachable.
- **Give placeholder examples** of the format ("name@example.com"), but keep the label visible.
- **Don't open the keyboard automatically** unless typing is the screen's only purpose.
- **Accounts:**
  - Require an account only for features that genuinely need one, and let people browse first.
  - Offer Sign in with Apple or Google, and passkeys.
  - Name the authentication method ("Sign in with Face ID").
  - Provide in-app account deletion (Apple requires it), and explain that subscriptions continue until cancelled.

## 9. Type and Dynamic Type

- **Use the platform text styles** so text follows the person's settings. iOS defaults at the standard size:

  | Style | Size / leading (pt) | Weight |
  | --- | --- | --- |
  | Large Title | 34 / 41 | Regular |
  | Title 1 | 28 / 34 | Regular |
  | Title 2 | 22 / 28 | Regular |
  | Title 3 | 20 / 25 | Regular |
  | Headline | 17 / 22 | Semibold |
  | Body | 17 / 22 | Regular |
  | Callout | 16 / 21 | Regular |
  | Subheadline | 15 / 20 | Regular |
  | Footnote | 13 / 18 | Regular |
  | Caption 1 | 12 / 16 | Regular |
  | Caption 2 | 11 / 13 | Regular |

- **iOS body is 17 pt and the minimum is 11 pt.** On Android, body is usually 14 to 16 sp with a 12 sp minimum, and every text size uses `sp` (Android 14 and later scale text non-linearly up to 200%).
- **Support at least 200% text enlargement.** Text wraps rather than truncating, side-by-side layouts stack, and icons beside text scale with it. Not everything must scale (tab labels, for example).
- **Avoid ultralight, thin and light weights** for UI text.
- **Older audiences:** start larger (body 17 to 19 pt), and keep secondary text, status labels and tab labels readable too (15 pt or more, scaling with the text size setting). Test the largest sizes, because many people raise them.
- **Custom fonts** must support Dynamic Type and Bold Text. A common pattern is a brand font for headings and the system font for body text.

## 10. Feedback: haptics, motion, sound

- **Every touch gets an immediate response:** a highlight on press, then the state change.
- **Feedback uses several channels together** (visual, text, haptic, sound), so no one channel carries meaning alone.
- **Haptics** mark meaningful moments: a toggle, success, a warning, an error. Never use them for every tap or as the only signal. iOS standard controls play haptics automatically. Android hardware varies, so prefer the system's semantic haptic constants over raw vibration, and keep haptics subtle.
- **Motion:** use the system transitions (push, sheet, zoom). Keep motion brief and interruptible, and follow the gesture (dismiss in the direction something came from).
- **Sound** is off for routine interaction, and respects the silent switch.

## 11. Liquid Glass (iOS 26 and later)

Apple's 2025 design introduced Liquid Glass, a translucent material for the control layer that floats above content. Apple retuned it in 2026 (iOS 27) for legibility, and people can now adjust how clear or tinted it is.

- **Use it only in the navigation and control layer:** tab bars, toolbars, sidebars, menus, sheets and floating buttons. Never in content (lists, cards, text). Sliders and toggles turn glassy only while being dragged.
- **Prefer system components,** which adopt Liquid Glass automatically and adapt to accessibility settings. Apply glass to custom controls sparingly. Never stack glass on glass.
- **Variants:** use the regular variant by default (required for text-heavy surfaces like alerts, popovers and sidebars). Use the clear variant only over rich media, with a dimming layer of about 35% if the content beneath is bright.
- **Colour on glass:** keep bars monochrome over colourful content. Tint the background of the one primary action rather than the symbols. Brand colour belongs in the content layer.
- **Shape:** concentric corner radii that echo the device, and capsule-shaped buttons near the screen edges on iPhone.
- **Never depend on one glass appearance.** People's settings, Reduce Transparency and Increase Contrast all change it. NN/G's 2025 review found translucent controls over busy content lose legibility, so check legibility over real content.
- **Cross-platform apps** shouldn't imitate Liquid Glass on Android or the web with blur effects. Use native iOS components where the framework allows, and solid surfaces elsewhere.

## 12. Launch, onboarding, permissions and settings

- **Launch:** the launch screen looks almost identical to the first screen, with no text, logo or advertising. Restore the previous state.
- **Onboarding:** optional, brief and interactive. Prefer contextual tips over a tour, defer setup, and ship good defaults. If skipped, don't show it again, but keep it findable. Ask for ratings or purchases only after people have used the app.
- **Permissions:**
  - Ask when the feature is first used, not at launch, and only for the minimum.
  - Purpose strings are one specific sentence ("Greenhill uses your location to show the nearest shed").
  - An optional explanation screen before a permission request has one button ("Continue"), and it always leads to the system prompt.
  - Respect a refusal and keep the rest of the app working.
- **Settings:** few settings with good defaults, and task options in context. Never duplicate system settings (appearance, text size, accessibility) inside the app; link to the system Settings page instead.

## 13. Android behaviours to keep

Even when an app's visuals are brand-led rather than Material, these system behaviours are expected:

- **System back:**
  - Every screen, sheet, dialog, search field and drawer responds to the back gesture or button, closing the innermost thing first.
  - Apps targeting Android 16 (API 36) get predictive back by default: the system previews the destination during the gesture, and the old back callbacks no longer fire.
  - Intercept back only when needed, such as to protect unsaved changes. Don't intercept it at the root, and don't use "press back again to exit".
- **Edge-to-edge:**
  - Mandatory from Android 15 (API 35), with no opt-out from API 36. Expo SDK 54 and React Native 0.81 enforce it.
  - Draw backgrounds behind the system bars, keep tappable elements out of the bar and gesture insets, and handle keyboard insets.
- **48 dp touch targets,** and body text of at least 12 sp, using `sp` throughout.
- **Runtime permissions** in context:
  - After two denials the system stops prompting, so link people to Settings instead.
  - Location, camera and microphone offer "Only this time".
  - Notifications need permission on Android 13 and later and are off by default for new installs, so ask when the person would want a notification.
- **Notification channels:** granular, named in people's terms ("Booking reminders"), and linked from the app. A channel's importance can't be changed once created, so choose carefully.
- **Large screens:** design for any width and orientation (see section 3).
- **Expected system components:** the Material date and time pickers, snackbars and the system share sheet are what Android users expect, even in a brand-styled app.
- **Motion:** Material 3 Expressive (2025) made springy, gesture-following motion the Android norm. Matching it isn't required, but stiff, linear motion feels dated.
- **Deep links** open with a sensible back stack.

## 14. Platform details side by side

| Detail | iOS | Android |
| --- | --- | --- |
| Back | Chevron at top-leading, plus swipe from the leading edge | System back gesture or button; an Up arrow in the top bar is conventional |
| Primary action in a sheet | Trailing edge of the sheet's top bar, with Cancel leading | Bottom of the sheet, or top-trailing in a full-screen dialog |
| Button and menu capitalisation | Apple's own apps use title case for buttons, menus and tabs | Sentence case |
| Date and time pickers | Native wheels or calendar | Material date picker |
| Share | System share sheet | System share sheet |
| Toast-style feedback | Inline state or a subtle banner | Snackbar |
| Notification settings | Per-app, plus in-app preferences | Per-channel, plus in-app preferences |
| Appearance toggle | Follow the system and don't add an in-app toggle | Follow the system; an in-app override is optional |

A cross-platform product can use sentence case everywhere for consistency (many do). Pick one style per element type and keep it.

## 15. React Native and Expo notes

- **Use platform-adaptive components** (React Navigation native stacks and tabs, native date pickers, native menus and action sheets), so each platform feels right without separate designs.
- **Safe areas:** use `react-native-safe-area-context` on every edge that touches a system bar. Handle edge-to-edge insets on Android, and set status bar styles for both themes.
- **Hit area:** use `hitSlop` or padding to reach 44 pt or 48 dp, and `Pressable` with a pressed style.
- **Accessibility:**
  - Give controls `accessibilityLabel` (or `aria-label`), `accessibilityRole` (or `role`) and `accessibilityState`, and group rows with `accessible`.
  - Announce changes with `AccessibilityInfo.announceForAccessibility`.
- **Text:** leave `allowFontScaling` on. Use `maxFontSizeMultiplier` only for elements that can't reflow, such as tab labels.
- **Haptics:** `expo-haptics`. On Android, prefer `performAndroidHapticsAsync` with the system constants over the simulated impact and notification haptics.
- **Predictive back** in Expo is opt-in through `android.predictiveBackGestureEnabled` at SDK 54 and expected to become the default. Test back behaviour on every screen.
- **Use `Platform.select`** for the small set of conventions in the table above, not for whole screens.
