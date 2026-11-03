# AKS-sikkerhetsvurdering: translate to English

Goal: every HTML page on the site is in English. Only this page was Norwegian (checked: no Norwegian letters in index.html, Developer-WS.html, MCP-Risk-Map.html).

Steps:
1. Translate CSS comments, `<title>`, body text, and all strings and comments in the script. Set `<html lang="en-GB">` to match the other pages.
2. Rename internal ids that show up in the URL (tab hash, filter keys) to English.
3. Output dates with `en-GB` instead of `nb-NO`.
4. Check that no Norwegian words or letters remain, and run the page in a browser (tabs, filter, diagram, copy buttons, no console errors).

Out of scope: file name (changing it would break any existing link to the page).
