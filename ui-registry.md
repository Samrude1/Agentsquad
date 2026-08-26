# UI Registry & Design Baseline

## Baseline — Established 2026-08-24
*Established via `/imprint audit` for Agent Squad portfolio platform.*

### Design Tokens & Properties

| Property | Standard Value / Class | Description |
| :--- | :--- | :--- |
| **Card Background** | `var(--bg-card, #ffffff)` | Pure white container background |
| **Card Border** | `1px solid var(--border-color, #e5e7eb)` | Subtle grey border |
| **Card Radius** | `12px` | Modern, consistent container rounding |
| **Input Background** | `#ffffff` | Clean white input background |
| **Input Border** | `1px solid var(--border-input, #d1d5db)` | Input border with `#111827` focus ring |
| **Input Radius** | `6px` | Input element border radius |
| **Button Primary** | `background: #111827`, `color: #ffffff`, `radius: 6px` | High-contrast black call-to-action |
| **Button Secondary / Action** | `radius: 6px`, specific role colors (`#16a34a`, `#2563eb`) | Functional action buttons |
| **Preset Chip** | `background: #f3f4f6`, `border: 1px solid #e5e7eb`, `radius: 9999px` | 1-Click interactive demo buttons |
| **Agent Header** | `.agent-header` (Icon + Title + Subtitle) | Unified header across all agent tabs |
| **Text Primary** | `#111827` | Headings and high-emphasis body text |
| **Text Secondary** | `#4b5563` | Form labels and secondary copy |
| **Text Muted** | `#6b7280` | Subtitles, helper text and hints |

---

### Component Registry

### AgentHeader
File: `frontend/src/components/*.jsx`
Pattern:
- Container: `.agent-header` (flex, gap 1rem, margin-bottom 1.5rem)
- Icon badge: `.agent-icon` (background `#f3f4f6`, border `#e5e7eb`, radius `10px`, size `48x48px`)
- Title: `.agent-title` (`#111827`, `1.25rem`, bold)
- Subtitle: `.agent-subtitle` (`#6b7280`, `0.9rem`)

### PresetChips
File: `frontend/src/components/*.jsx`
Pattern:
- Container: `.presets-container` (flex wrap, gap 0.5rem, margin 0.5rem 0 1.25rem)
- Chip: `.preset-chip` (`bg #f3f4f6`, `hover: bg #e5e7eb`, `font-size 0.8rem`, `padding 0.35rem 0.75rem`)

### ResultsView
File: `frontend/src/components/ResultsView.jsx`
Pattern:
- Container: `.results-container` (`bg white`, `border-radius 12px`, `padding 3rem 2.5rem`, `border 1px solid #e5e7eb`)
- Header: `.results-header` with status badge, copy button, and markdown download
