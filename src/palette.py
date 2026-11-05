"""Official GNOME HIG, LibAdwaita 1.6+, and GtkSourceView 5 Color Definitions.

References:
- LibAdwaita CSS Variables & Palette:
  https://gitlab.gnome.org/GNOME/libadwaita/-/blob/main/src/stylesheet/_palette.scss
  https://gitlab.gnome.org/GNOME/libadwaita/-/blob/main/src/stylesheet/_colors.scss
  https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/css-variables.html
- GtkSourceView 5 Style Schemes (Adwaita & Adwaita-dark):
  https://gitlab.gnome.org/GNOME/gtksourceview/-/blob/master/data/styles/Adwaita-dark.xml
  https://gitlab.gnome.org/GNOME/gtksourceview/-/blob/master/data/styles/Adwaita.xml
- GNOME Human Interface Guidelines (Color):
  https://developer.gnome.org/hig/guidelines/color.html
"""

from typing import Dict


def with_alpha(hex_color: str, alpha_pct: float) -> str:
    """Convert a 6-digit hex color (#RRGGBB) + alpha percentage (0..100) to #RRGGBBAA."""
    clean = hex_color.lstrip("#")
    if len(clean) != 6:
        raise ValueError(f"Expected 6-char hex color, got {hex_color}")
    alpha_int = max(0, min(255, round((alpha_pct / 100.0) * 255)))
    return f"#{clean.lower()}{alpha_int:02x}"


# ---------------------------------------------------------------------------
# 1. GNOME HIG & GtkSourceView 5 Named Palette
#    Upstream: libadwaita/_palette.scss + gtksourceview/Adwaita*.xml
# ---------------------------------------------------------------------------
GNOME_PALETTE: Dict[str, str] = {
    # Blue
    "blue_1": "#99c1f1",
    "blue_2": "#62a0ea",
    "blue_3": "#3584e4",
    "blue_4": "#1c71d8",
    "blue_5": "#1a5fb4",
    "blue_6": "#1b497e",
    "blue_7": "#193d66",
    # Green & Chameleon
    "green_1": "#8ff0a4",
    "green_2": "#57e389",
    "green_3": "#33d17a",
    "green_4": "#2ec27e",
    "green_5": "#26a269",
    "green_6": "#1f7f56",
    "green_7": "#1c6849",
    "chameleon_3": "#4e9a06",
    # Teal (GtkSourceView 5 extended palette)
    "teal_1": "#93ddc2",
    "teal_2": "#5bc8af",
    "teal_3": "#33b2a4",
    "teal_4": "#26a1a2",
    "teal_5": "#218787",
    # Yellow
    "yellow_1": "#f9f06b",
    "yellow_2": "#f8e45c",
    "yellow_3": "#f6d32d",
    "yellow_4": "#f5c211",
    "yellow_5": "#e5a50a",
    "yellow_6": "#d38b09",
    # Orange
    "orange_1": "#ffbe6f",
    "orange_2": "#ffa348",
    "orange_3": "#ff7800",
    "orange_4": "#e66100",
    "orange_5": "#c64600",
    # Red
    "red_1": "#f66151",
    "red_2": "#ed333b",
    "red_3": "#e01b24",
    "red_4": "#c01c28",
    "red_5": "#a51d2d",
    # Purple & Violet
    "purple_1": "#dc8add",
    "purple_2": "#c061cb",
    "purple_3": "#9141ac",
    "purple_4": "#813d9c",
    "purple_5": "#613583",
    "violet_2": "#7d8ac7",
    "violet_3": "#6362c8",
    "violet_4": "#4e57ba",
    # Brown
    "brown_1": "#cdab8f",
    "brown_2": "#b5835a",
    "brown_3": "#986a44",
    "brown_4": "#865e3c",
    "brown_5": "#63452c",
    # Light Neutrals (GtkSourceView 5 Adwaita scale)
    "light_1": "#ffffff",
    "light_2": "#fcfcfc",
    "light_3": "#f6f5f4",
    "light_4": "#deddda",
    "light_5": "#c0bfbc",
    "light_6": "#b0afac",
    "light_7": "#9a9996",
    # Dark Neutrals (LibAdwaita HIG scale)
    "dark_1": "#77767b",
    "dark_2": "#5e5c64",
    "dark_3": "#504e55",
    "dark_4": "#3d3846",
    "dark_5": "#241f31",
    "dark_6": "#121212",
    "dark_7": "#000000",
    # Dark Neutrals (GtkSourceView Adwaita-dark neutral gray scale)
    "gsv_dark_1": "#777777",
    "gsv_dark_2": "#5e5e5e",
    "gsv_dark_3": "#505050",
    "gsv_dark_4": "#3d3d3d",
    "gsv_dark_5": "#242424",
    # LibAdwaita 1.5+ System Accent Colors
    "accent_blue": "#3584e4",
    "accent_teal": "#2190a4",
    "accent_green": "#3a944a",
    "accent_yellow": "#c88800",
    "accent_orange": "#ed5b00",
    "accent_red": "#e62d42",
    "accent_pink": "#d56199",
    "accent_purple": "#9141ac",
    "accent_slate": "#6f8396",
}


# ---------------------------------------------------------------------------
# 2. LibAdwaita 1.6+ Semantic Surface & UI Tokens
#    Upstream: libadwaita/src/stylesheet/_colors.scss
# ---------------------------------------------------------------------------
LIBADWAITA_DARK_UI: Dict[str, str] = {
    # Core surfaces (updated cool-neutral dark palette from LibAdwaita 1.4-1.6+)
    "window_bg": "#222226",
    "window_fg": "#ffffff",
    "view_bg": "#1d1d20",
    "view_bg_alt": "#242428",          # Adwaita-dark.xml current-line (libadwaita-dark-alt)
    "view_fg": "#ffffff",
    "editor_fg": "#deddda",            # Balanced high-readability text (light_4 / light_5 blend)
    "editor_fg_muted": "#c0bfbc",      # Adwaita-dark.xml light_5
    "headerbar_bg": "#2e2e32",
    "headerbar_fg": "#ffffff",
    "headerbar_backdrop": "#222226",
    "sidebar_bg": "#2e2e32",
    "sidebar_fg": "#ffffff",
    "sidebar_backdrop": "#28282c",
    "secondary_sidebar_bg": "#28282c",
    "secondary_sidebar_fg": "#ffffff",
    "secondary_sidebar_backdrop": "#252529",
    "dialog_bg": "#36363a",
    "popover_bg": "#36363a",
    "thumbnail_bg": "#39393d",
    "toast_bg": "#505053",
    "card_bg": with_alpha("#ffffff", 8),
    # Accents & standalone oklab-adjusted colors
    "accent_bg": "#3584e4",            # @blue_3
    "accent_fg": "#ffffff",
    "accent_color": "#78aeed",         # oklab(from #3584e4 max(l, 0.85) a b)
    "destructive_bg": "#c01c28",       # @red_4
    "destructive_color": "#ff7b63",
    "success_bg": "#26a269",           # @green_5
    "success_color": "#57e389",
    "warning_bg": "#cd9309",
    "warning_color": "#f8e45c",
    "error_bg": "#c01c28",             # @red_4
    "error_color": "#ff7b63",
    # Opacity-derived tokens (LibAdwaita 1.6 _colors.scss)
    "border": with_alpha("#ffffff", 15),
    "border_subtle": with_alpha("#ffffff", 10),
    "shade": with_alpha("#000006", 36),
    "sidebar_border": with_alpha("#000006", 36),
    "focus_border": with_alpha("#78aeed", 50),
    "dim_fg": with_alpha("#ffffff", 55),
    "disabled_fg": with_alpha("#ffffff", 50),
    # Interactive states (currentColor mixing in _colors.scss)
    "hover": with_alpha("#ffffff", 7),
    "active": with_alpha("#ffffff", 16),
    "selected": with_alpha("#ffffff", 10),
    "selected_hover": with_alpha("#ffffff", 13),
    "selected_active": with_alpha("#ffffff", 19),
    "view_hover": with_alpha("#ffffff", 4),
    "view_active": with_alpha("#ffffff", 8),
    "view_selected": with_alpha("#3584e4", 25),
    "view_selected_hover": with_alpha("#3584e4", 32),
    "view_selected_active": with_alpha("#3584e4", 39),
    "trough": with_alpha("#ffffff", 15),
    "trough_hover": with_alpha("#ffffff", 20),
    "trough_active": with_alpha("#ffffff", 25),
}


LIBADWAITA_LIGHT_UI: Dict[str, str] = {
    # Core surfaces (updated LibAdwaita 1.4-1.6+ light palette)
    "window_bg": "#fafafb",
    "window_fg": "#323237",            # RGB(0 0 6 / 80%) on #fafafb
    "view_bg": "#ffffff",
    "view_bg_alt": "#f6f5f4",          # Adwaita.xml current-line (light_3)
    "view_fg": "#323237",
    "editor_fg": "#3d3846",            # Adwaita.xml dark_4 / dark_3
    "editor_fg_muted": "#504e55",      # Adwaita.xml dark_3
    "headerbar_bg": "#ffffff",
    "headerbar_fg": "#323237",
    "headerbar_backdrop": "#fafafb",
    "sidebar_bg": "#ebebed",
    "sidebar_fg": "#323237",
    "sidebar_backdrop": "#f2f2f4",
    "secondary_sidebar_bg": "#f3f3f5",
    "secondary_sidebar_fg": "#323237",
    "secondary_sidebar_backdrop": "#f6f6fa",
    "dialog_bg": "#fafafb",
    "popover_bg": "#ffffff",
    "thumbnail_bg": "#ffffff",
    "toast_bg": "#323237",
    "card_bg": "#ffffff",
    # Accents & standalone oklab-adjusted colors
    "accent_bg": "#3584e4",            # @blue_3
    "accent_fg": "#ffffff",
    "accent_color": "#1c71d8",         # oklab(from #3584e4 min(l, 0.5) a b)
    "destructive_bg": "#e01b24",       # @red_3
    "destructive_color": "#c01c28",
    "success_bg": "#2ec27e",           # @green_4
    "success_color": "#26a269",
    "warning_bg": "#e5a50a",           # @yellow_5
    "warning_color": "#ae7b03",
    "error_bg": "#e01b24",             # @red_3
    "error_color": "#c01c28",
    # Opacity-derived tokens (LibAdwaita 1.6 _colors.scss)
    "border": with_alpha("#000006", 15),
    "border_subtle": with_alpha("#000006", 10),
    "shade": with_alpha("#000006", 12),
    "sidebar_border": with_alpha("#000006", 9),
    "focus_border": with_alpha("#1c71d8", 50),
    "dim_fg": with_alpha("#000006", 55),
    "disabled_fg": with_alpha("#000006", 45),
    # Interactive states (currentColor mixing in _colors.scss)
    "hover": with_alpha("#000006", 7),
    "active": with_alpha("#000006", 16),
    "selected": with_alpha("#000006", 10),
    "selected_hover": with_alpha("#000006", 13),
    "selected_active": with_alpha("#000006", 19),
    "view_hover": with_alpha("#000006", 4),
    "view_active": with_alpha("#000006", 8),
    "view_selected": with_alpha("#3584e4", 22),
    "view_selected_hover": with_alpha("#3584e4", 30),
    "view_selected_active": with_alpha("#3584e4", 38),
    "trough": with_alpha("#000006", 15),
    "trough_hover": with_alpha("#000006", 20),
    "trough_active": with_alpha("#000006", 25),
}


# ---------------------------------------------------------------------------
# 3. GtkSourceView 5 Syntax Token Palettes
#    Upstream: Adwaita-dark.xml & Adwaita.xml by Christian Hergert (GNOME)
# ---------------------------------------------------------------------------
SYNTAX_DARK: Dict[str, str] = {
    "text": "#deddda",                 # High-legibility warm white (light_4)
    "text_secondary": "#c0bfbc",       # Adwaita-dark.xml def:text (light_5)
    "comment": "#77767b",              # dark_1 (def:comment)
    "doc_comment": "#9a9996",          # light_7 (def:doc-comment-element / def:shebang)
    "keyword": "#ffa348",              # orange_2 (def:statement, rust:lifetime)
    "preprocessor": "#ff7800",         # orange_3 / orange_4 (def:preprocessor, css:property-name, xml:attribute-name)
    "string": "#5bc8af",               # teal_2 (def:string)
    "type": "#5bc8af",                 # teal_2 bold (def:type, c:type-keyword, python:class-name)
    "tag_heading": "#33b2a4",          # teal_3 (def:heading, css:type-selector, xml:element-name)
    "function": "#62a0ea",             # blue_2 (def:function, python:builtin-function, def:link-destination)
    "function_light": "#99c1f1",       # blue_1 (method calls / secondary declarations)
    "number_constant": "#7d8ac7",      # violet_2 (def:number, def:constant, def:boolean, rust:macro, xml:attribute-value)
    "format_specifier": "#c061cb",     # purple_2 (format / regex / interpolation)
    "special_char": "#f66151",         # red_1 (def:special-char, c:signal-name, python:module-handler, diff:removed-line)
    "link_text": "#ed333b",            # red_2 (def:link-text)
    "identifier_property": "#8ff0a4",  # green_1 / chameleon softened for dark mode readability
    "parameter": "#ffbe6f",            # orange_1 (distinct warm parameter tone)
    "namespace_warning": "#f5c211",    # yellow_4 (xml:namespace, diff:location, def:warning)
    "error": "#e01b24",                # red_3 / red_4 (def:error)
}

SYNTAX_LIGHT: Dict[str, str] = {
    "text": "#3d3846",                 # dark_4 / dark_3 (Adwaita.xml text)
    "text_secondary": "#504e55",       # dark_3
    "comment": "#77767b",              # dark_1 (def:comment)
    "doc_comment": "#504e55",          # dark_3 (def:doc-comment-element)
    "keyword": "#c64600",              # orange_5 (def:statement, def:preprocessor, rust:lifetime)
    "preprocessor": "#e66100",         # orange_4 / orange_5 (css:property-name, xml:attribute-name)
    "string": "#218787",               # teal_5 (def:string)
    "type": "#218787",                 # teal_5 bold (def:type, c:type-keyword, python:class-name)
    "tag_heading": "#218787",          # teal_5 (def:heading, css:type-selector, xml:element-name)
    "function": "#1c71d8",             # blue_4 (def:function, python:builtin-function)
    "function_light": "#1a5fb4",       # blue_5 (method calls / secondary declarations)
    "number_constant": "#4e57ba",      # violet_4 (def:number, def:constant, def:boolean, rust:macro, xml:attribute-value)
    "format_specifier": "#813d9c",     # purple_4 (format / regex / interpolation)
    "special_char": "#ed333b",         # red_2 (def:special-char)
    "link_text": "#e01b24",            # red_3 (def:link-text, python:module-handler)
    "identifier_property": "#26a269",  # green_5 / chameleon_3 (#4e9a06)
    "parameter": "#986a44",            # brown_3 (distinct warm parameter tone on white)
    "namespace_warning": "#d38b09",    # yellow_6 (xml:namespace, diff:location)
    "error": "#c01c28",                # red_4 (def:error)
}


# ---------------------------------------------------------------------------
# 4. GNOME Console (kgx) / Ptyxis Terminal ANSI 16-Color Palette
# ---------------------------------------------------------------------------
TERMINAL_DARK: Dict[str, str] = {
    "background": "#1d1d20",
    "foreground": "#deddda",
    "cursor": "#deddda",
    "selection": with_alpha("#3584e4", 30),
    "ansiBlack": "#241f31",
    "ansiRed": "#c01c28",
    "ansiGreen": "#2ec27e",
    "ansiYellow": "#f5c211",
    "ansiBlue": "#1e78e4",
    "ansiMagenta": "#9841bb",
    "ansiCyan": "#0ab9dc",
    "ansiWhite": "#c0bfbc",
    "ansiBrightBlack": "#5e5c64",
    "ansiBrightRed": "#ed333b",
    "ansiBrightGreen": "#57e389",
    "ansiBrightYellow": "#f8e45c",
    "ansiBrightBlue": "#51a1ff",
    "ansiBrightMagenta": "#c061cb",
    "ansiBrightCyan": "#4fd2fd",
    "ansiBrightWhite": "#ffffff",
}

TERMINAL_LIGHT: Dict[str, str] = {
    "background": "#ffffff",
    "foreground": "#323237",
    "cursor": "#323237",
    "selection": with_alpha("#3584e4", 25),
    "ansiBlack": "#241f31",
    "ansiRed": "#c01c28",
    "ansiGreen": "#26a269",
    "ansiYellow": "#b5835a",
    "ansiBlue": "#1a5fb4",
    "ansiMagenta": "#813d9c",
    "ansiCyan": "#218787",
    "ansiWhite": "#deddda",
    "ansiBrightBlack": "#5e5c64",
    "ansiBrightRed": "#e01b24",
    "ansiBrightGreen": "#2ec27e",
    "ansiBrightYellow": "#e5a50a",
    "ansiBrightBlue": "#3584e4",
    "ansiBrightMagenta": "#9141ac",
    "ansiBrightCyan": "#26a1a2",
    "ansiBrightWhite": "#f6f5f4",
}
