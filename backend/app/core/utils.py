import os
import markdown

def save_markdown_report(content: str, topic: str, output_dir: str = "Reports") -> str:
    """Saves the markdown content to a file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    clean_topic = "".join(x for x in topic if x.isalnum() or x in " -_").strip().replace(" ", "_")
    filename = os.path.join(output_dir, f"tutkimus_{clean_topic[:30]}.md")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Markdown saved: {filename}")
    return filename

def convert_to_html(markdown_content: str, topic: str, output_filename: str) -> str:
    """Converts markdown to a styled HTML file."""
    try:
        html_content = markdown.markdown(markdown_content)
        
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Research: {topic}</title>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.8; font-size: 18px; max-width: 800px; margin: 0 auto; padding: 40px; color: #333; background-color: #fdfdfd; }}
                h1 {{ color: #2c3e50; font-size: 2.5em; margin-bottom: 0.5em; }}
                h2 {{ color: #34495e; font-size: 1.8em; margin-top: 1.5em; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
                h3 {{ color: #455a64; font-size: 1.4em; margin-top: 1.2em; }}
                p {{ margin-bottom: 1.2em; }}
                code {{ background-color: #f4f4f4; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }}
                pre {{ background-color: #f4f4f4; padding: 20px; border-radius: 8px; overflow-x: auto; font-size: 0.9em; }}
                a {{ color: #007bff; text-decoration: none; border-bottom: 1px dotted #007bff; }}
                a:hover {{ text-decoration: none; border-bottom: 2px solid #007bff; }}
                ul, ol {{ margin-bottom: 1.2em; padding-left: 1.5em; }}
                li {{ margin-bottom: 0.5em; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        html_filename = output_filename.replace(".md", ".html")
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"HTML saved: {html_filename}")
        return html_filename
        
    except Exception as e:
        print(f"HTML conversion failed: {e}")
        return ""
