// Showcase file for testing LibAdwaita / GNOME Theme syntax & semantic tokens
// Mirrors GtkSourceView 5 (Adwaita.xml & Adwaita-dark.xml) style mappings.

import std::collections::HashMap;
use std::fmt::{self, Display};

/// Configuration representing a modern LibAdwaita 1.6+ application window.
#[derive(Debug, Clone)]
pub struct AdwApplicationWindow<'a> {
    pub title: &'a str,
    pub default_width: u32,
    pub default_height: u32,
    pub dark_mode: bool,
    pub accent_color: AccentColor,
}

#[derive(Debug, Copy, Clone, PartialEq, Eq)]
pub enum AccentColor {
    Blue = 0x3584E4,
    Teal = 0x2190A4,
    Green = 0x3A944A,
    Yellow = 0xC88800,
    Orange = 0xED5B00,
    Red = 0xE62D42,
    Pink = 0xD56199,
    Purple = 0x9141AC,
    Slate = 0x6F8396,
}

pub const DEFAULT_BORDER_OPACITY: f32 = 0.15;
pub const HIGH_CONTRAST_BORDER_OPACITY: f32 = 0.50;

impl<'a> AdwApplicationWindow<'a> {
    /// Creates a new `AdwApplicationWindow` with GNOME HIG defaults.
    pub fn new(title: &'a str, dark_mode: bool) -> Self {
        Self {
            title,
            default_width: 1024,
            default_height: 768,
            dark_mode,
            accent_color: AccentColor::Blue,
        }
    }

    pub fn css_variables(&self) -> HashMap<&'static str, &'static str> {
        let mut vars = HashMap::new();
        if self.dark_mode {
            vars.insert("--window-bg-color", "#222226");
            vars.insert("--view-bg-color", "#1d1d20");
            vars.insert("--headerbar-bg-color", "#2e2e32");
            vars.insert("--secondary-sidebar-bg-color", "#28282c");
        } else {
            vars.insert("--window-bg-color", "#fafafb");
            vars.insert("--view-bg-color", "#ffffff");
            vars.insert("--headerbar-bg-color", "#ffffff");
            vars.insert("--sidebar-bg-color", "#ebebed");
        }
        vars
    }
}

impl<'a> Display for AdwApplicationWindow<'a> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "AdwApplicationWindow(title=\"{}\", size={}x{}, dark={})\n",
            self.title, self.default_width, self.default_height, self.dark_mode
        )
    }
}
