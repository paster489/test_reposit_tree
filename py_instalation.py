#!/usr/bin/env python3
import markdown
md = markdown.Markdown(extensions=['pymdownx.critic'])
print(md)
md = markdown.Markdown(extensions=['pymdownx.betterem'])
print(md)
md = markdown.Markdown(extensions=['pymdownx.caret'])
print(md)
md = markdown.Markdown(extensions=['pymdownx.mark'])
print(md)
md = markdown.Markdown(extensions=['pymdownx.tilde'])
print(md)
md = markdown.Markdown(extensions=['pymdownx.smartsymbols'])
print(md)
