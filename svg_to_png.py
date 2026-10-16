import cairosvg

# Paste your SVG here
SVG = r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <g fill="#BDBDC2">
    <path d="M3 6.5A2.5 2.5 0 0 1 5.5 4h10A2.5 2.5 0 0 1 18 6.5v11a2.5 2.5 0 0 1-2.5 2.5h-10A2.5 2.5 0 0 1 3 17.5z"/>
    <path d="m18 9 4-2.5v11L18 15z"/>
  </g>
</svg>
'''

# Convert SVG → PNG with transparent background
cairosvg.svg2png(
    bytestring=SVG.encode("utf-8"),
    write_to="youtube_icon_like_filled.png",
    output_width=512,
    output_height=512
)

print("Saved as output.png")