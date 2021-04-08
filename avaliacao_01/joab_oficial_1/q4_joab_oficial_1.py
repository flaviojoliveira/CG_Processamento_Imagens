import cairo

with cairo.SVGSurface("exemplo.svg", 300, 300) as surface:
    c = cairo.Context(surface)
    c.scale(300,300)
    c.set_line_width(1)
    c.move_to(1, 1)
    c.line_to(0.5, 0.5)
    c.move_to(2, 2.5)
    c.line_to(-0.5, -0.5)

    c.set_source_rgb(0.03, 0, 1)
    c.stroke()
    