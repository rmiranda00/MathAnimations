from manimlib.imports import *
from Polyhedra import *

import time

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class ShowTetra(Scene):
	def construct(self):
		T = Tetrahedron()

		self.play(ShowCreation(T))
		self.wait(3)

class ShowCube(Scene):
    def construct(self):
        C = Cube()

        self.play(ShowCreation(C))
        self.wait(3)

class ShowDodec(Scene):
    def construct(self):
        D = Dodecahedron()

        self.play(ShowCreation(D))
        self.wait(3)

class Test(Scene):
    def construct(self):
        axes_config2 = {
        "x_min": 0,
        "x_max": 15,
        "x_axis_width": 15,
        "x_tick_frequency": 1,
        "x_leftmost_tick": 0,
        "x_labeled_nums": None,
        "x_axis_label": None,
        "y_min": -1,
        "y_max": 1,
        "z_min": -1,
        "z_max": 1,
        "z_axis_height": 2,
        "y_axis_height": 2,
        "y_tick_frequency": 1,
        "y_bottom_tick": None, # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": None,
        "axes_color": LIGHT_GREY,
        "graph_origin": 0 * DOWN + 0 * LEFT,
        "exclude_zero_label": True,
        "num_graph_anchor_points": 25,
        "default_graph_colors": GOLD,
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "function_color": WHITE,
        "area_opacity": 0.8,
        "num_rects": 50,
        "light_source": 15 * DOWN + 7 * LEFT + 10 * OUT,
        "number_line_config": {
            "include_tip": False,
        },        
                           
                       
    }

class ThreeDGraph(OldThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5.5,
            "x_max": 5.5,
            "y_min": -5.5,
            "y_max": 5.5,
            "z_min": -3.5,
            "z_max": 3.5,
        }
        a = ThreeDAxes(**axis_config)
        surface = ParametricSurface(self.sur,u_min=-3, u_max=3, v_min=-3, v_max=3)
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.add(a, surface)
        self.begin_ambient_camera_rotation(rate=0.04)
        self.wait(10)
        

    def sur(self, u, v):
        return [u, v, u**2 + v**2]