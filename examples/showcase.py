#!/usr/bin/env python3
"""GNOME LibAdwaita & GtkSourceView 5 Syntax Highlighting Showcase."""

from dataclasses import dataclass
from typing import Dict, Optional
import re

ACCENT_HEX_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$")


@dataclass(frozen=True)
class StyleScheme:
    """Represents a GtkSourceView 5 style scheme."""

    scheme_id: str
    name: str
    is_dark: bool = True
    accent: str = "#3584e4"

    def validate(self) -> bool:
        if not ACCENT_HEX_PATTERN.match(self.accent):
            raise ValueError(f"Invalid hex color: {self.accent!r}")
        return True

    def describe(self, extra_note: Optional[str] = None) -> Dict[str, str]:
        mode = "dark" if self.is_dark else "light"
        summary = f"[{self.scheme_id}] {self.name} ({mode})\n"
        return {
            "summary": summary.strip(),
            "accent": self.accent,
            "note": extra_note or "GNOME HIG compliant",
        }


if __name__ == "__main__":
    scheme = StyleScheme("Adwaita-dark", "Adwaita Dark", is_dark=True)
    if scheme.validate():
        print(scheme.describe())
