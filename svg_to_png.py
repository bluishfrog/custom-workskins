import cairosvg

# Paste your SVG here
SVG = r'''
<svg xmlns="http://www.w3.org/2000/svg" height="18" viewBox="0 0 18 18" width="18" focusable="false" aria-hidden="true" style="pointer-events: none; display: inherit; width: 100%; height: 100%;"><path d="M8.041 1.635a2.447 2.447 0 011.763 3.047l-.53 1.858a.75.75 0 00.72.956h3.968c.636 0 1.217.36 1.502.928l.135.269a1.34 1.34 0 01-.45 1.709.336.336 0 00-.149.278v.052c0 .094.03.186.087.26a1.78 1.78 0 01-.309 2.459l-.374.298a.284.284 0 00-.091.312l.051.155c.163.49.076 1.03-.234 1.443a2.1 2.1 0 01-1.68.84l-2.935-.002a9 9 0 01-4.464-1.188l-.205-.117a1.5 1.5 0 00-.744-.197H2.25a.75.75 0 01-.75-.75V9.747a.75.75 0 01.751-.75L4.341 9a.75.75 0 00.71-.501l2.265-6.472a.612.612 0 01.725-.392Z"></path></svg>
'''

# Convert SVG → PNG with transparent background
cairosvg.svg2png(
    bytestring=SVG.encode("utf-8"),
    write_to="youtube_icon_like_filled.png",
    output_width=512,
    output_height=512
)

print("Saved as output.png")