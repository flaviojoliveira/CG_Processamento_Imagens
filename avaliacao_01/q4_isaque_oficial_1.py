import cairo
#Implemente novos valores (linhas 3 a 12)
with cairo.SVGSurface("example.svg", 400, 400) as surface:
  c = cairo.Context(surface)
  c.scale(400,400)
  c.set_line_width(0.10)
  c.move_to(2, 2)
  c.line_to(0.10, 0.10)
  c.move_to(3, 2)
  c.line_to(-0.10, -0.10)

  c.set_source_rgb
  c.stroke()