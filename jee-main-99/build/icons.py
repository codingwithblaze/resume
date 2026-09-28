"""Minimal inline SVG icon set (stroke icons, 24x24 grid)."""

_P = {
    "formula": '<path d="M17 5H7l6 7-6 7h10"/>',
    "shortcut": '<path d="M13 2 4 14h7l-1 8 10-13h-7z"/>',
    "important": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
    "trap": '<path d="M12 3 2 21h20z"/><path d="M12 10v5"/><path d="M12 18v.01"/>',
    "pyq": '<path d="M4 20V10"/><path d="M10 20V4"/><path d="M16 20v-7"/><path d="M22 20H2"/>',
    "revision": '<path d="M4 12a8 8 0 0 1 14-5.3L20 9"/><path d="M20 4v5h-5"/><path d="M20 12a8 8 0 0 1-14 5.3L4 15"/><path d="M4 20v-5h5"/>',
    "practice": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
    "mock": '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5"/><path d="M9 2h6"/>',
    "warning": '<path d="M8 2h8l6 6v8l-6 6H8l-6-6V8z"/><path d="M12 7v6"/><path d="M12 16.5v.01"/>',
    "ref": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "data": '<path d="M3 3v18h18"/><path d="M7 16v-4"/><path d="M12 16V8"/><path d="M17 16v-7"/>',
    "fact": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    "strategy": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
    "note": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><path d="M12 8v.01"/>',
    "def": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/>',
    "graph": '<path d="M3 3v18h18"/><path d="m7 15 4-5 3 3 5-6"/>',
    "example": '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 1 4 10.5c-.8.8-1 1.5-1 2.5H9c0-1-.2-1.7-1-2.5A6 6 0 0 1 12 3z"/>',
    "tip": '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 1 4 10.5c-.8.8-1 1.5-1 2.5H9c0-1-.2-1.7-1-2.5A6 6 0 0 1 12 3z"/>',
    "rmap": '<path d="M9 3h6"/><path d="M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><path d="M7.5 15h9"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "verified": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "third": '<path d="M5 20V12"/><path d="M12 20V6"/><path d="M19 20v-9"/>',
    "rec": '<circle cx="12" cy="12" r="8.5"/><path d="m15 9-1.8 4.2L9 15l1.8-4.2z"/>',
}


def _svg(name: str, cls: str) -> str:
    p = _P.get(name, _P["note"])
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>')


def box(name: str) -> str:
    return f'<span class="box-icon">{_svg(name, "ic")}</span>'


def small(name: str) -> str:
    return _svg(name, "ic-s")
