import cairo

with cairo.SVGSurface("img2.svg", 200, 200) as surface:
    c = cairo.Context(surface)
    c.scale(150, 150)
    c.set_line_width(0.02)
    c.move_to(2, 1)
    c.line_to(0.3, 0.3)
    c.move_to(1, 2)
    c.line_to(1, 1)

    c.set_source_rgb(1, 2, 1)
    c.stroke()