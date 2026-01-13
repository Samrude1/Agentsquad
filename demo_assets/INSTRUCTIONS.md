# 🎬 How to Record a Perfect Demo GIF

Since we are prioritizing the visual impact of your README, follow these steps to create a professional demo asset.

## 🛠 Tools Needed
- **Windows**: [ScreenToGif](https://www.screentogif.com/) (Free, Open Source, Highly Recommended)
- **Mac**: Kap or builtin Screen Record
- **General**: OBS Studio

## 📋 Scene Setup
1.  **Clean Your Desktop**: Close unnecessary tabs.
2.  **Open the App**: Go to `http://localhost:5173`.
3.  **Zoom In**: Press `Ctrl +` a few times so the text is large and readable.
4.  **Resize Window**: Make the browser window roughly **1200x800**. This aspect ratio looks great on GitHub.

## 🎥 Scenario 1: The Sales Agent Run (Short & Sweet) - `demo_sales.gif`
1.  Click "Sales Agent" tab.
2.  Type a Prospect Name (e.g., "TechCorp CEO").
3.  Type a Sender Name (e.g., "Agent Smith").
4.  **Start Recording**.
5.  Click "Generate Email".
6.  Wait for the result.
7.  Scroll down slowly to show the generated email.
8.  **Stop Recording**.

## 🎥 Scenario 2: The Research Agent Run (Visual) - `demo_research.gif`
1.  Click "Research Agent" tab.
2.  Type a Topic (e.g., "Future of AI Agents 2025").
3.  **Start Recording**.
4.  Click "Start Research".
5.  Capture the loading state (it shows activity).
6.  When the result appears (Markdown report), scroll slowly through it.
7.  Highlight a bold section or list with your mouse to show interactivity.
8.  **Stop Recording**.

## ✂️ Editing (In ScreenToGif)
- **Trim**: Cut out the "dead air" while waiting for the AI to think. Speed up the loading part by 2x or 4x.
- **Crop**: Crop the video to *just* your app interface (remove the browser URL bar and Windows taskbar).
- **Save**: Save as `.gif` or `.webp` inside the `demo_assets/` folder.

## 📤 Publishing
Once you have the files in `demo_assets/`:
1.  `git add demo_assets/`
2.  `git commit -m "Add demo assets"`
3.  `git push`
4.  I will then help you link them in the README!
