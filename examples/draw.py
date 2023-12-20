import math
import cairo


def draw(drawing, border=0.05, width=256, height=256):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.scale(width, height)

    pat = cairo.SolidPattern(1.0, 1.0, 1.0, 1.0)

    ctx.rectangle(0.0, 0.0, 1.0, 1.0)
    ctx.set_source(pat)
    ctx.fill()

    ctx.set_source_rgb(0.0, 0.0, 0.0)
    ctx.set_line_width(0.01)
    min_x, max_x, min_y, max_y = 255, 0, 255, 0
    for xs, ys in drawing["image"]:
        min_x = min(min_x, min(xs))
        max_x = max(max_x, max(xs))
        min_y = min(min_y, min(ys))
        max_y = max(max_y, max(ys))
    x_offset = (width - (max_x - min_x)) / (2 * width)
    y_offset = (height - (max_y - min_y)) / (2 * height)
    for xs, ys in drawing["image"]:
        for i, (x, y) in enumerate(zip(xs, ys)):
            sx = x_offset + ((x - min_x) / width)
            sy = y_offset + ((y - min_y) / height)
            bx = (border / 2) + sx * (1 - border)
            by = (border / 2) + sy * (1 - border)
            if i == 0:
                ctx.move_to(bx, by)
            else:
                ctx.line_to(bx, by)
                ctx.move_to(bx, by)
        ctx.close_path()
        ctx.stroke()

    surface.write_to_png(f"{drawing['key_id']}.png")
