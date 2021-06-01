# 4. Classifique a imagem gerada por este código (Matricial ou Vetorial) e implemente com novos novos valores (linhas 3 a 12)
# R: Vetorial

import cairo

with cairo.SVGSurface("Example.svg", 200,300) as surface:
  c = cairo.Context(surface)
  c.scale(200, 200)
  c.set_line_width(0.05)
  c.move_to(1,1)
  c.line_to(0.5, 0.5)
  c.move_to(2,1)
  c.line_to(-0.5, -0.5)
  c.set_source_rgb(0.9,0.2,0.69)
  c.stroke()