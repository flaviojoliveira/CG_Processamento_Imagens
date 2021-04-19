import cairo

WIDTH = 4
HEIGHT = 2 
PIXEL_SCALE = 80

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH*PIXEL_SCALE, HEIGHT*PIXEL_SCALE)

c = cairo.Context(surface)
c.scale(PIXEL_SCALE, PIXEL_SCALE)

c.rectangle(0,0,WIDTH, HEIGHT)

c.set_source_rgb(0.45, 0.123, 0.51)
c.fill()

c.move_to(1,1)
c.line_to(0.5,0.5)

c.move_to(2, 1)
c.line_to(0.5, 0.5)
c.set_source_rgb(0,1,0)
c.set_line_width(0.1)
c.stroke()

surface.write_to_png('line.png')
