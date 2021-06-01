import cairo

WIDTH = 9
HEIGHT = 9
PIXEL_SCALE = 80

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH * PIXEL_SCALE, HEIGHT * PIXEL_SCALE)

c = cairo.Context(surface)
c.scale(PIXEL_SCALE, PIXEL_SCALE)

c.rectangle(0, 0, WIDTH, HEIGHT)
c.set_source_rgb(1, 0, 0)
c.fill()

c.rectangle(3, 0, WIDTH, HEIGHT)
c.set_source_rgb(1, 1, 1)
c.fill()

c.rectangle(6, 0, WIDTH, HEIGHT)
c.set_source_rgb(0, 0, 1)
c.fill()

surface.write_to_png('bandeira_da_franca.png')
