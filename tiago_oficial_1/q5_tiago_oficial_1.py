import cairo
  
with cairo.SVGSurface("q5.svg", 700, 700) as surface:
  
    context = cairo.Context(surface)
  
    context.rectangle(100, 100, 100, 100)
    context.rectangle(300, 100, 100, 100)
  
    context.scale(700, 700)
  
    context.set_line_width(0.04)
  
    context.set_source_rgba(0.4, 1, 0.4, 1)

    context.stroke()
  
  
print("File Saved")