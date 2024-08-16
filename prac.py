from manim import *


class PlotCurve(Scene):
    def construct(self):
        # Define the curve function
        def curve_function(y):
            return (y - 1) * (y - 2) * (y - 3)

        # Create axes
        axes = Axes(
            x_range=[-3, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"color": BLUE},
        )

        # Plot the curve
        curve = ParametricFunction(lambda t: [curve_function(t), t, 0], t_range=[-3, 4], color=GREEN)

        # Add objects to the scene
        self.add(axes, curve)
        self.wait()


# Render the scene
if __name__ == "__main__":
    config = {"quality": "medium", "pixel_height": 720, "pixel_width": 1280}
    renderer = "cairo"  # or "opengl" for faster rendering
    scene = PlotCurve()
    scene.render(config=config, renderer=renderer)
