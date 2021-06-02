import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512, 256)
c = cairo.Context(surface)
c.set_source_rgb(0.4,0.4,0.4)
c.paint()
c.set_source_rgb(0.4,0,0.4)
c.set_line_width(6)
c.rectangle(200,50,100,50)
c.stroke()
c.set_source_rgb(0,0,0)
c.arc(100,80,40,0,2*math.pi)
c.fill_preserve()
c.set_line_width(6)
c.set_source_rgba(1,1,1)
c.stroke()

surface.write_to_png('form.png')

//DANIEL_QUEIROZ