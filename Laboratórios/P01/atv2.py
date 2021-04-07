import cairo

with cairo.SVGSurface("example.svg", 200,200) as surface:
  c=cairo.Context(surface)
  c.scale(200,200)
  c.set_line_width(0.05)
  c.move_to(1,1)
  c.line_to(0.5,0,5)
  c.move_to(2,1)
  c.line_to(-0.5,0,5)

  c.set_source_rgb(0,0,1)
  c.stroke()  