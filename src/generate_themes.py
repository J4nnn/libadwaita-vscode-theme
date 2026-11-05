#!/usr/bin/env python3
"""Generate Visual Studio Code themes from LibAdwaita 1.6+ & GtkSourceView 5 tokens."""

import json
from pathlib import Path
from typing import Any, Dict, List

from palette import (
    GNOME_PALETTE,
    LIBADWAITA_DARK_UI,
    LIBADWAITA_LIGHT_UI,
    SYNTAX_DARK,
    SYNTAX_LIGHT,
    TERMINAL_DARK,
    TERMINAL_LIGHT,
    with_alpha,
)


def build_workbench_colors(
    ui: Dict[str, str],
    syntax: Dict[str, str],
    term: Dict[str, str],
    is_dark: bool,
    high_contrast: bool = False,
) -> Dict[str, Any]:
    """Map LibAdwaita 1.6+ CSS variables to VS Code workbench color keys."""
    p = GNOME_PALETTE

    border = (
        with_alpha("#ffffff" if is_dark else "#000006", 50)
        if high_contrast
        else ui["border"]
    )
    focus_border = (
        with_alpha(ui["accent_color"], 80)
        if high_contrast
        else ui["focus_border"]
    )
    dim_fg = (
        with_alpha("#ffffff" if is_dark else "#000006", 90)
        if high_contrast
        else ui["dim_fg"]
    )
    line_num_fg = (
        "#9a9996" if is_dark else "#77767b"
    ) if high_contrast else ("#5e5e5e" if is_dark else "#b0afac")
    line_num_active_fg = (
        "#ffffff" if is_dark else "#241f31"
    ) if high_contrast else ("#c0bfbc" if is_dark else "#77767b")

    colors: Dict[str, Any] = {
        # Base & Contrast
        "focusBorder": focus_border,
        "foreground": ui["window_fg"],
        "disabledForeground": ui["disabled_fg"],
        "widget.border": border,
        "widget.shadow": ui["shade"],
        "selection.background": ui["view_selected_active"],
        "descriptionForeground": dim_fg,
        "errorForeground": ui["error_color"],
        "icon.foreground": ui["window_fg"],
        "sash.hoverBorder": ui["accent_bg"],

        # Window & Text
        "window.activeBorder": border if high_contrast else "#00000000",
        "window.inactiveBorder": border if high_contrast else "#00000000",
        "textBlockQuote.background": ui["secondary_sidebar_bg"],
        "textBlockQuote.border": ui["accent_bg"],
        "textCodeBlock.background": ui["secondary_sidebar_bg"],
        "textLink.activeForeground": ui["accent_bg"],
        "textLink.foreground": ui["accent_color"],
        "textPreformat.foreground": syntax["number_constant"],
        "textPreformat.background": ui["secondary_sidebar_bg"],
        "textSeparator.foreground": border,

        # Action & Toolbar (AdwHeaderBar / AdwButton flat style)
        "toolbar.hoverBackground": ui["hover"],
        "toolbar.hoverOutline": border if high_contrast else "#00000000",
        "toolbar.activeBackground": ui["active"],

        # Buttons (AdwButton .suggested-action & secondary buttons)
        "button.background": ui["accent_bg"],
        "button.foreground": ui["accent_fg"],
        "button.hoverBackground": p["blue_2"] if is_dark else p["blue_4"],
        "button.border": border if high_contrast else "#00000000",
        "button.secondaryBackground": ui["selected"],
        "button.secondaryForeground": ui["window_fg"],
        "button.secondaryHoverBackground": ui["selected_hover"],
        "checkbox.background": ui["view_bg"],
        "checkbox.foreground": ui["window_fg"],
        "checkbox.border": border,
        "checkbox.selectBackground": ui["accent_bg"],
        "checkbox.selectBorder": ui["accent_bg"],

        # Dropdowns (GtkDropDown / Popover)
        "dropdown.background": ui["popover_bg"],
        "dropdown.listBackground": ui["popover_bg"],
        "dropdown.foreground": ui["window_fg"],
        "dropdown.border": border,

        # Inputs (AdwEntryRow / GtkEntry)
        "input.background": ui["view_bg"] if not is_dark else ui["secondary_sidebar_bg"],
        "input.border": border,
        "input.foreground": ui["window_fg"],
        "input.placeholderForeground": dim_fg,
        "inputOption.activeBackground": ui["view_selected"],
        "inputOption.activeBorder": ui["accent_bg"],
        "inputOption.activeForeground": ui["window_fg"],
        "inputOption.hoverBackground": ui["hover"],
        "inputValidation.errorBackground": ui["error_bg"],
        "inputValidation.errorForeground": "#ffffff",
        "inputValidation.errorBorder": ui["error_color"],
        "inputValidation.infoBackground": ui["accent_bg"],
        "inputValidation.infoForeground": "#ffffff",
        "inputValidation.infoBorder": ui["accent_color"],
        "inputValidation.warningBackground": ui["warning_bg"],
        "inputValidation.warningForeground": "#ffffff" if is_dark else "#241f31",
        "inputValidation.warningBorder": ui["warning_color"],

        # Scrollbar (GtkScrollbar overlay slider)
        "scrollbar.shadow": ui["shade"],
        "scrollbarSlider.background": ui["trough"],
        "scrollbarSlider.hoverBackground": ui["trough_hover"],
        "scrollbarSlider.activeBackground": ui["trough_active"],

        # Badges & ProgressBar (GtkLevelBar / AdwIndicator)
        "badge.foreground": ui["accent_fg"],
        "badge.background": ui["accent_bg"],
        "progressBar.background": ui["accent_bg"],

        # Lists & Trees (GtkListView / AdwNavigationSidebar)
        "list.activeSelectionBackground": ui["selected_active"],
        "list.activeSelectionForeground": ui["window_fg"],
        "list.activeSelectionIconForeground": ui["window_fg"],
        "list.dropBackground": ui["view_selected"],
        "list.focusBackground": ui["selected_hover"],
        "list.focusForeground": ui["window_fg"],
        "list.focusHighlightForeground": ui["accent_color"],
        "list.focusOutline": focus_border,
        "list.highlightForeground": ui["accent_color"],
        "list.hoverBackground": ui["hover"],
        "list.hoverForeground": ui["window_fg"],
        "list.inactiveSelectionBackground": ui["selected"],
        "list.inactiveSelectionForeground": ui["window_fg"],
        "list.inactiveSelectionIconForeground": ui["window_fg"],
        "list.inactiveFocusBackground": ui["selected"],
        "list.invalidItemForeground": ui["error_color"],
        "list.errorForeground": ui["error_color"],
        "list.warningForeground": ui["warning_color"],
        "listFilterWidget.background": ui["popover_bg"],
        "listFilterWidget.outline": ui["accent_bg"],
        "listFilterWidget.noMatchesOutline": ui["error_bg"],
        "tree.indentGuidesStroke": border,
        "tree.tableColumnsBorder": border,

        # Activity Bar (Primary Navigation Rail -> LibAdwaita sidebar_bg_color)
        "activityBar.background": ui["sidebar_bg"],
        "activityBar.foreground": ui["sidebar_fg"],
        "activityBar.inactiveForeground": dim_fg,
        "activityBar.border": border,
        "activityBar.activeBorder": ui["accent_bg"],
        "activityBar.activeBackground": ui["selected"],
        "activityBarBadge.background": ui["accent_bg"],
        "activityBarBadge.foreground": ui["accent_fg"],
        "activityBarTop.foreground": ui["sidebar_fg"],
        "activityBarTop.activeBorder": ui["accent_bg"],
        "activityBarTop.inactiveForeground": dim_fg,
        "activityBarTop.background": ui["sidebar_bg"],

        # Side Bar (Split Pane -> LibAdwaita secondary_sidebar_bg_color)
        "sideBar.background": ui["secondary_sidebar_bg"],
        "sideBar.foreground": ui["secondary_sidebar_fg"],
        "sideBar.border": border,
        "sideBar.dropBackground": ui["view_selected"],
        "sideBarTitle.foreground": ui["secondary_sidebar_fg"],
        "sideBarSectionHeader.background": ui["sidebar_bg"],
        "sideBarSectionHeader.foreground": ui["sidebar_fg"],
        "sideBarSectionHeader.border": border,

        # Minimap
        "minimap.findMatchHighlight": with_alpha(p["yellow_3"], 60),
        "minimap.selectionHighlight": ui["view_selected_hover"],
        "minimap.errorHighlight": ui["error_color"],
        "minimap.warningHighlight": ui["warning_color"],
        "minimap.background": ui["view_bg"],
        "minimapSlider.background": ui["trough"],
        "minimapSlider.hoverBackground": ui["trough_hover"],
        "minimapSlider.activeBackground": ui["trough_active"],

        # Editor Groups & Tabs (AdwTabBar + AdwHeaderBar)
        "editorGroup.border": border,
        "editorGroup.dropBackground": ui["view_selected"],
        "editorGroupHeader.noTabsBackground": ui["headerbar_bg"],
        "editorGroupHeader.tabsBackground": ui["headerbar_bg"],
        "editorGroupHeader.tabsBorder": border,
        "editorGroupHeader.border": border,
        "tab.activeBackground": ui["view_bg"] if is_dark else "#f0f0f2",
        "tab.unfocusedActiveBackground": ui["window_bg"],
        "tab.activeForeground": ui["headerbar_fg"],
        "tab.border": border,
        "tab.activeBorder": ui["accent_bg"] if high_contrast else "#00000000",
        "tab.unfocusedActiveBorder": "#00000000",
        "tab.activeBorderTop": ui["accent_bg"],
        "tab.unfocusedActiveBorderTop": dim_fg,
        "tab.lastPinnedBorder": border,
        "tab.inactiveBackground": ui["headerbar_bg"],
        "tab.unfocusedInactiveBackground": ui["headerbar_backdrop"],
        "tab.inactiveForeground": dim_fg,
        "tab.unfocusedActiveForeground": dim_fg,
        "tab.unfocusedInactiveForeground": ui["disabled_fg"],
        "tab.hoverBackground": ui["hover"],
        "tab.unfocusedHoverBackground": ui["view_hover"],
        "tab.hoverForeground": ui["headerbar_fg"],

        # Editor Primary View (GtkSourceView Adwaita / Adwaita-dark)
        "editor.background": ui["view_bg"],
        "editor.foreground": syntax["text"],
        "editorLineNumber.foreground": line_num_fg,
        "editorLineNumber.activeForeground": line_num_active_fg,
        "editorCursor.background": ui["view_bg"],
        "editorCursor.foreground": syntax["text"],
        "editor.selectionBackground": ui["view_selected"],
        "editor.inactiveSelectionBackground": with_alpha(ui["accent_bg"], 14),
        "editor.selectionHighlightBackground": with_alpha(ui["accent_bg"], 16),
        "editor.selectionHighlightBorder": border if high_contrast else "#00000000",
        "editor.wordHighlightBackground": with_alpha(p["blue_2"] if is_dark else p["blue_3"], 18),
        "editor.wordHighlightStrongBackground": with_alpha(p["blue_2"] if is_dark else p["blue_3"], 28),
        "editor.wordHighlightTextBackground": with_alpha(p["blue_2"] if is_dark else p["blue_3"], 18),
        # Search match directly from Adwaita-dark.xml (#rgba(246,211,45,.5)) & Adwaita.xml (yellow_2)
        "editor.findMatchBackground": with_alpha(p["yellow_3"], 45) if is_dark else with_alpha(p["yellow_2"], 75),
        "editor.findMatchHighlightBackground": with_alpha(p["yellow_3"], 25) if is_dark else with_alpha(p["yellow_2"], 45),
        "editor.findRangeHighlightBackground": with_alpha(ui["accent_bg"], 12),
        "editor.findMatchBorder": p["yellow_4"] if high_contrast else "#00000000",
        "editor.hoverHighlightBackground": ui["view_hover"],
        "editor.lineHighlightBackground": ui["view_bg_alt"],
        "editor.lineHighlightBorder": "#00000000",
        "editorUnicodeHighlight.border": ui["warning_color"],
        "editorLink.activeForeground": ui["accent_color"],
        "editor.rangeHighlightBackground": ui["view_hover"],
        "editorWhitespace.foreground": "#505050" if is_dark else "#b0afac",  # draw-spaces in Adwaita*.xml
        "editorIndentGuide.background1": border,
        "editorIndentGuide.activeBackground1": dim_fg,
        "editorInlayHint.background": ui["selected"],
        "editorInlayHint.foreground": dim_fg,
        "editorInlayHint.typeBackground": ui["selected"],
        "editorInlayHint.typeForeground": syntax["type"],
        "editorInlayHint.parameterBackground": ui["selected"],
        "editorInlayHint.parameterForeground": syntax["parameter"],
        "editorRuler.foreground": border,
        "editorCodeLens.foreground": dim_fg,
        "editorBracketMatch.background": with_alpha(ui["accent_bg"], 20),
        "editorBracketMatch.border": ui["accent_color"],

        # Bracket Pair Colorization (GNOME HIG scales)
        "editorBracketHighlight.foreground1": p["blue_2"] if is_dark else p["blue_4"],
        "editorBracketHighlight.foreground2": p["orange_2"] if is_dark else p["orange_5"],
        "editorBracketHighlight.foreground3": p["teal_2"] if is_dark else p["teal_5"],
        "editorBracketHighlight.foreground4": p["purple_2"] if is_dark else p["purple_4"],
        "editorBracketHighlight.foreground5": p["green_3"] if is_dark else p["green_5"],
        "editorBracketHighlight.foreground6": p["yellow_3"] if is_dark else p["yellow_6"],
        "editorBracketHighlight.unexpectedBracket.foreground": ui["error_color"],

        # Folding & Overview Ruler
        "editor.foldBackground": with_alpha(ui["accent_bg"], 10),
        "editorOverviewRuler.background": ui["view_bg"],
        "editorOverviewRuler.border": border,
        "editorOverviewRuler.findMatchForeground": with_alpha(p["yellow_3"], 70),
        "editorOverviewRuler.rangeHighlightForeground": with_alpha(ui["accent_bg"], 50),
        "editorOverviewRuler.selectionHighlightForeground": with_alpha(ui["accent_bg"], 60),
        "editorOverviewRuler.wordHighlightForeground": with_alpha(ui["accent_bg"], 50),
        "editorOverviewRuler.wordHighlightStrongForeground": with_alpha(ui["accent_bg"], 80),
        "editorOverviewRuler.modifiedForeground": p["orange_3"] if is_dark else p["orange_4"],
        "editorOverviewRuler.addedForeground": p["teal_3"] if is_dark else p["teal_4"],
        "editorOverviewRuler.deletedForeground": p["red_1"] if is_dark else p["red_2"],
        "editorOverviewRuler.errorForeground": ui["error_color"],
        "editorOverviewRuler.warningForeground": ui["warning_color"],
        "editorOverviewRuler.infoForeground": ui["accent_color"],

        # Errors, Warnings, Gutter
        "editorError.foreground": ui["error_color"],
        "editorWarning.foreground": ui["warning_color"],
        "editorInfo.foreground": ui["accent_color"],
        "editorHint.foreground": p["teal_2"] if is_dark else p["teal_5"],
        "problemsErrorIcon.foreground": ui["error_color"],
        "problemsWarningIcon.foreground": ui["warning_color"],
        "problemsInfoIcon.foreground": ui["accent_color"],
        "editorGutter.background": ui["view_bg"],
        "editorGutter.modifiedBackground": p["orange_3"] if is_dark else p["orange_4"],
        "editorGutter.addedBackground": p["teal_3"] if is_dark else p["teal_4"],
        "editorGutter.deletedBackground": p["red_1"] if is_dark else p["red_2"],
        "editorGutter.commentRangeForeground": dim_fg,
        "editorGutter.foldingControlForeground": dim_fg,

        # Diff Editor (mapped to Adwaita*.xml diff:* styles)
        "diffEditor.insertedTextBackground": with_alpha(p["teal_3"] if is_dark else p["teal_4"], 18),
        "diffEditor.removedTextBackground": with_alpha(p["red_1"] if is_dark else p["red_2"], 18),
        "diffEditor.insertedLineBackground": with_alpha(p["teal_3"] if is_dark else p["teal_4"], 12),
        "diffEditor.removedLineBackground": with_alpha(p["red_1"] if is_dark else p["red_2"], 12),
        "diffEditor.diagonalFill": border,
        "diffEditor.border": border,

        # Editor Widgets, Suggest, Hover Popovers (AdwPopover / GtkPopover)
        "editorWidget.foreground": ui["window_fg"],
        "editorWidget.background": ui["popover_bg"],
        "editorWidget.border": border,
        "editorWidget.resizeBorder": ui["accent_bg"],
        "editorSuggestWidget.background": ui["popover_bg"],
        "editorSuggestWidget.border": border,
        "editorSuggestWidget.foreground": syntax["text"],
        "editorSuggestWidget.focusHighlightForeground": ui["accent_color"],
        "editorSuggestWidget.highlightForeground": ui["accent_color"],
        "editorSuggestWidget.selectedBackground": ui["selected_active"],
        "editorSuggestWidget.selectedForeground": ui["window_fg"],
        "editorHoverWidget.foreground": ui["window_fg"],
        "editorHoverWidget.background": ui["popover_bg"],
        "editorHoverWidget.border": border,
        "editorHoverWidget.statusBarBackground": ui["secondary_sidebar_bg"],
        "editorGhostText.foreground": dim_fg,
        "editorStickyScroll.background": ui["view_bg"],
        "editorStickyScrollHover.background": ui["view_bg_alt"],
        "editorStickyScroll.border": border,
        "editorStickyScroll.shadow": ui["shade"],

        # Peek View
        "peekView.border": ui["accent_bg"],
        "peekViewEditor.background": ui["window_bg"],
        "peekViewEditorGutter.background": ui["window_bg"],
        "peekViewEditor.matchHighlightBackground": with_alpha(p["yellow_3"], 35),
        "peekViewResult.background": ui["secondary_sidebar_bg"],
        "peekViewResult.fileForeground": ui["window_fg"],
        "peekViewResult.lineForeground": dim_fg,
        "peekViewResult.matchHighlightBackground": with_alpha(p["yellow_3"], 35),
        "peekViewResult.selectionBackground": ui["view_selected"],
        "peekViewResult.selectionForeground": ui["window_fg"],
        "peekViewTitle.background": ui["headerbar_bg"],
        "peekViewTitleDescription.foreground": dim_fg,
        "peekViewTitleLabel.foreground": ui["headerbar_fg"],

        # Merge Conflicts
        "merge.currentHeaderBackground": with_alpha(p["teal_3"], 40),
        "merge.currentContentBackground": with_alpha(p["teal_3"], 18),
        "merge.incomingHeaderBackground": with_alpha(p["blue_3"], 40),
        "merge.incomingContentBackground": with_alpha(p["blue_3"], 18),
        "merge.border": border,
        "editorOverviewRuler.currentContentForeground": p["teal_3"],
        "editorOverviewRuler.incomingContentForeground": p["blue_3"],

        # Panel (Bottom Terminal / Output / Problems -> LibAdwaita window_bg_color)
        "panel.background": ui["window_bg"],
        "panel.border": border,
        "panel.dropBorder": ui["accent_bg"],
        "panelTitle.activeBorder": ui["accent_bg"],
        "panelTitle.activeForeground": ui["window_fg"],
        "panelTitle.inactiveForeground": dim_fg,
        "panelInput.border": border,
        "panelSection.border": border,
        "panelSection.dropBackground": ui["view_selected"],
        "panelSectionHeader.background": ui["secondary_sidebar_bg"],
        "panelSectionHeader.foreground": ui["window_fg"],
        "panelSectionHeader.border": border,

        # Status Bar (Clean subtle bottom bar matching GNOME Builder / Text Editor)
        "statusBar.background": ui["headerbar_bg"],
        "statusBar.foreground": ui["headerbar_fg"],
        "statusBar.border": border,
        "statusBar.debuggingBackground": p["orange_4"] if is_dark else p["orange_3"],
        "statusBar.debuggingForeground": "#ffffff",
        "statusBar.debuggingBorder": border,
        "statusBar.noFolderForeground": ui["headerbar_fg"],
        "statusBar.noFolderBackground": ui["headerbar_bg"],
        "statusBar.noFolderBorder": border,
        "statusBarItem.activeBackground": ui["active"],
        "statusBarItem.hoverBackground": ui["hover"],
        "statusBarItem.hoverForeground": ui["headerbar_fg"],
        "statusBarItem.prominentForeground": ui["headerbar_fg"],
        "statusBarItem.prominentBackground": ui["selected"],
        "statusBarItem.prominentHoverBackground": ui["selected_hover"],
        "statusBarItem.remoteBackground": ui["accent_bg"],
        "statusBarItem.remoteForeground": ui["accent_fg"],
        "statusBarItem.errorBackground": ui["error_bg"],
        "statusBarItem.errorForeground": "#ffffff",
        "statusBarItem.warningBackground": ui["warning_bg"],
        "statusBarItem.warningForeground": "#ffffff" if is_dark else "#241f31",

        # Title Bar (AdwHeaderBar active & backdrop states)
        "titleBar.activeBackground": ui["headerbar_bg"],
        "titleBar.activeForeground": ui["headerbar_fg"],
        "titleBar.inactiveBackground": ui["headerbar_backdrop"],
        "titleBar.inactiveForeground": dim_fg,
        "titleBar.border": border,

        # Menus & Command Center (GtkPopoverMenu & HeaderBar Search/OmniBar)
        "menubar.selectionForeground": ui["headerbar_fg"],
        "menubar.selectionBackground": ui["hover"],
        "menu.foreground": ui["window_fg"],
        "menu.background": ui["popover_bg"],
        "menu.selectionForeground": ui["window_fg"],
        "menu.selectionBackground": ui["selected_hover"],
        "menu.separatorBackground": border,
        "menu.border": border,
        "commandCenter.foreground": ui["headerbar_fg"],
        "commandCenter.activeForeground": ui["headerbar_fg"],
        "commandCenter.background": ui["selected"],
        "commandCenter.activeBackground": ui["selected_hover"],
        "commandCenter.border": border,
        "commandCenter.inactiveForeground": dim_fg,
        "commandCenter.inactiveBorder": border,
        "commandCenter.activeBorder": focus_border,

        # Notifications & Toasts (AdwToast / AdwDialog)
        "notificationCenter.border": border,
        "notificationCenterHeader.foreground": ui["window_fg"],
        "notificationCenterHeader.background": ui["secondary_sidebar_bg"],
        "notificationToast.border": border,
        "notifications.foreground": ui["window_fg"],
        "notifications.background": ui["popover_bg"],
        "notifications.border": border,
        "notificationLink.foreground": ui["accent_color"],
        "notificationsErrorIcon.foreground": ui["error_color"],
        "notificationsWarningIcon.foreground": ui["warning_color"],
        "notificationsInfoIcon.foreground": ui["accent_color"],

        # Quick Input / Command Palette (AdwDialog / Quick Open)
        "pickerGroup.border": border,
        "pickerGroup.foreground": ui["accent_color"],
        "quickInput.background": ui["dialog_bg"],
        "quickInput.foreground": ui["window_fg"],
        "quickInputTitle.background": ui["headerbar_bg"],
        "quickInputList.focusBackground": ui["selected_active"],
        "quickInputList.focusForeground": ui["window_fg"],
        "quickInputList.focusIconForeground": ui["window_fg"],
        "keybindingLabel.background": ui["selected"],
        "keybindingLabel.foreground": ui["window_fg"],
        "keybindingLabel.border": border,
        "keybindingLabel.bottomBorder": border,

        # Integrated Terminal (GNOME Console / Ptyxis palette)
        "terminal.background": term["background"],
        "terminal.foreground": term["foreground"],
        "terminalCursor.foreground": term["cursor"],
        "terminalCursor.background": term["background"],
        "terminal.selectionBackground": term["selection"],
        "terminal.border": border,
        "terminal.ansiBlack": term["ansiBlack"],
        "terminal.ansiRed": term["ansiRed"],
        "terminal.ansiGreen": term["ansiGreen"],
        "terminal.ansiYellow": term["ansiYellow"],
        "terminal.ansiBlue": term["ansiBlue"],
        "terminal.ansiMagenta": term["ansiMagenta"],
        "terminal.ansiCyan": term["ansiCyan"],
        "terminal.ansiWhite": term["ansiWhite"],
        "terminal.ansiBrightBlack": term["ansiBrightBlack"],
        "terminal.ansiBrightRed": term["ansiBrightRed"],
        "terminal.ansiBrightGreen": term["ansiBrightGreen"],
        "terminal.ansiBrightYellow": term["ansiBrightYellow"],
        "terminal.ansiBrightBlue": term["ansiBrightBlue"],
        "terminal.ansiBrightMagenta": term["ansiBrightMagenta"],
        "terminal.ansiBrightCyan": term["ansiBrightCyan"],
        "terminal.ansiBrightWhite": term["ansiBrightWhite"],

        # Debug Toolbar & Views
        "debugToolBar.background": ui["popover_bg"],
        "debugToolBar.border": border,
        "editor.stackFrameHighlightBackground": with_alpha(p["yellow_3"], 25),
        "editor.focusedStackFrameHighlightBackground": with_alpha(p["green_3"], 25),
        "debugIcon.breakpointForeground": p["red_2"],
        "debugIcon.breakpointDisabledForeground": dim_fg,
        "debugIcon.startForeground": ui["success_color"],
        "debugIcon.pauseForeground": ui["warning_color"],
        "debugIcon.stopForeground": ui["error_color"],
        "debugIcon.restartForeground": ui["success_color"],
        "debugConsole.infoForeground": ui["accent_color"],
        "debugConsole.warningForeground": ui["warning_color"],
        "debugConsole.errorForeground": ui["error_color"],
        "debugConsole.sourceForeground": dim_fg,

        # Git Decorations (GNOME HIG semantic colors)
        "gitDecoration.addedResourceForeground": p["teal_2"] if is_dark else p["teal_5"],
        "gitDecoration.modifiedResourceForeground": p["orange_2"] if is_dark else p["orange_4"],
        "gitDecoration.deletedResourceForeground": p["red_1"] if is_dark else p["red_3"],
        "gitDecoration.renamedResourceForeground": p["blue_2"] if is_dark else p["blue_4"],
        "gitDecoration.stageModifiedResourceForeground": p["orange_1"] if is_dark else p["orange_5"],
        "gitDecoration.stageDeletedResourceForeground": p["red_2"] if is_dark else p["red_4"],
        "gitDecoration.untrackedResourceForeground": p["green_3"] if is_dark else p["green_5"],
        "gitDecoration.ignoredResourceForeground": dim_fg,
        "gitDecoration.conflictingResourceForeground": p["purple_2"] if is_dark else p["purple_4"],
        "gitDecoration.submoduleResourceForeground": p["violet_2"] if is_dark else p["violet_4"],

        # Breadcrumbs & Settings (AdwPreferencesPage / AdwActionRow)
        "breadcrumb.foreground": dim_fg,
        "breadcrumb.background": ui["view_bg"],
        "breadcrumb.focusForeground": ui["window_fg"],
        "breadcrumb.activeSelectionForeground": ui["accent_color"],
        "breadcrumbPicker.background": ui["popover_bg"],
        "settings.headerForeground": ui["window_fg"],
        "settings.modifiedItemIndicator": ui["accent_bg"],
        "settings.dropdownBackground": ui["popover_bg"],
        "settings.dropdownForeground": ui["window_fg"],
        "settings.dropdownBorder": border,
        "settings.checkboxBackground": ui["view_bg"],
        "settings.checkboxForeground": ui["window_fg"],
        "settings.checkboxBorder": border,
        "settings.RowHoverBackground": ui["view_hover"],
        "settings.textInputBackground": ui["view_bg"] if not is_dark else ui["secondary_sidebar_bg"],
        "settings.textInputForeground": ui["window_fg"],
        "settings.textInputBorder": border,
        "settings.numberInputBackground": ui["view_bg"] if not is_dark else ui["secondary_sidebar_bg"],
        "settings.numberInputForeground": ui["window_fg"],
        "settings.numberInputBorder": border,
    }
    return colors


def build_token_colors(syntax: Dict[str, str]) -> List[Dict[str, Any]]:
    """Map GtkSourceView 5 Adwaita / Adwaita-dark styles to TextMate grammar scopes."""
    return [
        {
            "name": "Comments (def:comment)",
            "scope": [
                "comment",
                "punctuation.definition.comment",
            ],
            "settings": {
                "foreground": syntax["comment"],
                "fontStyle": "italic",
            },
        },
        {
            "name": "Doc Comments & Shebangs (def:doc-comment-element, def:shebang)",
            "scope": [
                "comment.block.documentation",
                "comment.documentation",
                "keyword.other.documentation",
                "storage.type.class.jsdoc",
                "punctuation.definition.comment.shebang",
                "comment.line.number-sign.shebang",
            ],
            "settings": {
                "foreground": syntax["doc_comment"],
                "fontStyle": "bold",
            },
        },
        {
            "name": "Keywords & Statements (def:statement)",
            "scope": [
                "keyword",
                "keyword.control",
                "keyword.operator.new",
                "keyword.operator.expression",
                "keyword.operator.logical",
                "keyword.operator.word",
                "storage.modifier",
                "storage.type.function",
                "storage.type.class",
                "storage.type.struct",
                "storage.type.enum",
                "storage.type.interface",
                "storage.type.trait",
                "storage.type.type",
            ],
            "settings": {
                "foreground": syntax["keyword"],
                "fontStyle": "bold",
            },
        },
        {
            "name": "Control Flow & Operator Punctuation",
            "scope": [
                "keyword.operator",
                "punctuation.accessor",
                "punctuation.separator",
                "punctuation.terminator",
            ],
            "settings": {
                "foreground": syntax["text_secondary"],
            },
        },
        {
            "name": "Types, Classes & Storage Classes (def:type, c:storage-class, python:class-name)",
            "scope": [
                "entity.name.type",
                "entity.name.class",
                "entity.name.struct",
                "entity.name.enum",
                "entity.name.trait",
                "entity.name.interface",
                "entity.other.inherited-class",
                "storage.type",
                "storage.type.primitive",
                "storage.type.built-in",
                "storage.type.c",
                "storage.type.cs",
                "storage.type.go",
                "storage.type.rust",
                "support.type",
                "support.class",
            ],
            "settings": {
                "foreground": syntax["type"],
                "fontStyle": "bold",
            },
        },
        {
            "name": "Functions & Methods (def:function, python:builtin-function)",
            "scope": [
                "entity.name.function",
                "meta.function-call",
                "meta.function-call.generic",
                "support.function",
                "keyword.other.special-method",
            ],
            "settings": {
                "foreground": syntax["function"],
            },
        },
        {
            "name": "Strings (def:string)",
            "scope": [
                "string",
                "string.quoted",
                "string.template",
                "punctuation.definition.string",
            ],
            "settings": {
                "foreground": syntax["string"],
            },
        },
        {
            "name": "Numbers, Booleans & Constants (def:number, def:boolean, def:constant)",
            "scope": [
                "constant.numeric",
                "constant.language",
                "constant.character",
                "constant.other",
                "variable.other.constant",
                "support.constant",
                "entity.name.constant",
            ],
            "settings": {
                "foreground": syntax["number_constant"],
            },
        },
        {
            "name": "Special Characters & Escape Sequences (def:special-char, c:signal-name)",
            "scope": [
                "constant.character.escape",
                "constant.other.placeholder",
                "punctuation.section.embedded",
                "keyword.other.unit",
            ],
            "settings": {
                "foreground": syntax["special_char"],
            },
        },
        {
            "name": "Format Specifiers & Regular Expressions (c:printf, go:printf)",
            "scope": [
                "string.regexp",
                "constant.other.color",
                "meta.interpolation",
            ],
            "settings": {
                "foreground": syntax["format_specifier"],
            },
        },
        {
            "name": "Preprocessor, Directives & Macros (def:preprocessor, rust:macro, rust:attribute)",
            "scope": [
                "meta.preprocessor",
                "keyword.control.directive",
                "keyword.control.import",
                "keyword.control.from",
                "keyword.other.import",
                "keyword.other.package",
                "entity.name.function.preprocessor",
            ],
            "settings": {
                "foreground": syntax["preprocessor"],
            },
        },
        {
            "name": "Rust Macros, Attributes & Decorators (rust:macro, rust:attribute)",
            "scope": [
                "entity.name.function.macro",
                "meta.attribute",
                "entity.name.function.decorator",
                "punctuation.definition.decorator",
                "storage.type.annotation",
            ],
            "settings": {
                "foreground": syntax["number_constant"],
            },
        },
        {
            "name": "Rust Lifetimes (rust:lifetime)",
            "scope": [
                "storage.modifier.lifetime.rust",
                "entity.name.type.lifetime.rust",
                "punctuation.definition.lifetime.rust",
            ],
            "settings": {
                "foreground": syntax["keyword"],
            },
        },
        {
            "name": "Variables & Identifiers (def:text / def:identifier)",
            "scope": [
                "variable",
                "variable.other.readwrite",
                "meta.definition.variable",
            ],
            "settings": {
                "foreground": syntax["text"],
            },
        },
        {
            "name": "Function Parameters",
            "scope": [
                "variable.parameter",
                "meta.parameter",
            ],
            "settings": {
                "foreground": syntax["parameter"],
            },
        },
        {
            "name": "Object Properties & Fields (def:identifier)",
            "scope": [
                "variable.other.property",
                "variable.other.object.property",
                "variable.other.member",
                "support.variable.property",
                "meta.object-literal.key",
            ],
            "settings": {
                "foreground": syntax["identifier_property"],
            },
        },
        {
            "name": "Language Variables (self, this, super, cls)",
            "scope": [
                "variable.language",
            ],
            "settings": {
                "foreground": syntax["keyword"],
                "fontStyle": "italic",
            },
        },
        {
            "name": "Namespaces & Modules (xml:namespace)",
            "scope": [
                "entity.name.namespace",
                "entity.name.module",
                "storage.modifier.import",
                "storage.modifier.package",
            ],
            "settings": {
                "foreground": syntax["namespace_warning"],
            },
        },
        {
            "name": "HTML / XML / Blueprint Tags (xml:element-name)",
            "scope": [
                "entity.name.tag",
                "punctuation.definition.tag",
            ],
            "settings": {
                "foreground": syntax["tag_heading"],
            },
        },
        {
            "name": "HTML / XML Attributes (xml:attribute-name)",
            "scope": [
                "entity.other.attribute-name",
            ],
            "settings": {
                "foreground": syntax["preprocessor"],
            },
        },
        {
            "name": "CSS Selectors & IDs (css:id-selector, css:type-selector)",
            "scope": [
                "entity.name.tag.css",
                "entity.other.attribute-name.id.css",
                "entity.other.attribute-name.class.css",
            ],
            "settings": {
                "foreground": syntax["tag_heading"],
                "fontStyle": "bold",
            },
        },
        {
            "name": "CSS Pseudo-Selectors (css:pseudo-selector)",
            "scope": [
                "entity.other.attribute-name.pseudo-class.css",
                "entity.other.attribute-name.pseudo-element.css",
            ],
            "settings": {
                "foreground": syntax["number_constant"],
                "fontStyle": "bold",
            },
        },
        {
            "name": "CSS Properties (css:property-name)",
            "scope": [
                "support.type.property-name.css",
                "support.type.property-name.scss",
                "support.type.property-name.less",
            ],
            "settings": {
                "foreground": syntax["preprocessor"],
            },
        },
        {
            "name": "JSON / YAML / TOML Keys",
            "scope": [
                "support.type.property-name.json",
                "entity.name.tag.yaml",
                "keyword.key.toml",
                "variable.other.key.toml",
            ],
            "settings": {
                "foreground": syntax["function"],
            },
        },
        {
            "name": "Markdown Headings (def:heading)",
            "scope": [
                "markup.heading",
                "entity.name.section.markdown",
                "punctuation.definition.heading.markdown",
            ],
            "settings": {
                "foreground": syntax["tag_heading"],
                "fontStyle": "bold",
            },
        },
        {
            "name": "Markdown Bold (def:strong-emphasis)",
            "scope": [
                "markup.bold",
                "punctuation.definition.bold.markdown",
            ],
            "settings": {
                "fontStyle": "bold",
            },
        },
        {
            "name": "Markdown Italic (def:emphasis)",
            "scope": [
                "markup.italic",
                "punctuation.definition.italic.markdown",
            ],
            "settings": {
                "fontStyle": "italic",
            },
        },
        {
            "name": "Markdown Inline Code & Preformatted (def:inline-code, def:preformatted-section)",
            "scope": [
                "markup.inline.raw",
                "markup.fenced_code.block",
                "markup.raw.block",
            ],
            "settings": {
                "foreground": syntax["number_constant"],
            },
        },
        {
            "name": "Markdown Links (def:link-text, def:link-destination)",
            "scope": [
                "string.other.link.title.markdown",
                "string.other.link.description.markdown",
            ],
            "settings": {
                "foreground": syntax["link_text"],
            },
        },
        {
            "name": "Markdown Link URLs (def:link-destination)",
            "scope": [
                "markup.underline.link",
            ],
            "settings": {
                "foreground": syntax["function"],
                "fontStyle": "italic underline",
            },
        },
        {
            "name": "Markdown Lists & Quotes (def:list-marker)",
            "scope": [
                "punctuation.definition.list.begin.markdown",
                "markup.list.numbered.bullet",
                "markup.quote",
            ],
            "settings": {
                "foreground": syntax["preprocessor"],
                "fontStyle": "bold",
            },
        },
        {
            "name": "Diffs (diff:added-line, diff:changed-line, diff:removed-line, diff:location)",
            "scope": ["markup.inserted", "meta.diff.header.to-file"],
            "settings": {"foreground": syntax["tag_heading"]},
        },
        {
            "name": "Diff Changed",
            "scope": ["markup.changed"],
            "settings": {"foreground": syntax["preprocessor"]},
        },
        {
            "name": "Diff Deleted",
            "scope": ["markup.deleted", "meta.diff.header.from-file"],
            "settings": {"foreground": syntax["special_char"]},
        },
        {
            "name": "Diff Range / Location",
            "scope": ["meta.diff.range", "meta.diff.header"],
            "settings": {"foreground": syntax["namespace_warning"]},
        },
        {
            "name": "Invalid / Error (def:error)",
            "scope": ["invalid", "invalid.illegal"],
            "settings": {"foreground": syntax["error"]},
        },
    ]


def build_semantic_tokens(syntax: Dict[str, str]) -> Dict[str, Any]:
    """Map VS Code LSP semantic tokens to GtkSourceView 5 Adwaita styles."""
    return {
        "namespace": syntax["namespace_warning"],
        "class": {"foreground": syntax["type"], "bold": True},
        "struct": {"foreground": syntax["type"], "bold": True},
        "enum": {"foreground": syntax["type"], "bold": True},
        "interface": {"foreground": syntax["type"], "bold": True},
        "type": {"foreground": syntax["type"], "bold": True},
        "typeParameter": {"foreground": syntax["type"], "italic": True},
        "function": syntax["function"],
        "method": syntax["function"],
        "macro": syntax["number_constant"],
        "decorator": syntax["number_constant"],
        "variable": syntax["text"],
        "variable.readonly": syntax["number_constant"],
        "variable.defaultLibrary": {"foreground": syntax["keyword"], "italic": True},
        "parameter": syntax["parameter"],
        "property": syntax["identifier_property"],
        "enumMember": syntax["number_constant"],
        "keyword": {"foreground": syntax["keyword"], "bold": True},
        "modifier": {"foreground": syntax["keyword"], "bold": True},
        "comment": {"foreground": syntax["comment"], "italic": True},
        "string": syntax["string"],
        "number": syntax["number_constant"],
        "regexp": syntax["format_specifier"],
        "operator": syntax["text_secondary"],
        "lifetime": {"foreground": syntax["keyword"], "bold": False},
    }


def generate_all_themes(out_dir: Path) -> None:
    """Write all 4 LibAdwaita theme JSON files into `themes/`."""
    out_dir.mkdir(parents=True, exist_ok=True)

    variants = [
        {
            "filename": "libadwaita-dark-color-theme.json",
            "name": "LibAdwaita Dark",
            "type": "dark",
            "ui": LIBADWAITA_DARK_UI,
            "syntax": SYNTAX_DARK,
            "term": TERMINAL_DARK,
            "is_dark": True,
            "hc": False,
        },
        {
            "filename": "libadwaita-light-color-theme.json",
            "name": "LibAdwaita Light",
            "type": "light",
            "ui": LIBADWAITA_LIGHT_UI,
            "syntax": SYNTAX_LIGHT,
            "term": TERMINAL_LIGHT,
            "is_dark": False,
            "hc": False,
        },
        {
            "filename": "libadwaita-dark-hc-color-theme.json",
            "name": "LibAdwaita Dark (High Contrast)",
            "type": "hcDark",
            "ui": LIBADWAITA_DARK_UI,
            "syntax": SYNTAX_DARK,
            "term": TERMINAL_DARK,
            "is_dark": True,
            "hc": True,
        },
        {
            "filename": "libadwaita-light-hc-color-theme.json",
            "name": "LibAdwaita Light (High Contrast)",
            "type": "hcLight",
            "ui": LIBADWAITA_LIGHT_UI,
            "syntax": SYNTAX_LIGHT,
            "term": TERMINAL_LIGHT,
            "is_dark": False,
            "hc": True,
        },
    ]

    for v in variants:
        theme_doc = {
            "$schema": "vscode://schemas/color-theme",
            "name": v["name"],
            "type": v["type"],
            "semanticHighlighting": True,
            "colors": build_workbench_colors(
                v["ui"], v["syntax"], v["term"], v["is_dark"], v["hc"]
            ),
            "semanticTokenColors": build_semantic_tokens(v["syntax"]),
            "tokenColors": build_token_colors(v["syntax"]),
        }
        target_path = out_dir / v["filename"]
        target_path.write_text(
            json.dumps(theme_doc, indent=2) + "\n", encoding="utf-8"
        )
        print(
            f"Generated {target_path.name} "
            f"({len(theme_doc['colors'])} UI colors, "
            f"{len(theme_doc['tokenColors'])} TextMate rules, "
            f"{len(theme_doc['semanticTokenColors'])} semantic rules)"
        )


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    generate_all_themes(repo_root / "themes")
