# Generate random bright color
  - convert hsv color space to RGB color space


        import colorsys
        import random

        def random_colors(N, bright=True):
            """
            N : the number of colors
            Generate random bright colors.
            To get visually distinct colors, generate them in HSV space then
            convert to RGB.
            """
            brightness = 1.0 if bright else 0.7
            #non-normmalized RGB tuple
            colors = [tuple(round(j * 255) for j in colorsys.hsv_to_rgb(i / N, 1, brightness)) for i in range(N)]
            random.shuffle(colors)

            return colors
            
            
         test:
         input: N = 8
         output: [(128, 255, 0), (255, 191, 0), (0, 255, 64), (255, 0, 191), (0, 255, 255), (128, 0, 255), (0, 64, 255), (255, 0, 0)]
