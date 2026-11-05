# Changelog

All notable changes to the **LibAdwaita / GNOME Theme** extension will be documented in this file.

## [1.0.0] - 2026-11-04

### Added
- **LibAdwaita Dark**: Updated GNOME 47+ / LibAdwaita 1.6+ dark theme (`#1d1d20` view, `#222226` window, `#2e2e32` headerbar/sidebar, `#28282c` secondary sidebar) paired with `GtkSourceView 5` (`Adwaita-dark.xml`) syntax highlighting.
- **LibAdwaita Light**: Updated GNOME 47+ / LibAdwaita 1.6+ light theme (`#ffffff` view/headerbar, `#fafafb` window, `#ebebed` sidebar, `#f3f3f5` secondary sidebar) paired with `GtkSourceView 5` (`Adwaita.xml`) syntax highlighting.
- **LibAdwaita Dark (High Contrast)** & **LibAdwaita Light (High Contrast)**: High-contrast accessibility variants honoring LibAdwaita's `@media (prefers-contrast: more)` specifications (`50%` border opacity, `80%` focus ring opacity, `90%` dim opacity).
- Full **Semantic Highlighting** (`semanticHighlighting: true` + `semanticTokenColors`) and comprehensive **TextMate** grammar scopes across C, C++, Rust, Python, Vala, TypeScript/JavaScript, Go, C#, HTML/XML/Blueprint, CSS/SCSS, Markdown, and Diffs.
- Complete **GNOME Console / Ptyxis** 16-color ANSI terminal palette integration.
- Deterministic theme generator (`src/generate_themes.py`) and color reference module (`src/palette.py`).
