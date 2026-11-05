# LibAdwaita / GNOME Theme for Visual Studio Code

<p align="left">
  <img src="assets/icon.png" width="112" alt="LibAdwaita / GNOME Theme Icon" />
</p>

An authentic, standards-compliant **LibAdwaita 1.6+ / GNOME 47+** color theme suite for Visual Studio Code.

Designed from the ground up using official upstream **LibAdwaita CSS variables**, the **GNOME Human Interface Guidelines (HIG)** palette, and Christian Hergert's **GtkSourceView 5 (`Adwaita.xml` & `Adwaita-dark.xml`)** syntax schemes used in **GNOME Builder** and **GNOME Text Editor**.

---

## Included Theme Variants

1. **LibAdwaita Dark** — Modern cool-neutral dark mode (`#1d1d20` editor view, `#222226` window, `#2e2e32` headerbar & primary rail, `#28282c` secondary split sidebar).
2. **LibAdwaita Light** — Crisp paper-white and alabaster light mode (`#ffffff` editor view & headerbar, `#fafafb` window, `#ebebed` primary rail, `#f3f3f5` secondary split sidebar).
3. **LibAdwaita Dark (High Contrast)** — Follows LibAdwaita's `@media (prefers-contrast: more)` specification (`50%` border opacity, `80%` focus ring opacity, `90%` dim label opacity).
4. **LibAdwaita Light (High Contrast)** — High-contrast light accessibility variant with crisp `50%` borders and reinforced token contrast.

---

## Upstream Standards & Color References

### 1. LibAdwaita 1.6+ Surface Architecture
Unlike pre-2023 Adwaita themes that used warm brownish grays (`#242424` / `#303030`), LibAdwaita 1.4 through 1.6+ uses a cool-neutral surface hierarchy defined in [`src/stylesheet/_colors.scss`](https://gitlab.gnome.org/GNOME/libadwaita/-/blob/main/src/stylesheet/_colors.scss):

| LibAdwaita CSS Variable | VS Code Workbench Mapping | Dark Hex | Light Hex |
| :--- | :--- | :--- | :--- |
| `--view-bg-color` | `editor.background`, `minimap.background`, `terminal.background` | `#1d1d20` | `#ffffff` |
| `libadwaita-dark-alt` / `light_3` | `editor.lineHighlightBackground` | `#242428` | `#f6f5f4` |
| `--window-bg-color` | `panel.background`, `peekViewEditor.background` | `#222226` | `#fafafb` |
| `--headerbar-bg-color` | `titleBar.activeBackground`, `editorGroupHeader.tabsBackground`, `statusBar.background` | `#2e2e32` | `#ffffff` |
| `--sidebar-bg-color` | `activityBar.background`, `sideBarSectionHeader.background` | `#2e2e32` | `#ebebed` |
| `--secondary-sidebar-bg-color` | `sideBar.background`, `textBlockQuote.background` | `#28282c` | `#f3f3f5` |
| `--dialog-bg-color` / `--popover-bg-color` | `quickInput.background`, `editorWidget.background`, `menu.background` | `#36363a` | `#ffffff` / `#fafafb` |
| `--accent-bg-color` / `--accent-color` | `button.background`, `focusBorder`, `badge.background`, `tab.activeBorderTop` | `#3584e4` / `#78aeed` | `#3584e4` / `#1c71d8` |
| `--border-color` (`15%` / `50%` HC) | `sideBar.border`, `panel.border`, `editorGroup.border`, `input.border` | `#ffffff26` | `#00000626` |

### 2. GtkSourceView 5 Syntax Highlighting (`Adwaita` & `Adwaita-dark`)
Syntax and LSP semantic tokens map directly to GNOME's official [`Adwaita-dark.xml`](https://gitlab.gnome.org/GNOME/gtksourceview/-/blob/master/data/styles/Adwaita-dark.xml) and [`Adwaita.xml`](https://gitlab.gnome.org/GNOME/gtksourceview/-/blob/master/data/styles/Adwaita.xml):

| Syntax Category | GtkSourceView Rule | Dark Token (`Adwaita-dark.xml`) | Light Token (`Adwaita.xml`) |
| :--- | :--- | :--- | :--- |
| **Default Text** | `text` | `#deddda` (`light_4`) | `#3d3846` (`dark_4`) |
| **Keywords / Statements** | `def:statement` (bold) | `#ffa348` (`orange_2`) | `#c64600` (`orange_5`) |
| **Preprocessor / Attributes / CSS Props** | `def:preprocessor`, `xml:attribute-name` | `#ff7800` (`orange_3`) | `#e66100` (`orange_4`) |
| **Functions & Methods** | `def:function`, `python:builtin-function` | `#62a0ea` (`blue_2`) | `#1c71d8` (`blue_4`) |
| **Strings** | `def:string` | `#5bc8af` (`teal_2`) | `#218787` (`teal_5`) |
| **Types, Classes & Structs** | `def:type` (bold), `python:class-name` | `#5bc8af` (`teal_2` bold) | `#218787` (`teal_5` bold) |
| **Tags, Headings & Selectors** | `def:heading`, `xml:element-name`, `css:type-selector` | `#33b2a4` (`teal_3`) | `#218787` (`teal_5`) |
| **Numbers, Constants, Booleans, Macros** | `def:number`, `def:constant`, `rust:macro` | `#7d8ac7` (`violet_2`) | `#4e57ba` (`violet_4`) |
| **Special Chars, Escapes & Deletions** | `def:special-char`, `diff:removed-line` | `#f66151` (`red_1`) | `#ed333b` (`red_2`) |
| **Properties & Identifiers** | `def:identifier` | `#8ff0a4` (`green_1`) | `#26a269` (`green_5`) |
| **Namespaces & Diff Locations** | `xml:namespace`, `diff:location` | `#f5c211` (`yellow_4`) | `#d38b09` (`yellow_6`) |
| **Comments** | `def:comment` (italic) | `#77767b` (`dark_1`) | `#77767b` (`dark_1`) |
| **Doc Comments & Shebangs** | `def:doc-comment-element` (bold) | `#9a9996` (`light_7`) | `#504e55` (`dark_3`) |

---

## How to Install & Use

### Method 1: Local Symlink (Fastest for Development & Immediate Use)
Link this repository directly into your Visual Studio Code extensions directory:

```bash
ln -s ~/Code/libadwaita-vscode-theme ~/.vscode/extensions/j4nnn.libadwaita-vscode-theme-1.0.0
```
*(If you use **VSCodium** or **Code - OSS**, link to `~/.vscode-oss/extensions/` instead.)*

### Method 2: Package and Install `.vsix`
If you have `@vscode/vsce` (or `npx @vscode/vsce`) available:

```bash
cd ~/Code/libadwaita-vscode-theme
npx @vscode/vsce package
code --install-extension libadwaita-vscode-theme-1.0.0.vsix
```

### Method 3: Run in Extension Development Host
Open the repository in VS Code and press **`F5`**:

```bash
code ~/Code/libadwaita-vscode-theme
```

---

## Activating the Theme & Recommended GNOME Settings

1. Open the Command Palette in VS Code (`Ctrl+Shift+P`).
2. Run **Preferences: Color Theme** (`Ctrl+K Ctrl+T`).
3. Choose one of:
   - **LibAdwaita Dark**
   - **LibAdwaita Light**
   - **LibAdwaita Dark (High Contrast)**
   - **LibAdwaita Light (High Contrast)**

### Recommended `settings.json` for a Native GNOME Look
To make VS Code blend seamlessly into a GNOME 47+ / LibAdwaita desktop (matching **GNOME Builder** and **GNOME Text Editor** with Adwaita Sans / Adwaita Mono or Cantarell / Source Code Pro):

```jsonc
{
  "workbench.colorTheme": "LibAdwaita Dark",
  "workbench.preferredDarkColorTheme": "LibAdwaita Dark",
  "workbench.preferredLightColorTheme": "LibAdwaita Light",
  "workbench.preferredHighContrastColorTheme": "LibAdwaita Dark (High Contrast)",
  "workbench.preferredHighContrastLightColorTheme": "LibAdwaita Light (High Contrast)",
  "window.autoDetectColorScheme": true,
  "window.titleBarStyle": "custom",
  "window.commandCenter": true,
  "editor.semanticHighlighting.enabled": true,
  "editor.fontFamily": "'Adwaita Mono', 'Source Code Pro', 'JetBrains Mono', monospace",
  "editor.fontSize": 13.5,
  "editor.lineHeight": 1.55,
  "editor.renderLineHighlight": "all",
  "editor.bracketPairColorization.enabled": true
}
```

---

## Modifying or Rebuilding the Themes

All four theme JSON files in `themes/` are deterministically generated from [`src/palette.py`](src/palette.py) and [`src/generate_themes.py`](src/generate_themes.py) (zero external dependencies, requires only Python 3):

```bash
python3 src/generate_themes.py
```

---

## Official References
- [LibAdwaita Documentation — CSS Variables](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/css-variables.html)
- [LibAdwaita Documentation — Named Colors & HIG Palette](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/named-colors.html)
- [GNOME GitLab — `libadwaita/src/stylesheet/_colors.scss`](https://gitlab.gnome.org/GNOME/libadwaita/-/blob/main/src/stylesheet/_colors.scss)
- [GNOME GitLab — `libadwaita/src/stylesheet/_palette.scss`](https://gitlab.gnome.org/GNOME/libadwaita/-/blob/main/src/stylesheet/_palette.scss)
- [GNOME GitLab — `gtksourceview/data/styles/Adwaita-dark.xml`](https://gitlab.gnome.org/GNOME/gtksourceview/-/blob/master/data/styles/Adwaita-dark.xml)
- [GNOME GitLab — `gtksourceview/data/styles/Adwaita.xml`](https://gitlab.gnome.org/GNOME/gtksourceview/-/blob/master/data/styles/Adwaita.xml)
- [GNOME Human Interface Guidelines — Color](https://developer.gnome.org/hig/guidelines/color.html)
