"""Use the repository README as the documentation homepage."""

import re
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files

MATHJAX_TYPESET = """\
if (window.MathJax && window.MathJax.Hub) {
  window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
}
"""


def on_files(files: Files, config: MkDocsConfig) -> Files:
    """Add the README homepage and the MathJax typeset script."""
    readme = Path(config.config_file_path).with_name("README.md")
    content = re.sub(
        r"\(\./src/recommendationsystems/(\w+)\)",
        r"(./\1/\1.ipynb)",
        readme.read_text(encoding="utf-8"),
    )
    files.append(File.generated(config, "index.md", content=content))
    files.append(
        File.generated(config, "js/mathjax-typeset.js", content=MATHJAX_TYPESET)
    )
    return files
